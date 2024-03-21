import random
import time

import mysql.connector
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# # Create a new user
# user = User.objects.create_user(username='example_user', password='example_password')


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
# Create your views here.
# views.py
def fetch_users():
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()
    
    cursor = adi_conn.execute("SELECT * FROM userids_passwords")
    users = cursor.fetchall()  # Fetch all rows from the cursor
    return users

def authenticate1(request, username, password):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()

    # Select user based on username and password
    adi_conn.execute("SELECT * FROM userids_passwords WHERE userid=%s AND password=%s AND is_locked = %s" , (username, password,'F'))
    user = adi_conn.fetchone()  # Fetch the first matching row

    if user:
        # Reset the number of tries to 0
        adi_conn.execute("UPDATE userids_passwords SET tries = 0 WHERE userid = %s", (username,))

        return True
    else:
        # Get the current number of tries for the user
        adi_conn.execute("SELECT tries FROM userids_passwords WHERE userid=%s", (username,))
        r = adi_conn.fetchone()
        print(r)
        if r is None:
            return False
        tries = r[0]

        # Increment the number of tries by 1
        tries += 1

        # Check if the number of tries exceeds 2
        # if tries >= 3:
        #     # Set tries to 0 and is_locked to 'T', and record the attempt time
        #     adi_conn.execute("UPDATE userids_passwords SET tries = 0, is_locked = 'T', attempt_time = %s WHERE userid = %s", (time.strftime('%Y-%m-%d %H:%M:%S'), username))
        #     adi_conn1.commit()
        if 1==1:
            # Update the number of tries for the user
            adi_conn.execute("UPDATE userids_passwords SET tries = %s WHERE userid = %s", (tries, username))
            adi_conn1.commit()
            print("HULA")

        return False

def create_user(username, password):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()
    
    # Check if the username already exists in the database
    adi_conn.execute("SELECT * FROM userids_passwords WHERE userid = %s", (username,))
    existing_user = adi_conn.fetchone()
    
    if existing_user:
        return False  # Username already exists
    else:
        # Insert the new user into the database
        adi_conn.execute("INSERT INTO userids_passwords (userid, passwords,is_locked) VALUES (%s, %s,%s)", (username, password,"F"))
        adi_conn1.commit()
        return True  # User created successfully

def login_view(request):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        query = "Insert Into log_entry (userid,is_success) Values (%s,%s)"
        user = authenticate1(request, username=username, password=password)
        if user:
            # login(request, user)
            adi_conn.execute(query,(username,1))
            adi_conn1.commit()
            return render(request,'home.html')  # Redirect to home page after successful login
        else:
            adi_conn.execute(query,(username,0))
            adi_conn1.commit()
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
def create_account(request):
    if request.method == 'POST':
        # print("111111111111111111111111")
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phonenumber')
        Gender = request.POST.get('gender')
        House_Number = request.POST.get('House_Number')
        City = request.POST.get('City')
        Dob = request.POST.get('DOB')
        pincode = request.POST.get('pin')
        name = request.POST.get('name')
        print(email, password, phone_number,Gender,House_Number,City,Dob,pincode)
        adi_conn1 = mysql_bckens()
        adi_conn = adi_conn1.cursor()
        query = "Select phnumber from users"
        adi_conn.execute(query)
        d = adi_conn.fetchall()
        print(d)
        for i in d:
            for j in i:
                print(str(j),str(phone_number),str(j)==str(phone_number))
                if str(j) == str(phone_number):
                    alert_message = "Phone number already registered!"
                    return render(request, 'create_account.html', {'alert_message': alert_message})
        adi_conn.execute("select userid from users")
        d = adi_conn.fetchall()
        # d = [str(x) for x in i]
        userids = []
        for i in d:
            for j in i:
                userids.append(str(j))
        userid = random.randint(10,9999)
        while userid in d:
            userid = random.randint(10,9999)
        print(userid)
        # adi_conn.execute("select userid from users")
        # d = adi_conn.fetchall()
        if Gender == "male":
            Gender = "M"
        else:
            Gender = "F"
        query = "INSERT INTO users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        print(query,(userid,email, name,phone_number,Gender,House_Number,City,pincode,Dob))
        adi_conn.execute(query,(userid,email, name,phone_number,Gender,House_Number,City,pincode,Dob))
        query = "Insert into userids_passwords (userid,password,is_locked) Value (%s, %s, %s)"
        adi_conn.execute(query,(userid,password,"F"))
        print(query,(userid,password,"F"))
        # adi_conn.execut("")
        adi_conn1.commit()
        
                    # return render(request, 'create_account.html')
        return render(request, 'home.html')
    # print("JIJO")
    return render(request, 'create_account.html')



def Flights(request):
    return render(request, 'Flights.html')