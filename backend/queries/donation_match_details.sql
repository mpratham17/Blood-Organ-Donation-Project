
SELECT pr.patient_name,
       d.donor_name,
       dm.match_date
FROM donation_match dm
JOIN patient_request pr
ON dm.request_id = pr.request_id
JOIN donation_record dr
ON dm.donation_id = dr.donation_id
JOIN donor d
ON dr.donor_id = d.donor_id;