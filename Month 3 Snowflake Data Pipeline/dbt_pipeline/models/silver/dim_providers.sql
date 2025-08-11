{{ config(materialized='table') }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['provider_id']) }} AS provider_key,
    provider_id,
    TRIM(provider_name) AS provider_name,
    TRIM(specialty) AS specialty,
    TRIM(location) AS location,
    current_date() AS last_updated
FROM {{ source('healthcare_raw', 'providers') }}