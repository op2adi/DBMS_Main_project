import random
import time
# # Create a new user
# user = User.objects.create_user(username='example_user', password='example_password')
from datetime import datetime

import mysql.connector
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# views.py
from django.shortcuts import redirect, render


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
# Create your views here.
# views.py
class user_cls:
    def __init__(self, userid):
        userid = userid
    def user_id(self):
        return self.userid
    def userid_set(self,userid):
        self.userid = userid
    def all_details(self):
        adi_conn1 = mysql_bckens()
        adi_conn = adi_conn1.cursor()
        print(self.userid)
        k = int(self.userid)
        # print(k,type(k))
        adi_conn.execute("SELECT * FROM users where userid = %s",(k,))
        c = adi_conn.fetchall()
        # pop = [x for x in c if x[0]==k]
        return c


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
    global usrer_info
    usrer_info = user_cls(00000)
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
            usrer_info.userid_set(username)
            return render(request,'home.html')  # Redirect to home page after successful login
        else:
            adi_conn.execute(query,(username,0))
            adi_conn1.commit()
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
def create_account(request):
    global usrer_info
    usrer_info = user_cls(00000)
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
        query = "Select phnumber,email from users"
        adi_conn.execute(query)
        d = adi_conn.fetchall()
        print(d)
        for i in d:
            for j in i:
                print(str(j),str(phone_number),str(j)==str(phone_number))
                if str(j) == str(phone_number):
                    alert_message = "Phone number already registered!"
                    return render(request, 'create_account.html', {'alert_message': alert_message})
                if str(j) == str(email):
                    alert_message = "Email already registered!"
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
        usrer_info.userid_set(userid)
        # adi_conn.execute("select userid from users")
        # d = adi_conn.fetchall()
        if Gender == "male":
            Gender = "M"
        else:
            Gender = "F"
        query = "INSERT INTO users (userid, email, name, phnumber, gender, Address_hno, City, Pincode, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        query2 = "Insert into userids_passwords (userid,password,is_locked) Value (%s, %s, %s)"
        adi_conn.execute(query2,(userid,password,"F"))
        print(query2,(userid,password,"F"))
        print(query,(userid,email, name,phone_number,Gender,House_Number,City,pincode,Dob))
        adi_conn.execute(query,(userid,email, name,phone_number,Gender,House_Number,City,pincode,Dob))
        # adi_conn.execut("")
        adi_conn1.commit()
        
                    # return render(request, 'create_account.html')
        return userids_show(request,userid)
    # print("JIJO")
    return render(request, 'create_account.html')



def Flights(request):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()

    adi_conn.execute("SELECT * FROM Flight,transport where transport.Transport_id = Flight.Transport_id")  # Assuming 'trains' is the table name
    flights = adi_conn.fetchall()  # Fetch all train data from the database
    print(flights)
    context = {'flights': flights}
    return render(request, 'Flights.html', context)

def Trains(request):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()

    adi_conn.execute("SELECT * FROM trains,transport where transport.Transport_id = Trains.Transport_id")  # Assuming 'trains' is the table name
    trains = adi_conn.fetchall()  # Fetch all train data from the database
    # print(trains)
    context = {'trains': trains}
    return render(request, 'Trains.html', context)


def Holidays(request):
    return render(request, 'Trains.html')

def Hotels(request):
    return render(request, 'Trains.html')

def search_trains(request):
    if request.method == 'GET':
        print("JIJI")
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        date = request.GET.get('date')
        
        # Fetch trains from the database based on the selected source, destination, and date
        # Perform database query here and fetch the results
        
        # For demonstration, let's assume you have a list of trains
        trains = [
            {'train_no': '12345', 'train_name': 'Express', 'departure_time': '10:00', 'arrival_time': '15:00'},
            {'train_no': '54321', 'train_name': 'Superfast', 'departure_time': '12:00', 'arrival_time': '17:00'}
        ]
        
        context = {
            'trains': trains
        }
        return render(request, 'Trains.html', context)
    else:
        # Handle other request methods (POST, etc.) if necessary
        pass
    print("HU")

def submit_booking(request):
    return render(request, 'Book.html')


def Book_full(request):
    try:
        user = usrer_info
        print("userifo defined")
    except:
        return login_view(request)
    user = user.all_details()
    d = {}
    print(user)
    d["userid"] = user[0][0]
    d["email"] = user[0][1]
    d["name"] = user[0][2]
    d["phone"] = user[0][3]
    d["gender"] = user[0][4]
    d["house_no"] = user[0][5]
    d["city"] = user[0][6]
    d["Pincode"] = user[0][7]
    d["dob"] = user[0][8]
    d["age"] = calculate_age(d["dob"]) # calculate please
    print(d)
    return render(request, 'book.html',{"user":d})

def userids_show(request,user_id):
    return render(request, 'userid_show.html', {"user_id":user_id})