{{ config(materialized='table') }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['procedure_code']) }} AS procedure_key,
    procedure_code,
    description,
    current_date() AS last_updated
FROM {{ source('healthcare_raw', 'procedures') }}