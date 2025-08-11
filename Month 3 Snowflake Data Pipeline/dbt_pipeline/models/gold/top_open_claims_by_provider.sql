SELECT 
    pr.provider_name,
    pr.specialty,
    pr.location,
    claim.claim_date,
    SUM(claim.cost_of_procedure) as cost_of_procedure,
    SUM(claim.claim_amount) AS claim_amount
    
FROM {{ ref("fact_claims") }} AS claim
    LEFT JOIN {{ ref("dim_providers") }} AS pr
        ON pr.provider_id = claim.provider_id
WHERE 1=1
    AND claim.status = 'Approved'
    AND YEAR(claim.claim_date) = YEAR(CURRENT_DATE())
GROUP BY
    pr.provider_name,
    pr.specialty, 
    pr.location,
    claim.claim_date
ORDER BY SUM(claim.claim_amount) DESC