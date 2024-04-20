use makemytrip;

select * from transprt;

start transaction set vacany = 2;

start transaction t1 ;
q1 : select vacany from transport;
q2 : update transport set vacany = vacany - 5; -- assuming r=that only 5 tickets are available
start transaction t2;
q3 : select vacany from transport;
q4 : update transport set vacany = vacany - 5; -- assuming r=that only 5 tickets are available

1st transaction will commit  : - t1 will commit : = t1:commit

2nd will commit : - t2 will commit : = t2:commit 
order is q1,q2,q3,c,q4 see it contains a faulty incossistency 

-- After 1st commit the dtabase will be in consistent state as the vacany will be 0 which is possible.
-- But after 2nd commit the dtabase will be in inconsistent state as the vacany will be -5 which is not possible as integrity constraint is present.

-- the sequence of transactions state here will as provided but as database locks the row and so it wont affect

-- The situation described involves a read-write conflict in the context of database transactions. Let’s break it down:

-- Read operation: A transaction reads data from the database without modifying it.
-- Write operation: A transaction modifies data in the database and saves the changes.
-- Now, let’s analyze the scenario you’ve presented:

-- Transaction T1:
-- Reads the original value of the “vacancy” field from the “transport” table (que
-- Transaction T2:
-- Starts after T1.
-- Reads the original value of the “vacancy” field from the “transport” table (query q3).ry q1).
-- Updates the “vacancy” field by subtracting 5 (query q2).
-- Updates the “vacancy” field by subtracting 5 (query q4).
-- The issue arises when both transactions are interleaved during execution. Here’s what happens:

-- T1 reads the original value of “vacancy” and waits for T2 to finish.
-- T2 also reads the original value of “vacancy,” overwrites it, and commits.
-- When T1 reads from “vacancy” again, it discovers two different versions of the value. This inconsistency forces T1 to abort because it doesn’t know which value to use. This is an example of an unrepeatable read or a read-write conflict1.

-- 2nd Conflicting Transaction

-- Now for this I NEED TO to give 2 diff transactions in a conflicting state
-- This is the best idea i thought 
start transaction t3 ;
q1: delete from userids_passwords;
q2: Rollback

start transaction t4 ; 
q3: select * from users;
q4: INSERT Into userids_passwords(userid,password,is_locked) VALUES
(8895,'Aditya@1998','F');
q5: INSERT INTO Users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES
(8895, 'zgonzalez@example.com', 'Connie Williams', '5152121722', 'F', '0569', 'New Karenview', '489077', '2005-11-26');
q6:commit

-- The 2nd transaction will be in inconsistent state as the userids_passwords table will be empty and the users table will have a record with userid 8895 which is not present in the userids_passwords table. This violates the referential integrity constraint between the two tables.

-- Also Lets say Vikraam (check spelling ) ji was there was wants to delee all transactions (by mistake you know he is a good person then Mukesh ji came he found out userid 8895 is available as there will be no recrds so mukkesh ji tried to insert the record but dbms has locked) so when vikraam ji did rollback mukesh ji got an error userid exist Moye Moye


order of execution q1,q3,q4,q5,q2,q6 
Soon it will fail as it will give an error

-- This is write read or irrepeatable read this is because as we have seen write read hence it is god to go

