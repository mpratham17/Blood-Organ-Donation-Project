
SELECT h.hospital_name,
       b.blood_group,
       b.available_units
FROM blood_inventory b
JOIN hospital h
ON b.hospital_id = h.hospital_id
ORDER BY h.hospital_name, b.blood_group;