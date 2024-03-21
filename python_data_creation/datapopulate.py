# uses random gtgo generate values

import os
import random
import string
from datetime import datetime, timedelta

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
        # exit(0)

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
        # cursor.execute("Select userid from userds_passwords")
        

        # Enter data
        for record in data:
            # Generate unique userid
            userid = generate_unique_userid(existing_userids)
            sql2 = "INSERT INTO userids_passwords (userid,password,is_locked) Values (%s,%s,%s)"

            # Insert data into the table
            sql = "INSERT INTO Users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for i in range(8))
            # return password
            # password = 
            val = (userid,) + record
            va2 = (userid,)+(password,"F")
            try:
                print(sql2,va2)
                cursor.execute(sql2,va2)
            except :
                print(Exception)
                continue
            # print(val)
            adi_con.commit()
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
            print(f"INSERT INTO Complaint (complaint_id, user_id, complaint_description) VALUES ({record[0]}, {record[1]}, {str(record[2])})"+";")
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
    timings = random_date(datetime(2024, 1, 1), datetime.now())
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
    ghjkl = fetch_user_ids()
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
        # print(ghjkl)
        dfg = random.choice(ghjkl)
        
        amt = int(cursor.fetchone()[0])*qwe
        l+=(amt,random_date(datetime(2023, 1, 1), datetime(2024, 12, 31)),qwe,dfg)
        query = "INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount,Date_of_journey,Quantity,userid) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        # print(f"INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount,Date_of_journey,Quantity) VALUES {l[0], l[1], l[2], l[3], l[4], l[5]}")
        
        cursor.execute(query,l)
        print(f"INSERT INTO Tickets (Ticket_No, Train_No, Flight_No, Amount,Date_of_journey,Quantity,userid) VALUES {l[0], l[1], l[2], l[3], l[4], l[5],l[6]}"+";")
        
def hotel_Add():
    fake = Faker()
    hotel_id = []
    a = 0
    query = "INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES (%s, %s, %s)"
    for i in range(10):
        while True:
            a = random.randint(1000,9999)
            if a in hotel_id:
                continue
            hotel_id.append(a)
            break
        loc =  fake.city()
        pr = random.randint(1000,10000)
        t = (a,loc,pr)
        try:
            cursor.execute(query,t)
            adi_con.commit()
        except:
            print("HUHUU")
        print(f"INSERT INTO Hotels (Hotel_id, Location, Pricing) VALUES {a, loc, pr}"+";")
def fech_hotel_id():
    cursor.execute("Select Hotel_Id from Hotels")
    return [row[0] for row in cursor.fetchall()]
def hotlel_invoice():
    fake = Faker()
    hotel_id = fech_hotel_id()
    u_id = fetch_user_ids()
    query = "INSERT INTO Hotel_Invoice (Date_of_entering, Hotel_id, Userid) VALUES (%s, %s, %s)"
    tup = []
    for i in range(len(hotel_id)):
        k = u_id[i]
        e = fake.date()
        sm = (e,hotel_id[i],u_id[i])
        cursor.execute(query,(e,hotel_id[i],u_id[i]))
        adi_con.commit()
        tup.append(sm)
    print("INSERT INTO Hotel_Invoice (Date_of_entering, Hotel_id, Userid) VALUES")
    for i in tup[:len(tup)-1:]:
        print(i,end = ",")
        print()
    print(tup[-1],end = ";")
def random_date(start, end):
    current_datetime = datetime.now()
    start_date = current_datetime + timedelta(days=1)  # Ensure start date is in the future
    end_date = start_date + timedelta(days=random.randint(1, 365))  # Adjust range as needed
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))


# Function to generate random Payment_Status
def random_payment_status():
    return random.choice(['0', '1'])
def fetch_ticket_ids():
    cursor.execute("Select ticket_No from tickets")
    return [row[0] for row in cursor.fetchall()]
def payments():
    user_ids= fetch_user_ids()
    ticket_ids= fetch_ticket_ids()
    hotel_ids= fech_hotel_id()
    query = "INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) VALUES (%s, %s, %s, %s, %s, %s)"
    tmp = 0
    lol = []
    for i in range(10):
        payment_id = i + 1
        user_id = random.choice(user_ids)
        ticket_id = random.choice(ticket_ids)
        hotel_id = random.choice(hotel_ids)
        if tmp%3==0:
            hotel_id=None
            tmp+=1
        elif tmp%3==1:
            ticket_id = None
            tmp+=1
        else:
            tmp+=1
        payment_status = random_payment_status()
        date_of_payment = random_date(datetime(2024, 1, 1), datetime.now())
        payt = (payment_id, user_id, ticket_id, payment_status, hotel_id, date_of_payment.strftime('%Y-%m-%d %H:%M:%S'))
        cursor.execute(query,payt)
        adi_con.commit()
        lol.append(payt)
        # print(f"INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) "
        #     f"VALUES ({payment_id}, {user_id}, {ticket_id}, '{payment_status}', {hotel_id}, '{date_of_payment.strftime('%Y-%m-%d %H:%M:%S')}');")
    print("INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) VALUES ")
    for i in lol[:-1]:
        print(i,end=",")
        print()
    print(lol[-1],end=";")

def holiay_package():
    hotel_ids = fech_hotel_id()
    # ticket_no = fetch_ticket_ids()
    flight_add = fetch_flight_number()
    pa = []
    for i in range(10):
        package_id = random.randint(1000,10000)
        hotel_id = random.choice(hotel_ids)
        flight = random.choice(flight_add)
        # ticket = random.choice(ticket_no)
        price = random.randint(100,1000)
        start_date = random_date(datetime(2023, 1, 1), datetime(2024, 12, 31))
        end_date = random_date(start_date, datetime(2025, 12, 31))
        op = [package_id, hotel_id, start_date,flight, end_date, price]
        pa.append(op)
        # Inserting record into the database
        cursor.execute("INSERT INTO HolidayPackage (Package_id, Hotel_id, Start_date, flight_No,End_Date,Price) VALUES (%s, %s, %s, %s,%s,%s)",
                    (package_id, hotel_id, start_date,flight, end_date, price))
        adi_con.commit()
    print("INSERT INTO HolidayPackage (Package_id, Hotel_id, Start_date, flight_No,End_Date,Price) VALUES ")
    for i in pa[:-1:]:
        for j in range(len(i)):
            if type(i[j])==datetime:
                i[j]= str(i[j].strftime("%Y-%m-%d %H:%M:%S"))
        print(tuple(i),end=",")
        print()
    for i in range(len(pa[-1])):
        if type(pa[-1][i])==datetime:
            pa[-1][i]= str(pa[-1][i].strftime("%Y-%m-%d %H:%M:%S"))
    print(tuple(pa[-1]),end=";")

def fetch_packagge_id():
    cursor.execute("SELECT package_id from holidaypackage")
    return [row[0] for row in cursor.fetchall()]
def fetch_payment_id(spl_needed = False):
    if spl_needed == True:
        cursor.execute("SELECT payment_id from payments where Ticket_id is not NULL and hotel_id is not NULL and payment_status is not NULL")
        return [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT payment_id from payments")
    return [row[0] for row in cursor.fetchall()]
def holiday_pay():
    k = fetch_packagge_id()
    q = fetch_payment_id(True)
    query = "INSERT INTO Holiday_Pay (Payment_Id,Package_id) VALUES (%s,%s)"
    pop =[]
    # print(k)
    for i in range(min(len(k),len(q))):
        l = (q[i], k[i])
        # print(l)
        cursor.execute(query,l)
        pop.append(l)
    print("INSERT INTO Holiday_Pay (Payment_Id,Package_id) VALUES ")
    for i in pop[:-1]:
        print(i,end = ",")
        print()
    print(pop[-1],end=";")
    adi_con.commit()
if __name__ == '__main__':
    clear_all_tables()
    adding_for_users()
    add_complaints()
    Lounge_data()
    transport_data()
    transid = fetch_transport_data()
    train_Add()
    Flight_Add()
    bookerd_Loungue()
    Tickets_add()
    hotel_Add()
    hotlel_invoice()
    payments()
    holiay_package()
    holiday_pay()