SELECT donor_name,
       city
FROM donor
WHERE donor_id IN (
    SELECT donor_id
    FROM donation_record
    WHERE donation_type = 'organ'
);