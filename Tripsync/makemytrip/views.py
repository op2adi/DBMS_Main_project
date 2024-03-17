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
        if tries >= 3:
            # Set tries to 0 and is_locked to 'T', and record the attempt time
            adi_conn.execute("UPDATE userids_passwords SET tries = 0, is_locked = 'T', attempt_time = %s WHERE userid = %s", (time.strftime('%Y-%m-%d %H:%M:%S'), username))
            adi_conn1.commit()
        else:
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate1(request, username=username, password=password)
        if user:
            # login(request, user)
            return render(request,'home.html')  # Redirect to home page after successful login
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
