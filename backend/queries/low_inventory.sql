SELECT hospital_id,
       blood_group,
       available_units
FROM blood_inventory
WHERE available_units < 5;
