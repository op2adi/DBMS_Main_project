use makemytrip;
DELETE FROM users;
DELETE FROM complaint;
DELETE FROM loungue;
DELETE FROM transport;
DELETE FROM flight;
DELETE FROM trains;
DELETE FROM booked_loungue;
DELETE FROM tickets;
DELETE FROM hotels;
DELETE FROM hotel_invoice;
DELETE FROM payments;
DELETE FROM holidaypackage;
DELETE FROM holiday_pay;
delete From userids_passwords;

INSERT Into userids_passwords(userid,password,is_locked) VALUES
(8895,'Aditya@1998','F'),
(1111,'Aditya@1998','F'),
(2377,'Aditya@1998','F'),
(3066,'Aditya@1998','F'),
(4145,'Aditya@1998','F'),
(5545,'Aditya@1998','F'),
(2562,'Aditya@1998','F'),
(3138,'Aditya@1998','F'),
(3635,'Aditya@1998','F'),
(6572,'Aditya@1998','F'),
(9080,'Aditya@1998','F'),
(8345,'Aditya@1998','F');

INSERT INTO Users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES
(8895, 'zgonzalez@example.com', 'Connie Williams', '5152121722', 'F', '0569', 'New Karenview', '489077', '2005-11-26'),
(6572, 'opeterson@example.com', 'Don Patel', '8671506984', 'M', '5090', 'Jacksonmouth', '455650', '1996-12-14'),
(3635, 'jonathan35@example.net', 'Tracy Bryant', '2660146278', 'M', '3936', 'Port Janet', '591937', '1980-01-05'),
(4145, 'strongsabrina@example.org', 'Carrie Ross', '3470101245', 'F', '80532', 'New Catherine', '656736', '1992-05-25'),
(5545, 'samantha86@example.org', 'Bryan Cole', '7764923567', 'F', '7156', 'New Michaelbury', '716780', '1987-02-12'),
(2562, 'zacharydaniels@example.com', 'Chad Davis', '9347709345', 'M', '8905', 'Lake Kristinatown', '473586', '1974-08-02'),
(9080, 'jessica28@example.net', 'Donald Sanchez', '6403857742', 'M', '7698', 'Anitaview', '734803', '1989-09-01'),
(2377, 'kristen88@example.org', 'Tamara Arias', '8426163966', 'F', '9241', 'Lake Pamela', '316230', '1968-03-14'),
(3066, 'danielharrell@example.org', 'Timothy Johnson', '4438085941', 'F', '40803', 'Barrettburgh', '123607', '2003-02-13'),
(8345, 'rodgersrichard@example.net', 'Michael Thompson', '2412212768', 'F', '12316', 'Brittneyport', '700354', '1991-06-23');
INSERT INTO Complaint (complaint_id, user_id, complaint_description) VALUES
(2507, 9080, 'Bit her compare identify consider security nice. Fund compare might ready hard. Four store language involve issue.'),
(4284, 9080, 'At around business fire example put. Item at account both ability beat. Economy within pay little image. Student record food price other power forget. Perform cut knowledge bank specific. Tax color alone professor.'),
(3262, 2562, 'Method war hour. Scene daughter standard issue. Wrong drive end chance quite. Economic fly interesting great pull sea speak administration.'),
(6478, 8345, 'Skin fish movement attention travel return today until. Mission detail her feel too analysis control. Officer student lose song hold.'),
(5216, 2562, 'Inside people song national happy a night. Economy suddenly long maintain science. Spring break identify several. Every arm trip whole budget itself cause. Fish actually yet material must offer learn including. Very must similar own pass guy inside.'),
(2458, 9080, 'Decision end market police another information often husband. Believe provide section apply her foreign. Also arrive why food until.'),
(8240, 5545, 'Particularly lot item ok. Behind buy eight identify. Teach another many kid avoid garden. Simple organization figure understand. Buy kid view night challenge thank perform order. Option ground detail later about whom.'),
(2658, 9080, 'Share keep arrive relate place condition share list. Artist amount maintain difference. Different recently account it. Pull activity as each line simply. Charge such capital to these.'),
(6630, 3066, 'Establish upon evidence quickly. Whole represent face performance source. Improve realize strategy while size. Teacher treatment despite move produce discuss.'),
(5180, 9080, 'Education collection week traditional. Wait scene consider southern occur. Own smile early today. Great raise somebody foreign next.');
INSERT INTO Loungue (Offers_code, Credit_Card, Timings, Place) VALUES
('DtHAT7gr', 'Kotak Mahindra Bank', '1973-04-23 13:10:14', '23193 Mckay Rapids Websterchester, SD 25499'),
('TMnSg3gO', 'Axis Bank', '1979-06-27 16:44:15', '0332 Rhonda Valleys Port Sarah, ND 47596'),
('WojG4orL', 'HDFC Bank', '2002-04-29 12:05:28', '6233 Charlotte Square Evanmouth, FM 88074'),
('jUssSnrE', 'Axis Bank', '1984-08-19 00:50:47', '4186 Sellers Street South Jennifer, OR 93257'),
('2TcTW0XX', 'State Bank of India', '2019-12-07 09:00:58', '3763 Rebecca Lights Suite 548 South Richardland, NY 89462'),
('23gb3tZ0', 'State Bank of India', '1978-06-14 15:20:42', '7026 Ross Route Taylorstad, UT 36213'),
('wvpgvvus', 'Kotak Mahindra Bank', '2018-04-25 14:43:08', '845 Margaret Keys Nicholasfurt, HI 14097'),
('dTF02CdV', 'Axis Bank', '1978-09-28 20:20:12', '7418 Bradley Falls Apt. 158 Laurenport, AK 33224'),
('oMF6W1pJ', 'HDFC Bank', '1989-05-22 21:27:18', '0184 Owens Extensions Benjaminmouth, NY 31028'),
('2IcygsLQ', 'Axis Bank', '1987-03-30 14:47:22', '8778 Morgan Mountains Apt. 884 Jonesview, OH 07974');
INSERT INTO Transport (Transport_id, Start_Loc, Destn_Loc, Timings, Price, Vacany)
VALUES
    (1692550, 'Lake Carolyntown', 'South Eric', '2023-10-04 05:01:26', 63, 100),
    (1692551, 'South Eric', 'Lake Carolyntown', '2023-10-04 05:01:26', 63, 100),
    (2994091, 'Port Teresaborough', 'New Amanda', '2023-03-16 00:29:50', 637, 100),
    (2994092, 'New Amanda', 'Port Teresaborough', '2023-03-16 00:29:50', 637, 100),
    (3906758, 'Lake Brian', 'Reneeville', '2023-05-02 04:33:29', 130, 100),
    (3906759, 'Reneeville', 'Lake Brian', '2023-05-02 04:33:29', 130, 100),
    (5566892, 'South Sheila', 'South Edwardmouth', '2023-03-03 06:39:05', 489, 100),
    (5566893, 'South Edwardmouth', 'South Sheila', '2023-03-03 06:39:05', 489, 100),
    (6071396, 'Mikaylaland', 'South Rickyview', '2023-11-05 01:17:10', 202, 100),
    (6071397, 'South Rickyview', 'Mikaylaland', '2023-11-05 01:17:10', 202, 100),
    (7503402, 'North Alanstad', 'Rachelfort', '2023-12-03 23:17:30', 741, 100),
    (7503403, 'Rachelfort', 'North Alanstad', '2023-12-03 23:17:30', 741, 100),
    (9601069, 'Ortizmouth', 'Smithview', '2025-02-10 22:25:21', 983, 100),
    (9601070, 'Smithview', 'Ortizmouth', '2025-02-10 22:25:21', 983, 100),
    (8824409, 'Hudsonchester', 'South Kerrystad', '2024-08-10 02:10:27', 249, 100),
    (8824410, 'South Kerrystad', 'Hudsonchester', '2024-08-10 02:10:27', 249, 100),
    (1760014, 'New Glenn', 'West Joymouth', '2024-01-20 05:21:08', 219, 100),
    (1760015, 'West Joymouth', 'New Glenn', '2024-01-20 05:21:08', 219, 100),
    (8868283, 'North Sarah', 'East Kellyfort', '2024-03-16 12:57:58', 748, 100),
    (8868284, 'East Kellyfort', 'North Sarah', '2024-03-16 12:57:58', 748, 100);

INSERT INTO Trains (Train_No, Transport_Id, Name)
VALUES
    (1580, 6071396, 'HGTREDFBNDJMFCAYH'),
    (1734, 8824410, 'EJWVWWIQSUAUY'),
    (8916, 1760015, 'GBZVZEOVFGJDXSDXWCP'),
    (4875, 3906759, 'XWAHDTVZCA'),
    (6607, 7503403, 'NGQCDPCPMPRLVAVGVOWK'),
    (3482, 6071397, 'YLPKCQWINQKJDSREEL'),
    (3442, 2994091, 'AKJEOIZCRSSEFJ'),
    (1828, 1692550, 'DYHVBQBAOCDAQFGQULGF'),
    (8436, 9601070, 'FTWDLEAPIA'),
    (6310, 1760014, 'SAUJCFAWVYFQ');
INSERT INTO Flight (Flight_No, Transport_Id, Name)
VALUES
    (9220, 5566893, 'NKKEGKKCOITMBX'),
    (8991, 8824409, 'HTNQGYSJMHVCVO'),
    (9684, 7503402, 'MDJJRQIFBFF'),
    (9986, 8868284, 'EMTLXGZJQXNPDYUJ'),
    (9811, 3906758, 'WTAXUREMDFKGR'),
    (5911, 1692551, 'CPGNTSPGOABFXIPYDGX'),
    (3039, 8868283, 'ANBXKCIMVC'),
    (7876, 5566892, 'PIGYJCEQFVGEBX'),
    (6830, 2994092, 'LEYPGTAVIGUMKSOU'),
    (2266, 9601069, 'GGKNOVATBJ');
INSERT INTO booked_loungue (Date_on, Offers_code, userid, Flight_No)
VALUES
    ('2024-11-10 19:30:57', 'oMF6W1pJ', 2377, 9986),
    ('2024-11-10 19:30:57', 'jUssSnrE', 2377, 9684),
    ('2024-11-10 19:30:57', 'dTF02CdV', 5545, 6830),
    ('2024-11-10 19:30:57', '2TcTW0XX', 3066, 9220),
    ('2024-11-10 19:30:57', 'dTF02CdV', 6572, 6830),
    ('2024-11-10 19:30:57', 'jUssSnrE', 2377, 2266),
    ('2024-11-10 19:30:57', 'wvpgvvus', 6572, 9684),
    ('2024-11-10 19:30:57', 'DtHAT7gr', 3635, 9220),
    ('2024-11-10 19:30:57', 'oMF6W1pJ', 4145, 7876),
    ('2024-11-10 19:30:57', 'DtHAT7gr', 8345, 3039);
INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount, Date_of_journey, Quantity,userid)
VALUES
    (17541, NULL, 3039, 748, '2011-04-28', 1,2377),
    (41319, 8916, NULL, 219, '2005-01-07', 1,2377),
    (36816, NULL, 9684, 1482, '2004-10-16', 2,5545),
    (48365, 8916, NULL, 1095, '2020-01-13', 5,6572),
    (23461, NULL, 9220, 1956, '2009-04-24', 4,2377),
    (15140, 1828, NULL, 126, '1996-01-07', 2,8345),
    (40312, NULL, 7876, 978, '2017-02-18', 2,4145),
    (74169, 8436, NULL, 983, '1982-10-21', 1,3635),
    (27476, NULL, 2266, 4915, '1982-06-28', 5,8345),
    (81615, 1580, NULL, 404, '2013-01-20', 2,6572);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (4002, 'Ryanport', 8460);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (7072, 'Salasside', 2921);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (5871, 'Whiteville', 8835);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (1478, 'East Jason', 2528);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (5490, 'North Mistytown', 4950);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (1691, 'West Carolberg', 1875);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (7295, 'Riveratown', 4553);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (9032, 'Peggyfurt', 9609);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (7467, 'Lake Dianaville', 5326);
INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (7777, 'East Nicholasbury', 4860);
INSERT INTO Hotel_Invoice (Date_of_entering, Hotel_id, Userid) VALUES
('2010-09-04', 1478, 2377),
('2003-01-16', 1691, 3066),
('1986-09-23', 4002, 4145),
('2016-12-09', 5490, 5545),
('2017-04-30', 5871, 8345),
('2001-10-09', 7072, 8895),
('1978-08-22', 7295, 2562),
('2005-02-10', 7467, 3635),
('1999-07-02', 7777, 6572),
('2017-07-25', 9032, 9080);
INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) VALUES
(1, 9080, 48365, '1', NULL, '2022-03-20 03:27:41'),
(2, 3066, NULL, '0', 7777, '2024-01-24 05:46:17'),
(3, 4145, 41319, '0', 7295, '2023-04-02 15:16:50'),
(4, 8895, 27476, '0', NULL, '2022-09-26 01:41:56'),
(5, 2562, NULL, '1', 1691, '2024-01-18 06:19:40'),
(6, 3635, 17541, '1', 1691, '2022-07-21 20:15:04'),
(7, 5545, 74169, '1', NULL, '2022-10-25 05:13:17'),
(8, 3066, NULL, '1', 1478, '2023-09-27 10:41:38'),
(9, 5545, 81615, '0', 5490, '2023-04-26 13:06:40'),
(10, 4145, 27476, '1', NULL, '2023-11-18 15:26:19');
INSERT INTO HolidayPackage (Package_id, Hotel_id, Start_date, flight_No,End_Date,Price) VALUES
(2180, 4002, '2024-11-19 11:29:36', 9811, '2025-02-14 14:14:06', 671),
(2129, 1691, '2023-07-24 20:30:09', 9220, '2024-10-13 10:18:02', 440),
(5187, 7072, '2023-02-26 00:48:21', 3039, '2025-07-16 23:13:56', 940),
(9164, 1691, '2024-12-13 08:19:57', 2266, '2024-12-25 05:19:02', 584),
(8409, 1478, '2024-11-05 14:41:18', 7876, '2024-12-03 20:21:26', 954),
(7343, 7467, '2024-01-27 00:19:23', 5911, '2024-08-12 03:07:30', 475),
(9074, 1691, '2023-08-19 04:44:05', 8991, '2023-10-21 17:38:40', 105),
(9289, 1478, '2023-04-17 21:50:22', 9220, '2023-05-10 07:15:45', 353),
(2187, 5490, '2023-04-17 03:00:24', 6830, '2025-08-09 18:52:24', 306),
(6271, 5490, '2024-11-04 20:29:38', 9684, '2025-03-21 01:21:39', 145);
INSERT INTO Holiday_Pay (Payment_Id,Package_id) VALUES
(6, 9164),
(9, 5187),
(3, 7343);