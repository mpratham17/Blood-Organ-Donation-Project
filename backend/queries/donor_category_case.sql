SELECT donor_name,
       age,
       blood_group,
       CASE
           WHEN age < 25 THEN 'Young Donor'
           WHEN age BETWEEN 25 AND 30 THEN 'Adult Donor'
           ELSE 'Senior Donor'
       END AS donor_category
FROM donor;