{{ config(materialized='table') }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['claim_id']) }} AS claim_key,
    c.claim_id,
    c.customer_id,
    c.provider_id,
    c.procedure_code,
    c.claim_date,
    c.status,
    c.claim_amount,
    p.standard_cost AS cost_of_procedure,
    current_date AS last_updated
FROM {{ source('healthcare_raw', 'claims') }} AS c
    LEFT JOIN {{ source('healthcare_raw', 'procedures') }} as p
        ON p.procedure_code = c.procedure_code
