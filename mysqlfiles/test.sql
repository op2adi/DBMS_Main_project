use makemytrip;

start transaction;

UPDATE transport SET Vacany = Vacany-1 WHERE Transport_id =  8824410;
UPDATE transport SET Vacany = Vacany-1 WHERE Transport_id =  8824410;

COMMIT;
# ROLLBACK ;
