
SELECT blood_required,
       COUNT(*) AS total_requests
FROM patient_request
WHERE blood_required IS NOT NULL
GROUP BY blood_required
ORDER BY total_requests DESC;