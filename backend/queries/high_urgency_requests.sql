SELECT patient_name,
       blood_required,
       organ_required,
       request_date
FROM patient_request
WHERE urgency_level = 'high';