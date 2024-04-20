use makemytrip

-- Transactions for Non conflicting transactions


start transaction t1 :
q1 :  update userids_passwords set password = 12 where userid = 1111;
q2 : commit


start transaction t2 :
q3 :  update userids_passwords set password = 12 where userid = 9080;
q4 : commit


start transaction t3 :
q5 :  INSERT INTO Transport (Transport_id, Start_Loc, Destn_Loc, Timings, Price, Vacany)
VALUES
    (1692553, 'Lake Carolyntown', 'South Eric', '2025-10-04 05:01:26', 63, 100),
q6 : commit


start transaction t4 :
q7 :  INSERT INTO Complaint (complaint_id, user_id, complaint_description) VALUES
(25337, 9080, 'Bit her compare identify consider security nice. Fund compare might ready hard. Four store language involve issue.');
q8 : commit

start transaction t5 :
q9 :  INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount, Date_of_journey, Quantity,userid)
VALUES
    (17541, NULL, 3039, 748, '2011-04-28', 1,2377);
q10 : commit



any order will work as it is a serializable SCHEDULE YUps

-- why this works ?
-- Ans s  it works than anything else because all transactions dont have any dependencies so if occurs in this fashion so it will never produces any error



-- These transactions are deemed non-conflicting due to their independent nature in operating on distinct data sets within the database. Each transaction encapsulates a unique set of operations, ensuring that they proceed without interference from one another.

-- Consider the breakdown:

-- Transaction t1 focuses on updating the password for a specific user identified by the userid 1111, while transaction t2 targets a different user with userid 9080 for a password update. These updates are isolated and do not overlap, thus eliminating any potential conflicts between the two transactions.

-- Transaction t3 involves the insertion of a new record into the Transport table, detailing transport information such as the Transport_id, Start_Loc, Destn_Loc, Timings, Price, and Vacancy. This insertion operation operates independently of the updates carried out by t1 and t2, guaranteeing a lack of conflict.

-- Similarly, transaction t4 deals with the insertion of a complaint record into the Complaint table, assigning a unique complaint_id to a user identified by the user_id 9080 and providing a description of the complaint. As this operation pertains to a separate table and does not intersect with the operations of other transactions, it proceeds without conflict.

-- Lastly, transaction t5 handles the insertion of a new ticket record into the Tickets table, specifying details such as Ticket_No, Train_No, Flight_No, Amount, Date_of_journey, Quantity, and userid. This insertion operation operates independently of the preceding transactions, ensuring a lack of overlap or interference.

-- Due to the absence of shared data or dependencies across these transactions, they can be executed in any order without causing inconsistencies or conflicts within the database. This property ensures the serializability of the schedule, allowing transactions to execute concurrently without impacting each other's outcomes.