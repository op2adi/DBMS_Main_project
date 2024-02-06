DROP DATABASE if EXISTS makemytrip;
CREATE DATABASE makemytrip;
show DATABASES ;
use makemytrip;
CREATE TABLE Gender_Ref
(   gender CHAR(1) NOT NULL,
    PRIMARY KEY (gender)
) ENGINE = InnoDB ;

INSERT INTO Gender_Ref (gender)
    VALUES
        ('F'), ('M')  ;


CREATE TABLE Users (
    userid INT  PRIMARY KEY,
    email VARCHAR(80) NOT NULL UNIQUE CHECK (email REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'),
    name VARCHAR(25) NOT NULL,
    phnumber CHAR(10) NOT NULL UNIQUE CHECK (phnumber REGEXP '^[0-9]{10}$'),
    gender CHAR(1) NOT NULL,
    Address_hno VARCHAR(5) NOT NULL,
    City VARCHAR(30) NOT NULL,
    Pincode CHAR(6) NOT NULL CHECK (Pincode REGEXP '^[0-9]{6}$'),
    dob DATE NOT NULL,
    age INT, -- we will calculate later when need it is an attribute and nhi bhi marzi hai mtlb lena chahoto le lo wrna mtlo
    FOREIGN KEY (gender)
        REFERENCES Gender_Ref(gender)
);

CREATE TABLE Complaint (
    complaint_id INT  PRIMARY KEY,
    user_id INT NOT NULL,
    complaint_description TEXT NOT NULL,
    filed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(userid)
);

CREATE TABLE Loungue(
    Offers_code CHAR(10) PRIMARY KEY,
    Credit_Card Varchar(30) ,
    Timings DATETIME NOT NULL ,
    Place VARCHAR(60) NOT NULL
#     Price INT NOT NULL , -- we wil simply provide price also incase no credit cards is available remember offercode is mandate but credit card is optional doubt
);

create table Booked_Loungue (
    -- this is for relationship
    Date_on Datetime NOT NULL,
    Offers_code char(10) NOT NULL ,
    userid INT NOT NULL ,
    Flight_No INT Not NULL, # Need to give foreign key for flight number
    FOREIGN KEY (userid) REFERENCES Users(userid)
);

create table Transport(
    -- this is a disjoint set @Adi Bhai coding
    Transport_id INT PRIMARY KEY,
    Start_Loc VARCHAR(50) NOT NULL,
    Destn_Loc VARCHAR(50) NOT NULL ,
    Timings TIMESTAMP NOT NULL,
    Price INT NOT NULL,
    Vacany Int DEFAULT 100
);

create table Trains(
    Train_No INT PRIMARY KEY ,
    Transport_Id INT NOT NULL ,
    Name Varchar(100) NOT NULL ,
    FOREIGN KEY (Transport_Id) REFERENCES Transport(Transport_id)
);

create table Flight(
    Flight_No INT PRIMARY KEY ,
    Transport_Id INT NOT NULL ,
    Name VARCHAR(50) NOT NULL
);

create TABLE Tickets(
    Ticket_No INT PRIMARY KEY ,
    Train_No INT Not NULL ,
    Flight_No INT NOT NULL ,
    Amount INT NOT NULL ,
    Date_of_journey DATETIME NOT NULL ,
    Quantity INT Not NULL ,
    Foreign Key (Train_No) references Trains(Train_No),
    FOREIGN KEY (Flight_No) REFERENCES Flight(Flight_No),
    CHECK ( Quantity > 0 )
);

Create table Hotels (
    Hotel_id int PRIMARY KEY ,
    Location VARCHAR(50) NOT NULL ,
    Pricing Int NOT NULL ,
    Vacancy INT NOT NULL DEFAULT 100
);

create table Hotel_Invouice(
    Date_of_entering DATE NOT NULL ,
    Hote_Id Int NOT NULL ,
    Userid INT Not Null ,
    FOREIGN KEY (Hote_Id) references Hotels(Hotel_id),
    FOREIGN KEY (Userid) references Users(userid)
);