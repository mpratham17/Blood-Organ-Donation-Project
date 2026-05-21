USE BloodOrganDonation;

ALTER TABLE donor AUTO_INCREMENT = 1;
ALTER TABLE hospital AUTO_INCREMENT = 1;
ALTER TABLE donor AUTO_INCREMENT = 1;
ALTER TABLE patient_request AUTO_INCREMENT = 1;
ALTER TABLE donation_record AUTO_INCREMENT = 1;
ALTER TABLE donation_match AUTO_INCREMENT = 1;

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



INSERT INTO donor
(donor_name, age, gender, blood_group, city, phone, organ_donor, organ_type, last_donation_date)
VALUES
('Arjun',22,'Male','O+','Bangalore','9871111111',TRUE,'Kidney',NULL),
('Sneha',24,'Female','A+','Chennai','9871111112',FALSE,NULL,NULL),
('Rahul',28,'Male','B+','Hyderabad','9871111113',TRUE,'Liver',NULL),
('Priya',21,'Female','AB+','Mumbai','9871111114',FALSE,NULL,NULL),
('Karan',30,'Male','O-','Delhi','9871111115',TRUE,'Heart',NULL),
('Meera',26,'Female','A-','Pune','9871111116',FALSE,NULL,NULL),
('Vikram',35,'Male','B-','Kolkata','9871111117',TRUE,'Kidney',NULL),
('Anjali',23,'Female','O+','Mysore','9871111118',FALSE,NULL,NULL),
('Rohit',27,'Male','AB-','Coimbatore','9871111119',TRUE,'Liver',NULL),
('Divya',29,'Female','A+','Kochi','9871111120',FALSE,NULL,NULL),
('Manoj',31,'Male','B+','Vizag','9871111121',TRUE,'Lung',NULL),
('Pooja',25,'Female','O-','Madurai','9871111122',FALSE,NULL,NULL),
('Suresh',34,'Male','A-','Nagpur','9871111123',TRUE,'Pancreas',NULL),
('Nisha',22,'Female','AB+','Trichy','9871111124',FALSE,NULL,NULL),
('Ajay',28,'Male','B-','Salem','9871111125',TRUE,'Kidney',NULL),
('Keerthi',24,'Female','O+','Jaipur','9871111126',FALSE,NULL,NULL),
('Harish',32,'Male','A+','Lucknow','9871111127',TRUE,'Liver',NULL),
('Lavanya',27,'Female','B+','Patna','9871111128',FALSE,NULL,NULL),
('Deepak',29,'Male','AB-','Surat','9871111129',TRUE,'Heart',NULL),
('Reshma',23,'Female','O-','Bhopal','9871111130',FALSE,NULL,NULL);



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
FROM  hospital;

SELECT *
FROM donor;

SELECT *
FROM patient_request;

SELECT* 
FROM donation_record;

SELECT * 
FROM donation_match;

SELECT * FROM blood_inventory;