import random
import time
# # Create a new user
# user = User.objects.create_user(username='example_user', password='example_password')
from datetime import datetime

import mysql.connector


def calculate_age(date_of_birth):
    # Get the current date
    current_date = datetime.now().date()
    
    # Calculate the difference in years between the current date and the date of birth
    age = current_date.year - date_of_birth.year - ((current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day))
    
    return age

def mysql_bckens():
    connection = mysql.connector.connect(
        host='localhost', # host mt hi chedo chl jayega
        user='root', # user dalo
        password='Aditya@1998', # password dalo me bdl dung anhi batunga
        database='makemytrip' # optional hai comment bhi kr skte ho phir password me se , bhi remove krna 
    )
    if connection.is_connected():
        print("YES")
    else:
        print("NO"*100)

    # Create cursor
    # cursor = connection.cursor()

    return connection


adi_conn1 = mysql_bckens()
adi_conn = adi_conn1.cursor()

# Query 1 if we want to see or all female users

adi_conn.execute("Select count(*) from users where Gender = (%s) group by Gender",('F',))

k = adi_conn.fetchall()

for i in k:
    print("Total female users are", i[0])

# Query 2 if we want to see which of our current users have ever booked any hotel

adi_conn.execute("SELECT name FROM users WHERE userid IN (SELECT DISTINCT userid FROM hotel_invoice)")


k = adi_conn.fetchall()
for i in k:
    print(i[0])
    
# Query 3  Here i printed those unique users whose payment has succes that means they have booked from our application
adi_conn.execute("Select Distinct user_id from payments where payment_status = (%s)",(1,))
k = adi_conn.fetchall()
for i in k:
    print(i[0])
