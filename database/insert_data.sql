USE BloodOrganDonation;


INSERT INTO hospital (hospital_name, city, contact) VALUES
('Apollo Hospital', 'Bangalore', '9876543210'),
('City Care', 'Chennai', '9123456780'),
('Global Hospital', 'Hyderabad', '9988776655'),
('Fortis Medical', 'Mumbai', '9012345678'),
('Sunrise Hospital', 'Delhi', '9876501234'),
('LifeLine Hospital', 'Pune', '9988123456'),
('Medico Center', 'Kolkata', '9765432109'),
('Care Plus', 'Mysore', '9345678123'),
('Unity Hospital', 'Coimbatore', '9090909090'),
('Green Cross', 'Kochi', '9887766554'),
('Rainbow Hospital', 'Vizag', '9445566778'),
('Hope Medical', 'Madurai', '9556677889'),
('Prime Health', 'Nagpur', '9112233445'),
('Aster Clinic', 'Rajkot', '9001122334'),
('Nova Hospital', 'Salem', '9881234567'),
('Healing Touch', 'Jaipur', '9778899001'),
('Metro Care', 'Lucknow', '9334455667'),
('Royal Hospital', 'Patna', '9223344556'),
('Elite Medical', 'Surat', '9667788990'),
('Wellness Hospital', 'Bhopal', '9554433221');

SELECT *
FROM  hospital;

INSERT INTO donor
(donor_name, age, gender, blood_group, city, phone, organ_donor, organ_type, last_donation_date)
VALUES
('Arjun',22,'Male','O+','Bangalore','9871111111',TRUE,'Kidney','2026-01-10'),
('Sneha',24,'Female','A+','Chennai','9871111112',FALSE,NULL,'2026-02-15'),
('Rahul',28,'Male','B+','Hyderabad','9871111113',TRUE,'Liver','2026-03-01'),
('Priya',21,'Female','AB+','Mumbai','9871111114',FALSE,NULL,'2026-01-25'),
('Karan',30,'Male','O-','Delhi','9871111115',TRUE,'Heart','2026-02-20'),
('Meera',26,'Female','A-','Pune','9871111116',FALSE,NULL,'2026-03-12'),
('Vikram',35,'Male','B-','Kolkata','9871111117',TRUE,'Kidney','2026-04-05'),
('Anjali',23,'Female','O+','Mysore','9871111118',FALSE,NULL,'2026-01-18'),
('Rohit',27,'Male','AB-','Coimbatore','9871111119',TRUE,'Liver','2026-03-22'),
('Divya',29,'Female','A+','Kochi','9871111120',FALSE,NULL,'2026-02-14'),
('Manoj',31,'Male','B+','Vizag','9871111121',TRUE,'Lung','2026-01-30'),
('Pooja',25,'Female','O-','Madurai','9871111122',FALSE,NULL,'2026-02-28'),
('Suresh',34,'Male','A-','Nagpur','9871111123',TRUE,'Pancreas','2026-03-15'),
('Nisha',22,'Female','AB+','Trichy','9871111124',FALSE,NULL,'2026-04-01'),
('Ajay',28,'Male','B-','Salem','9871111125',TRUE,'Kidney','2026-03-18'),
('Keerthi',24,'Female','O+','Jaipur','9871111126',FALSE,NULL,'2026-02-11'),
('Harish',32,'Male','A+','Lucknow','9871111127',TRUE,'Liver','2026-01-29'),
('Lavanya',27,'Female','B+','Patna','9871111128',FALSE,NULL,'2026-03-09'),
('Deepak',29,'Male','AB-','Surat','9871111129',TRUE,'Heart','2026-04-10'),
('Reshma',23,'Female','O-','Bhopal','9871111130',FALSE,NULL,'2026-02-16');

SELECT *
FROM donor;

INSERT INTO patient_request
(hospital_id, patient_name, blood_required, organ_required, required_units, urgency_level, request_date)
VALUES
(1,'Kiran','O+',NULL,2,'high','2026-05-01'),
(2,'Meena',NULL,'Kidney',1,'mid','2026-05-02'),
(3,'Raj','A+',NULL,3,'high','2026-05-03'),
(4,'Sanjay','B+',NULL,2,'low','2026-05-04'),
(5,'Anu',NULL,'Liver',1,'high','2026-05-05'),
(6,'Ravi','AB+',NULL,1,'mid','2026-05-06'),
(7,'Geetha','O-',NULL,2,'high','2026-05-07'),
(8,'Mohan',NULL,'Heart',1,'high','2026-05-08'),
(9,'Asha','A-',NULL,1,'mid','2026-05-09'),
(10,'Vijay','B-',NULL,2,'low','2026-05-10'),
(11,'Kavya',NULL,'Kidney',1,'high','2026-05-11'),
(12,'Naveen','O+',NULL,3,'mid','2026-05-12'),
(13,'Shreya','AB-',NULL,1,'high','2026-05-13'),
(14,'Arav',NULL,'Lung',1,'mid','2026-05-14'),
(15,'Bhavna','A+',NULL,2,'low','2026-05-15'),
(16,'Dinesh','B+',NULL,1,'high','2026-05-16'),
(17,'Preethi',NULL,'Pancreas',1,'mid','2026-05-17'),
(18,'Yash','O-',NULL,2,'high','2026-05-18'),
(19,'Ritika','AB+',NULL,1,'low','2026-05-19'),
(20,'Suraj',NULL,'Heart',1,'high','2026-05-20');

SELECT *
FROM patient_request;

INSERT INTO donation_record
(donor_id, hospital_id, donation_type, donation_date, donation_units)
VALUES
(1,1,'blood','2026-05-01',1),
(2,2,'blood','2026-05-02',1),
(3,3,'organ','2026-05-03',1),
(4,4,'blood','2026-05-04',2),
(5,5,'organ','2026-05-05',1),
(6,6,'blood','2026-05-06',1),
(7,7,'organ','2026-05-07',1),
(8,8,'blood','2026-05-08',1),
(9,9,'organ','2026-05-09',1),
(10,10,'blood','2026-05-10',2),
(11,11,'organ','2026-05-11',1),
(12,12,'blood','2026-05-12',1),
(13,13,'organ','2026-05-13',1),
(14,14,'blood','2026-05-14',2),
(15,15,'organ','2026-05-15',1),
(16,16,'blood','2026-05-16',1),
(17,17,'organ','2026-05-17',1),
(18,18,'blood','2026-05-18',2),
(19,19,'organ','2026-05-19',1),
(20,20,'blood','2026-05-20',1);

SELECT* 
FROM donation_record;

INSERT INTO donation_match
(request_id, donation_id, match_date)
VALUES
(1,1,'2026-05-01'),
(2,2,'2026-05-02'),
(3,3,'2026-05-03'),
(4,4,'2026-05-04'),
(5,5,'2026-05-05'),
(6,6,'2026-05-06'),
(7,7,'2026-05-07'),
(8,8,'2026-05-08'),
(9,9,'2026-05-09'),
(10,10,'2026-05-10'),
(11,11,'2026-05-11'),
(12,12,'2026-05-12'),
(13,13,'2026-05-13'),
(14,14,'2026-05-14'),
(15,15,'2026-05-15'),
(16,16,'2026-05-16'),
(17,17,'2026-05-17'),
(18,18,'2026-05-18'),
(19,19,'2026-05-19'),
(20,20,'2026-05-20');

SELECT * 
FROM donation_match;

INSERT INTO blood_inventory
(hospital_id, blood_group, available_units)
VALUES
(1,'O+',10),
(2,'A+',8),
(3,'B+',7),
(4,'AB+',5),
(5,'O-',6),
(6,'A-',4),
(7,'B-',3),
(8,'AB-',2),
(9,'O+',9),
(10,'A+',7),
(11,'B+',6),
(12,'AB+',4),
(13,'O-',5),
(14,'A-',3),
(15,'B-',2),
(16,'AB-',1),
(17,'O+',8),
(18,'A+',6),
(19,'B+',5),
(20,'AB+',4);

SELECT *
FROM blood_inventory;