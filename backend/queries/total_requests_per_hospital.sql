
SELECT h.hospital_name,
       COUNT(pr.request_id) AS total_requests
FROM hospital h
JOIN patient_request pr
ON h.hospital_id = pr.hospital_id
GROUP BY h.hospital_name;