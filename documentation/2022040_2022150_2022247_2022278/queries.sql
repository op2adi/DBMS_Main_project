use makemytrip;

SELECT users.City, SUM(tickets.Amount) AS TotalAmount
FROM users
INNER JOIN tickets ON users.userid = tickets.userid
GROUP BY users.City
HAVING SUM(tickets.Amount) = (
    SELECT MAX(TotalSum)
    FROM (
        SELECT SUM(Amount) AS TotalSum
        FROM tickets,users where tickets.userid=users.userid
        GROUP BY users.City
    ) AS MaxSums
);



SELECT u.name, u.email, l.date_on, f.name AS Flight_Name, bl.Offers_Code AS offers, bl.Credit_card
  FROM Users u
   INNER JOIN Booked_Loungue l ON u.userid = l.userid
   INNER JOIN Flight f ON l.Flight_No = f.Flight_No
    INNER JOIN Loungue bl ON bl.Offers_code = l.Offers_code;


Select Name , COUNT( ti.Ticket_No) as total_tickets from Trains t , Tickets ti  where t.Train_No = ti.Train_No Group By T.name ;

# select * from transport ;

SELECT transport.*,flight.Name FROM TRANSPORT,flight WHERE Timings LIKE '%2024-03-%' AND vacany > 0 and (transport.Transport_id=flight.Transport_Id) ;

-- users who booked both train and flight

select users.userid,users.name from tickets,users where tickets.userid=users.userid AND Train_No is not NULL
intersect
select users.userid,users.name from tickets,users where tickets.userid=users.userid AND Flight_No is not NULL;


-- user requested to change userid used on update cascade contraint so it will run with no error

update users set userid = 1111 where userid = 8345;


-- there must not  be any user who has booked longue but no flight

select *
from booked_loungue,tickets where tickets.Flight_No=booked_loungue.Flight_No AND tickets.Flight_No is NULL;

-- removing age column to as only gives data redundancy
ALTER TABLE users DROP COLUMN age;


-- printing users who have booked loungues using a different command

SELECT u.Name
FROM Users u
WHERE EXISTS (
    SELECT 1
    FROM Booked_Loungue l
    WHERE u.userid = l.userid
);

-- Print tickets whose payment is not cleared

select User_id,Ticket_id from payments where Payment_Status!=1 and Ticket_id is not NULL;

SELECT u.userid, SUM(t.Amount) AS total_amount
FROM Users u
JOIN Payments p ON u.userid = p.User_id
JOIN Tickets t ON p.Ticket_id = t.Ticket_No
where Payment_Status=1
GROUP BY u.userid;

select name,count(user_id) as total_complaints from complaint,users where users.userid=complaint.user_id group by user_id order by count(user_id) desc;

-- should generate Error
update users set email = 'abc';

-- If we run the above query then we expect to get a error message to show up as the output as the above query violates the constraints of our database, as we have the constraint in out inputs such that ours emails entered should have an '@' and a .com or similar domain name in it.
