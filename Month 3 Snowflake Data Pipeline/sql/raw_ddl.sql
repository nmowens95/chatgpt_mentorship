/*
DDL for Healthcare Data Pipeline in Snowflake for raw schema
*/
CREATE OR REPLACE TABLE healthcare.raw.providers (
    provider_id STRING PRIMARY KEY,
    provider_name STRING,
    specialty STRING,
    location STRING
);

CREATE OR REPLACE TABLE healthcare.raw.procedures (
    procedure_code STRING PRIMARY KEY,
    description STRING,
    standard_cost FLOAT
);

CREATE OR REPLACE TABLE healthcare.raw.claims (
    claim_id STRING PRIMARY KEY,
    customer_id STRING,
    provider_id STRING,
    procedure_code STRING,
    claim_date DATE,
    claim_amount FLOAT,
    status STRING
);

CREATE OR REPLACE TABLE heathcare.raw.customers (
    customer_id STRING PRIMARY KEY,
    first_name STRING,
    last_name STRING,
    gender STRING,
    dob DATE,
    zip_code STRING 
);