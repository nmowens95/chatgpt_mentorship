CREATE TABLE IF NOT EXISTS customers_gold (
	customer_id VARCHAR(256) NOT NULL,
	full_name TEXT,
	email TEXT,
	phone_number TEXT,
	address TEXT,
	date_of_birth DATE,
	signup_date DATE,
	is_active BOOLEAN,
	account_balance NUMERIC(12,2),
	preferred_contact_method TEXT,
	loaded_at TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (customer_id)
)