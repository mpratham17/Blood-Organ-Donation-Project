USE bloodorgandonation;

DELIMITER //
CREATE TRIGGER update_blood_inventory
AFTER INSERT ON donation_record
FOR EACH ROW
BEGIN 
	DECLARE donor_blood_group VARCHAR(5);
    
    IF NEW.donation_type='blood' THEN
		SELECT blood_group
        INTO donor_blood_group
        FROM donor
        WHERE donor_id=NEW.donor_id;
        
        IF EXISTS(
			SELECT *
			FROM blood_inventory
            WHERE hospital_id=NEW.hospital_id AND blood_group=donor_blood_group) 
            THEN
				UPDATE blood_inventory
                SET available_units=available_units+NEW.donation_units
                WHERE hospital_id=NEW.hospital_id AND blood_group=donor_blood_group;
			ELSE 
				INSERT INTO blood_inventory ( hospital_id, blood_group, available_units) VALUES (NEW.hospital_id,donor_blood_group,NEW.donation_units);
		END IF;
				
	END IF;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER donation_cooldown_validation
BEFORE INSERT ON donation_record
FOR EACH ROW 

BEGIN
	DECLARE last_date DATE;
    
    IF NEW.donation_type='blood' THEN
		SELECT last_donation_date
        INTO last_date
        FROM donor
        WHERE donor_id=NEW.donor_id;
        
        IF last_date IS NOT NULL AND DATEDIFF(NEW.donation_date,last_date)<90 THEN
			SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT='Donor still in cooldown period';
		
        ELSE 
			UPDATE donor
            SET last_donation_date=NEW.donation_date
            WHERE donor_id=NEW.donor_id;
		END IF;
	END IF;
END //
DELIMITER ;

