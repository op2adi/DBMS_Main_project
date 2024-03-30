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
END //

-- DELIMITER ;

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

-- DELIMITER ;

-- Dropping the update_valid_tickets_trigger if it exists
DROP TRIGGER IF EXISTS update_valid_tickets_trigger;

-- Recreating the update_valid_tickets_trigger trigger
DELIMITER //

CREATE TRIGGER update_valid_tickets_trigger BEFORE INSERT ON Tickets
FOR EACH ROW
BEGIN
    IF NEW.date_of_journey < NOW() THEN
        SET NEW.is_valid = 0;
#         insert into tickets (Ticket_No, Train_No, Flight_No, Amount, Date_of_journey, Quantity, userid) VALUES (NEW.Ticket_No,NEW.Train_No,NEW.Flight_No,NEW.Amount,NEW.Date_of_journey,NEW.Date_of_journey,NEW.userid);
    END IF;
#         insert into tickets (Ticket_No, Train_No, Flight_No, Amount, Date_of_journey, Quantity, userid) VALUES (NEW.Ticket_No,NEW.Train_No,NEW.Flight_No,NEW.Amount,NEW.Date_of_journey,NEW.Date_of_journey,NEW.userid);
END//

-- DELIMITER ;

DELIMITER //


-- Dropping the validate_tickets_event if it exists
DROP EVENT IF EXISTS validate_tickets_event;

# -- Recreating the validate_tickets_event event only if it doesn't already exist
CREATE EVENT IF NOT EXISTS validate_tickets_event
ON SCHEDULE EVERY 10 SECOND
STARTS CURRENT_TIMESTAMP
DO
    UPDATE Tickets
    SET is_valid = 0
    WHERE date_of_journey < NOW();

# DELIMITER //

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

-- DELIMITER //

DELIMITER //
DROP TRIGGER IF EXISTS update_valid_tickets_trigger7;

create trigger update_valid_tickets_trigger7 BEFORE update on tickets
FOR EACH ROW
BEGIN
    IF NEW.date_of_journey > NOW() THEN
        SET NEW.is_valid = 1;
    ELSE
        SET NEW.is_valid = 0;
    END IF;
END;

# DROP PROCEDURE if exists delete_old_log_entries;
# CREATE PROCEDURE delete_old_log_entries()
# BEGIN
# #     select  sleep(3);
#     DELETE FROM log_entry
#     ORDER BY attempt_time ASC
#     LIMIT 1;
# END //
#
# DROP TRIGGER IF EXISTS log_entry_count_trigger;
# CREATE TRIGGER log_entry_count_trigger
# AFTER INSERT ON log_entry
# #     select sleep(3);
# FOR EACH ROW
# BEGIN
#     DECLARE entry_count INT;
#
#     -- Get the count of entries in the log_entry table
#     SELECT COUNT(*) INTO entry_count FROM log_entry;
#
#     -- If the count exceeds 10, delete the oldest entry
#     IF entry_count > 3 THEN
#         CALL delete_old_log_entries();
#     END IF;
# END//
#
# DELIMITER ;
