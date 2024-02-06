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
    userid INT AUTO_INCREMENT PRIMARY KEY,
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
