CREATE TABLE IF NOT EXISTS claims_gold (
	claim_id VARCHAR(256) NOT NULL,
	customer_id VARCHAR(256) NOT NULL,
	claim_date DATE,
	claim_amount NUMERIC(12,2),
	currency TEXT,
	status TEXT,
	service_type TEXT,
	claim_description TEXT,
	provider_name TEXT,
	follow_up_required BOOLEAN,
	loaded_at TIMESTAMP DEFAULT NOW(),
	PRIMARY KEY (claim_id)
);