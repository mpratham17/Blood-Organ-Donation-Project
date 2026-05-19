SELECT blood_group,
       COUNT(*) AS total_donors
FROM donor
GROUP BY blood_group;