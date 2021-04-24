#!/usr/bin/env python3

import http.server
import requests
import os
from urllib.parse import unquote, parse_qs
import threading 
from socketserver import ThreadingMixIn
import psycopg2
from config import config

def connectDB(): 
  connection = None
  try:
    params = config()

    connection = psycopg2.connect(**params)

    cursor = connection.cursor()

    print('PostgreSQL database version:')
    cursor.execute('SELECT version()')

    db_version = cursor.fetchone()
    print(db_version)

    cursor.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if connection is not None:
      connection.close()
      print('db connection closed')

class ThreadHTTPServer(ThreadingMixIn, http.server.HTTPServer):
    "This is an HTTPServer that supports thread-based concurrency."

class Server(http.server.BaseHTTPRequestHandler):
  def do_HEAD(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(bytes('<html><head><title>Title goes here.</title></head><body><H1>Hello world</H1></body></html>','utf-8'))
    #self.wfile.close()
    print('hello from get')
  
  def do_POST(self):
    self.send_response(200)
    print('hello from post')

if __name__ == '__main__':
  connectDB()
  server_address = ('', int(os.environ.get('PORT', '8000')))
  httpd = ThreadHTTPServer(server_address, Server)
  httpd.serve_forever()
    