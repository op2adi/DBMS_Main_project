use makemytrip;
DROP table userids_passwords;
CREATE TABLE `userids_passwords` (
  `userid` int NOT NULL,
  `password` varchar(50) NOT NULL,
    is_locked CHAR(1) Not NULL ,
    attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL ,
    tries INT DEFAULT 0 NOT NULL ,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO userids_passwords (userid, password,is_locked) VALUES (12, 'W','F');
# DROP TRIGGER lock_account_trigger;
# DROP TRIGGER u
DELIMITER //

CREATE TRIGGER lock_account_trigger BEFORE INSERT ON userids_passwords
FOR EACH ROW
BEGIN
    IF NEW.tries >= 3 THEN
        SET NEW.is_locked = 'T';
        SET NEW.attempt_time = CURRENT_TIMESTAMP;
    END IF;
END//

DELIMITER ;
DELIMITER //
DROP event unlock_account_event;
CREATE EVENT unlock_account_event
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 2 SECOND
DO
    UPDATE userids_passwords SET is_locked = 'F' WHERE is_locked = 'T';

DELIMITER ;
