# uses random gtgo generate values

import os
import random
import string

import mysql.connector
from faker import Faker

transid = []
# global declaratoiom for this 
# print(os.environ.get("DB_PASSWORD"))
# adi_con = ''
def connect(print_result=False):
    # global adi_con
    adi_con = mysql.connector.connect(host="localhost", user="root",
                                      passwd="Aditya@1998")  # here i connected it to my database dont forget to enter your password and uname phir kehte hai ki placemnent nhi lgti
    if print_result:
        print(adi_con.is_connected())
    return adi_con


adi_con = connect()  # you can set it to true

# main cursor from which query will be executed and value added
cursor = adi_con.cursor()  # cursor to execute queries global declaration


def execute(query):  # for execution of queries
    cursor.execute(query)
    return


execute("use makemytrip")  # temp execution


# first clear all tables
def clear_all_tables():
    try:
        # Get a list of all tables in the database
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(tables)
        # Loop through each table and delete all records
        for table in tables:
            table_name = table[0]
            print(table_name)
            if table_name != "gender_ref":
                cursor.execute(f"DELETE FROM {table_name}")
                print(f"DELETE FROM {table_name};")
                adi_con.commit()
                # print(f"All records cleared from table {table_name} successfully!")

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
        phnumber = fake.random_number(digits=10)
        while len(str(phnumber)) != 10:
            phnumber = fake.random_number(digits=10)
        # print(phnumber)
        gender = random.choice(['M', 'F'])
        Address_hno = fake.building_number()
        City = fake.city()
        Pincode = fake.random_number(digits=6)
        while len(str(Pincode)) != 6:
            Pincode = fake.random_number(digits=6)
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
            # print(sql,val+";")
            print(f"INSERT INTO Users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES"+f" ({userid}, {record[0]}, {record[1]}, {record[2]}, {record[3]}, {record[4]}, {record[5]}, {record[6]}, {record[7]} )"+";")
            adi_con.commit()

            # print("Record inserted successfully!")
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
            cursor.execute("INSERT INTO Complaint (complaint_id, user_id, complaint_description) VALUES (%s, %s, %s)",
            record)
            print(f"INSERT INTO Complaint (complaint_id, user_id, complaint_description) VALUES ({record[0]}, {record[1]}, {record[2]})"+";")
            adi_con.commit()
            # print("Record inserted successfully!")
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
def fetch_offer_code():
    offer_codes = []
    try:
        cursor.execute("SELECT Offers_code FROM loungue")
        offer_codes = [row[0] for row in cursor.fetchall()]
    except mysql.connector.Error as err:
        print("Error:", err)
    return offer_codes


def generate_fake_data_for_loungue(num_records):
    fake = Faker()
    data = []
    for _ in range(num_records):
        offer_code = generate_offer_code()
        credit_card = fake.random_element(
            elements=('HDFC Bank', 'ICICI Bank', 'State Bank of India', 'Axis Bank', 'Kotak Mahindra Bank'))
        timings = fake.date_time()
        place = fake.address()
        data.append((offer_code, credit_card, timings, place))
    return data


def enter_data_for_loungue(data):
    try:
        for record in data:
            cursor.execute("INSERT INTO Loungue (Offers_code, Credit_Card, Timings, Place) VALUES (%s, %s, %s, %s)",
                           record)
            adi_con.commit()
            print(f"INSERT INTO Loungue (Offers_code, Credit_Card, Timings, Place) VALUES ({record[0]}, {record[1]}, {record[2]}, {record[3]});")
            # print("Record inserted successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)


def Lounge_data():
    num_records = 10
    data = generate_fake_data_for_loungue(num_records)

    # Call the function to enter data
    enter_data_for_loungue(data)
    


def generate_transport_data():
    fake = Faker()
    k = 0
    while True:
        k = random.randint(1000000,10000000)
        if k not in transid:
            transid.append(k)
            break

    # flight_no = random.randint(1000,9999)
    start_loc = fake.city()
    destn_loc = fake.city()
    while start_loc == destn_loc:
        destn_loc = fake.city()
    timings = fake.date_time_between(start_date='-1y', end_date='+1y')
    price = random.randint(10, 1000)
    return (k,start_loc, destn_loc, timings, price,100)  # Set destination to original start location

def transport_data():
    for i in range(10):
        transport_data = generate_transport_data()
        transport_data = list(transport_data)
        insert_query = "INSERT INTO Transport (Transport_id, Start_Loc, Destn_Loc, Timings, Price, Vacany) VALUES (%s,%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, transport_data)
        adi_con.commit()
        print(f"INSERT INTO Transport (Transport_id, Start_Loc, Destn_Loc, Timings, Price, Vacany) VALUES {transport_data[0], transport_data[1], transport_data[2], transport_data[3], transport_data[4],transport_data[5]}"+";")
        while transport_data[0] in transid:
            transport_data[0]+=1
        transid.append(transport_data[0])
        transport_data[1],transport_data[2]=transport_data[2],transport_data[1]
        cursor.execute(insert_query, transport_data)
        adi_con.commit()
        print(f"INSERT INTO Transport (Transport_id, Start_Loc, Destn_Loc, Timings, Price, Vacany) VALUES {transport_data[0], transport_data[1], transport_data[2], transport_data[3], transport_data[4],transport_data[5]}"+";")


def fetch_transport_data():
    cursor.execute("SELECT Transport_id FROM Transport")  
    transport_ids = [row[0] for row in cursor.fetchall()]
    return transport_ids

def generate_train_data(transport_ids):
    trains = []
    for i in range(10):
        train_no = random.randint(1000, 9999)
        transport_id = random.choice(transport_ids)
        trains.append((train_no, transport_id))
        transport_ids.remove(transport_id)  # Remove the used transport ID to
        # ensure it's not used for flights
        # print(transport_ids)
    return trains

# Function to generate flight data
def generate_flight_data(transport_ids):
    flights = []
    for i in range(10):
        flight_no = random.randint(1000, 9999)
        transport_id = random.choice(transport_ids)
        flights.append((flight_no, transport_id))
        transport_ids.remove(transport_id)  # Remove the used transport ID to ensure it's not used for trains
        # print(transport_ids)
    return flights
def train_Add():
    fg = Faker()
    # print(transid)
    adi_badi = generate_train_data(transid)
    for i in range(10):
        word_length = random.randint(10, 20)  # Random length for each word
        word = ''.join(random.choices(string.ascii_uppercase, k=word_length))
        adi_badi[i]+=(word,)
    query = "INSERT INTO Trains (Train_No, Transport_Id, Name) VALUES (%s,%s, %s)"
    for i in adi_badi:
        cursor.execute(query,i)
        adi_con.commit()
        print(f'INSERT INTO Trains (Train_No, Transport_Id, Name) VALUES {i[0], i[1], i[2]}'+";")
    # print(t)
    # print(adi_badi)
def Flight_Add():
    # transid = fetch_transport_data()
    print(transid)
    adi_badi = generate_flight_data(transid)
    for i in range(len(adi_badi)):
        word_length = random.randint(10, 20)  # Random length for each word
        word = ''.join(random.choices(string.ascii_uppercase, k=word_length))
        adi_badi[i]+=(word,)
    query = "INSERT INTO flight (Flight_No, Transport_Id, Name) VALUES (%s,%s, %s)"
    for i in adi_badi:
        cursor.execute(query,i)
        adi_con.commit()
        print(f'INSERT INTO flight (flight_No, Transport_Id, Name) VALUES {i[0], i[1], i[2]}'+";")
    
def fetch_flight_number():
    cursor.execute("SELECT flight_No FROM flight")
    transport_ids = [row[0] for row in cursor.fetchall()]
    return transport_ids

def bookerd_Loungue():
    fake = Faker()
    userids = fetch_user_ids()
    offer = fetch_offer_code()
    fl = fetch_flight_number()
    query = "INSERT INTO  booked_loungue (Date_on, Offers_code, userid, Flight_No) VALUES (%s, %s, %s, %s)"
    for i in range(10):
        k=('2024-11-10 19:30:57',)+((random.choice(offer),))+(random.choice(userids),)+(random.choice(fl),)
        # print(k)
        cursor.execute(query, k)
        print(f"INSERT INTO  booked_loungue (Date_on, Offers_code, userid, Flight_No) VALUES {k[0], k[1],k[2],k[3]}"+";")

def fetch_train_no():
    cursor.execute("SELECT train_No FROM Trains")
    transport_ids = [row[0] for row in cursor.fetchall()]
    return transport_ids

def Tickets_add():
    fg = 0
    fake = Faker()
    q = fetch_train_no()
    r = fetch_flight_number()
    for i in range(10):
        k = random.randint(999,99999)
        l=(k,)
        if fg:
            l+=(random.choice(q),)
            l+=(None,)
        else:
            l+=(None,)
            l+=(random.choice(r),)
        qwe = random.randint(1,5)
        if fg:
            cursor.execute(f"Select Price from transport , Trains where Trains.Train_No={l[1]} && Trains.Transport_id=Transport.Transport_id")
            fg = 0
        else:
            # print(l[2])
            cursor.execute(f"Select Price from transport , flight where flight.flight_No={l[2]} && flight.Transport_id=Transport.Transport_id")
            fg = 1
            # print(cursor.fetchall())
        amt = int(cursor.fetchone()[0])*qwe
        l+=(amt,fake.date(),qwe)
        query = "INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount,Date_of_journey,Quantity) VALUES (%s, %s, %s, %s,%s,%s)"
        # print(f"INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount,Date_of_journey,Quantity) VALUES {l[0], l[1], l[2], l[3], l[4], l[5]}")
        
        cursor.execute(query,l)
        print(f"INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount,Date_of_journey,Quantity) VALUES {l[0], l[1], l[2], l[3], l[4], l[5]}"+";")
        
        
        
if __name__ == '__main__':
    # clear_all_tables()
    # adding_for_users()
    # add_complaints()
    # Lounge_data()
    # transport_data()
    transid = fetch_transport_data()
    # train_Add()
    # Flight_Add()
    bookerd_Loungue()
    Tickets_add()