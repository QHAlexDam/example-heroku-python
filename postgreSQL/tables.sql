CREATE EXTENSION pgcrypto;

CREATE TABLE account (
    account_id SERIAL,
    account_username VARCHAR(20) NOT NULL,
    account_password TEXT NOT NULL,
    account_first_name VARCHAR(20) NOT NULL,
    account_last_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(account_id)
);

INSERT INTO account (account_username, account_password, account_first_name, account_last_name) 
    VALUES ('admin', crypt('password', gen_salt('bf')), 'I am the', 'admin now');