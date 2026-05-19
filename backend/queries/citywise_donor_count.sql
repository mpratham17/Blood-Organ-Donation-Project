
SELECT city,
       COUNT(*) AS total_donors
FROM donor
GROUP BY city
HAVING COUNT(*) >= 1;