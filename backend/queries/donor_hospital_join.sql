SELECT d.donor_name,
       h.hospital_name,
       dr.donation_type,
       dr.donation_date
FROM donation_record dr
JOIN donor d
ON dr.donor_id = d.donor_id
JOIN hospital h
ON dr.hospital_id = h.hospital_id;
