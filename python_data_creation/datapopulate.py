# uses random gtgo generate values

import os
import random
import string

import mysql.connector
from faker import Faker


# print(os.environ.get("DB_PASSWORD"))
# adi_con = ''
def connect(print_result=False):
    # global adi_con
    adi_con = mysql.connector.connect(host = "localhost", user = "root",passwd = "Aditya@1998") # here i connected it to my database dont forget to enter your password and uname phir kehte hai ki placemnent nhi lgti
    if print_result:
        print(adi_con.is_connected())
    return adi_con

adi_con = connect() # you can set it to true 

#main cursor from which query will be executed and value added
cursor = adi_con.cursor() # cursor to execute queries global declaration

def execute(query): # for execution of queries
    cursor.execute(query)
    return


execute("use makemytrip") #temp execution 

# first clear all tables
def clear_all_tables():
    try:
        # Get a list of all tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()

        # Loop through each table and delete all records
        for table in tables:
            table_name = table[0]
            if table_name!="gender_ref":
                cursor.execute(f"DELETE FROM {table_name}")
                adi_con.commit()
                print(f"All records cleared from table {table_name} successfully!")

    except mysql.connector.Error as err:
        print("Error:", err)


# for users table
def generate_unique_userid(existing_userids):
    while True:
        userid = random.randint(1000, 9999)
        if userid not in existing_userids:
            return userid

def generate_fake_data_for_users(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        email = fake.email()
        name = fake.name()
        phnumber = fake.random_number(digits = 10)
        while len(str(phnumber))!=10:
            phnumber = fake.random_number(digits = 10)
        # print(phnumber)
        gender = random.choice(['M', 'F'])
        Address_hno = fake.building_number()
        City = fake.city()
        Pincode = fake.random_number(digits =6)
        while len(str(Pincode))!=6:
            Pincode = fake.random_number(digits =6)
        dob = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
        data.append((email, name, phnumber, gender, Address_hno, City, Pincode, dob))
    return data

def enter_temp_data_for_users(data):
    try:
        # Check for existing userids
        cursor.execute("SELECT userid FROM users")
        existing_userids = set(row[0] for row in cursor.fetchall())

        # Enter data
        for record in data:
            # Generate unique userid
            userid = generate_unique_userid(existing_userids)

            # Insert data into the table
            sql = "INSERT INTO Users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (userid,) + record
            # print(val)
            cursor.execute(sql, val)
            adi_con.commit()

            print("Record inserted successfully!")
            existing_userids.add(userid)

    except mysql.connector.Error as err:
        print("Error:", err)


def adding_for_users():
    # Generate fake data
    num_records = 10
    data = generate_fake_data_for_users(num_records)

    # Call the function to enter temporary data
    enter_temp_data_for_users(data)


# for complaint table user must be run to run this
def generate_unique_complaint_id(existing_ids):
    while True:
        complaint_id = random.randint(1000, 9999)
        if complaint_id not in existing_ids:
            return complaint_id

def fetch_user_ids():
    user_ids = []
    try:
        cursor.execute("SELECT userid FROM Users")
        user_ids = [row[0] for row in cursor.fetchall()]
    except mysql.connector.Error as err:
        print("Error:", err)
    return user_ids

def generate_fake_complaint_data(num_complaints, user_ids):
    fake = Faker()
    data = []
    for _ in range(num_complaints):
        complaint_id = generate_unique_complaint_id(data)
        user_id = random.choice(user_ids)
        description = fake.paragraph(nb_sentences=5, variable_nb_sentences=True)
        data.append((complaint_id, user_id, description))
    return data

def enter_complaint_data(data):
    try:
        for record in data:
            cursor.execute("INSERT INTO Complaint (complaint_id, user_id, complaint_description) VALUES (%s, %s, %s)", record)
            adi_con.commit()
            print("Record inserted successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)
def add_complaints():
    # Fetch user IDs from the Users table
    user_ids = fetch_user_ids()

    # Generate fake complaint data
    num_complaints = 10
    data = generate_fake_complaint_data(num_complaints, user_ids)
    enter_complaint_data(data)


# for Loungue
def generate_offer_code():
    offer_code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return offer_code

def generate_fake_data_for_loungue(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        offer_code = generate_offer_code()
        credit_card = fake.random_element(elements=('HDFC Bank', 'ICICI Bank', 'State Bank of India', 'Axis Bank', 'Kotak Mahindra Bank'))
        timings = fake.date_time()
        place = fake.address()
        data.append((offer_code, credit_card, timings, place))
    return data

def enter_data_for_loungue(data):
    try:
        for record in data:
            cursor.execute("INSERT INTO Loungue (Offers_code, Credit_Card, Timings, Place) VALUES (%s, %s, %s, %s)", record)
            adi_con.commit()
            print("Record inserted successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)

def Lounge_data():
    num_records = 10
    data = generate_fake_data_for_loungue(num_records)

    # Call the function to enter data
    enter_data_for_loungue(data)

if __name__ == '__main__':
    clear_all_tables()
    adding_for_users()
    add_complaints()
    Lounge_data()