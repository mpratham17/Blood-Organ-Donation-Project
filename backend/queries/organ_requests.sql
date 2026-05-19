
SELECT patient_name,
       organ_required,
       urgency_level
FROM patient_request
WHERE organ_required IS NOT NULL;