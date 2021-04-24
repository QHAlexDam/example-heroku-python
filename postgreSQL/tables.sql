CREATE EXTENTION pgcrypto;

CREATE TABLE account {
    account_id SERIAL,
    account_username VARCHAR(20) NOT NULL,
    account_password TEXT NOT NULL,
    account_first_name VARCHAR(20) NOT NULL,
    account_last_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(account_id)
};