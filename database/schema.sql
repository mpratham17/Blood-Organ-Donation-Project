CREATE DATABASE BloodOrganDonation;
USE BloodOrganDonation;
CREATE TABLE donor(
	donor_id INT PRIMARY KEY auto_increment,
    donor_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male','Female','Others') NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    city VARCHAR(20) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    organ_donor BOOLEAN NOT NULL DEFAULT FALSE,
    organ_type VARCHAR(15),
    last_donation_date DATE
);
CREATE TABLE hospital(
	hospital_id INT PRIMARY KEY auto_increment,
    hospital_name VARCHAR(15) NOT NULL,
    city VARCHAR(15) NOT NULL,
    contact VARCHAR(15) NOT NULL
);
CREATE TABLE patient_request(
	request_id INT PRIMARY KEY auto_increment,
    hospital_id INT NOT NULL,
    patient_name VARCHAR(20) NOT NULL,
    blood_required VARCHAR(5),
    organ_reqired VARCHAR(10),
    required_units INT,
    urgency_level ENUM('low','mid','high') NOT NULL,
    request_date DATE NOT NULL,
    
    FOREIGN KEY(hospital_id) REFERENCES hospital(hospital_id)
);
CREATE TABLE donation_record(
	donation_id INT PRIMARY KEY auto_increment,
	donor_id INT NOT NULL,
	hospital_id INT NOT NULL,
	donation_type ENUM('bood','organ') NOT NULL,
	donation_date DATE NOT NULL,
	donation_units int,
	
	FOREIGN KEY(donor_id) REFERENCES donor(donor_id),
	FOREIGN KEY(hospital_id) REFERENCES hospital(hospital_id)
);
CREATE TABLE donation_match(
	match_id INT PRIMARY KEY auto_increment,
    request_id INT NOT NULL,
    donation_id INT NOT NULL,
    match_date DATE NOT NULL,
    
    FOREIGN KEY(request_id) REFERENCES patient_request(request_id),
    FOREIGN KEY(donation_id) REFERENCES donation_record(donation_id)
);
CREATE TABLE blood_inventory(
	hospital_id INT NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    available_units INT DEFAULT 0,
    
    PRIMARY KEY(hospital_id,blood_group),
    FOREIGN KEY(hospital_id) REFERENCES hospital(hospital_id)
);