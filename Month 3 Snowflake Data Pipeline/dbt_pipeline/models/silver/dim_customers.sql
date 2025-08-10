WITH cust AS (
    SELECT
        customer_id,
        TRIM(first_name) AS first_name,
        TRIM(last_name) AS last_name,
        gender,
        dob,
        CASE
            WHEN LENGTH(zip_code) != 5
            THEN NULL
            ELSE zip_code
        END AS zip_code,
        current_date() AS last_updated
    FROM  {{ source('healthcare_raw', 'customers') }}
    )

SELECT
    {{ dbt_utils.generate_surrogate_key(['customer_id']) }} AS customer_key,
    customer_id,
    first_name,
    last_name,
    gender,
    dob,
    zip_code,
    IFF(zip_code IS NULL, 1, 0) AS zip_flag,
    last_updated
FROM cust
ORDER BY customer_id