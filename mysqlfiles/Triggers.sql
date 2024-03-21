USE makemytrip;

-- Dropping the lock_account_trigger if it exists
DROP TRIGGER IF EXISTS lock_account_trigger;

-- Recreating the lock_account_trigger trigger
DELIMITER //

CREATE TRIGGER lock_account_trigger BEFORE UPDATE ON userids_passwords
FOR EACH ROW
BEGIN
    IF NEW.tries >= 3 THEN
        SET NEW.is_locked = 'T';
        SET NEW.attempt_time = CURRENT_TIMESTAMP;
    END IF;
END//

DELIMITER ;

-- Dropping the unlock_account_event if it exists
DROP EVENT IF EXISTS unlock_account_event;

-- Recreating the unlock_account_event event only if it doesn't already exist
CREATE EVENT IF NOT EXISTS unlock_account_event
ON SCHEDULE EVERY 10 SECOND
STARTS CURRENT_TIMESTAMP
DO
    UPDATE userids_passwords
    SET is_locked = 'F', tries = 0
    WHERE is_locked = 'T';

DELIMITER ;

-- Dropping the update_valid_tickets_trigger if it exists
DROP TRIGGER IF EXISTS update_valid_tickets_trigger;

-- Recreating the update_valid_tickets_trigger trigger
DELIMITER //

CREATE TRIGGER update_valid_tickets_trigger BEFORE INSERT ON Tickets
FOR EACH ROW
BEGIN
    IF NEW.date_of_journey < NOW() THEN
        SET NEW.is_valid = 0;
    END IF;
END//

DROP TRIGGER IF EXISTS update_valid_tickets_trigger_payment;
CREATE TRIGGER update_valid_tickets_trigger AFTER INSERT ON Tickets
FOR EACH ROW
BEGIN
    DECLARE ticket_exists INT;

    -- Check if the newly inserted ticket already exists in payments table
    SELECT COUNT(*) INTO ticket_exists FROM payments WHERE ticket_no = NEW.ticket_no;

    -- If the ticket does not exist in payments table, insert it
    IF ticket_exists = 0 THEN
        INSERT INTO payments (Payment_Id, user_id, Ticket_id,Payment_Status,Hotel_id,date_of_payment)
        VALUES ();
    END IF;
END//

DELIMITER ;

-- Dropping the validate_tickets_event if it exists
DROP EVENT IF EXISTS validate_tickets_event;

-- Recreating the validate_tickets_event event only if it doesn't already exist
CREATE EVENT IF NOT EXISTS validate_tickets_event
ON SCHEDULE EVERY 10 SECOND
STARTS CURRENT_TIMESTAMP
DO
    UPDATE Tickets
    SET is_valid = 0
    WHERE date_of_journey < NOW();

DELIMITER //
DROP TRIGGER IF EXISTS update_valid_tickets_trigger8;
CREATE TRIGGER update_valid_tickets_trigger8 BEFORE INSERT ON Tickets
FOR EACH ROW
BEGIN
    IF NEW.date_of_journey < NOW() THEN
        SET NEW.is_valid = 0;
    ELSE
        SET NEW.is_valid = 1;
    END IF;
END;

DELIMITER ;
