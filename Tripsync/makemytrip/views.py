import random
import time
# # Create a new user
# user = User.objects.create_user(username='example_user', password='example_password')
from datetime import datetime, timedelta

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
        #     return False
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
        global usrer_info
        usrer_info = user_cls(00000)
        username = request.POST.get('username')
        password = request.POST.get('password')
        query = "Insert Into log_entry (userid,is_success) Values (%s,%s)"
        # adi_conn1.commit()
        user = authenticate1(request, username=username, password=password)
        if user:
            # login(request, user)
            adi_conn.execute(query,(username,1))
            # time.sleep(3)
            # adi_conn1.commit()
            usrer_info.userid_set(username)
            adi_conn.execute("Update userids_passwords set tries = (%s) where userid = (%s)",(0,int(username)))
            adi_conn1.commit()
            return redirect(home_spl)  # Redirect to home page after successful login
        else:
            adi_conn.execute(query,(username,0))
            adi_conn1.commit()
            # adi_conn
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
def home_spl(request):
    return render(request, 'home.html')
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
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()
    adi_conn.execute('''SELECT *
FROM HolidayPackage,hotels,transport,flight
where (holidaypackage.Flight_No = flight.Flight_No and flight.Transport_Id = transport.Transport_Id and holidaypackage.Hotel_id = hotels.Hotel_id and transport.Destn_Loc = hotels.Location)
;''')  # Assuming 'trains' is the table name
    trains = adi_conn.fetchall()
    # print(trains[0])
    answer = []
    for i in range(len(trains)):
        answer.append(list(trains[i]))
    # for train in answer:
    # answer.append(min(answer[9],answer[15]-3))
        # print(train)
    
    print(answer)
    for ans in answer:
        ans.append(min(ans[9],ans[15]))
    context = {'trains': answer}
    return render(request, 'holiday.html',context)


def Hotels(request):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()
    adi_conn.execute("Select * from Hotels")
    hotels = adi_conn.fetchall() # fetching all hotels
    context = {'hotels':hotels}
    current_date_time=datetime.now()
    current_date_time += timedelta(days=1)
    return render(request, 'hotels.html', {"current_date_time": current_date_time, **context})

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
        alert_message = "Please Login first"
        return render(request, 'login.html', {'alert_message': alert_message})
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
def Payment(request):
    if request.method == 'POST':
        try:
            ur = usrer_info
        except:
            return redirect("http://127.0.0.1:8000/")
        global adi_conn1
        global adi_conn 
        adi_conn1 = mysql_bckens()
        adi_conn = adi_conn1.cursor()
        package_id = request.POST.get('package_id')
        train_id = request.POST.get('train_id')
        flight_id = request.POST.get('flight_id')
        hotel_id = request.POST.get('hotel_id')
        loc = request.POST.get('loc')
        start_loc = request.POST.get('start_loc')
        dest_loc = request.POST.get('dest_loc')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        age = request.POST.get('age')
        # price = request.POST.get('price')
        gender = request.POST.get('gender')
        quantity = request.POST.get('quantity') 
        print(flight_id) # debug
        user_details = {
            'train_id': train_id,
            'start_loc': start_loc,
            'dest_loc': dest_loc,
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'pincode': pincode,
            'age': age,
            'gender': gender,
            'quantity': quantity
            # 'price': price
        }
        if (package_id == None and (train_id!=None or flight_id!=None)):
            try:
                query = "INSERT INTO TICKETS (ticket_no, train_no, flight_no, amount, date_of_journey, quantity, userid, is_valid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                query2 = "INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) VALUES (%s,%s,%s,%s,%s,%s)"
                adi_conn.execute("Select ticket_no from tickets")
                s = [x[0] for x in adi_conn.fetchall()]
                print(s)
                adi_spl = s[0]
                while adi_spl in s:
                    adi_spl = random.randint(99,12345)
                print(adi_spl)
                p =[]
                print(train_id)
                if train_id:
                    print("NO")
                if train_id:
                # p = []:
                    adi_conn.execute("Select price,timings,vacany from transport,trains where transport.transport_id = trains.transport_id and trains.train_no = (%s) ",(int(train_id),))
                    p = adi_conn.fetchall()
                    
                # print("Select price,timings from transport,trains where transport.transport_id = trains.transport_id and trains.train_no = (%s) ",(int(train_id),))
                # p = adi_conn.fetchall()
                if not(p):
                    adi_conn.execute("Select price,timings,vacany from transport, flight where transport.transport_id = flight.transport_id and flight.flight_no = (%s) ",(int(flight_id),))
                    p = adi_conn.fetchall()
                print(p)
                # exit(0)
                q = p[0][1]
                vac = p[0][2]
                if vac<0:
                    return render("error.html")
                elif vac==0 or (vac-int(quantity))<0:
                    return redirect("/home/?seats_full=True")
                
                p = p[0][0]
                # user_details['price'] = p
                price = {"price": p*int(quantity)}
                print(p,int(p),type(p))
                # q = 
                if train_id:
                    flight_id = None
                    train_id = int(train_id)
                else:
                    train_id = None
                    flight_id = int(flight_id)
                ans = (adi_spl,train_id,flight_id,int(p)*int(quantity),q,int(quantity),int(usrer_info.user_id()),1)
                print(ans)
                # exit()
                adi_conn.execute(query,ans)
                adi_conn.execute("select payment_id from payments")
                hoho = adi_conn.fetchall()
                hoho = [x[0] for x in hoho]
                hoho1 = hoho[0]
                while hoho1 in hoho:
                    hoho1 = random.randint(1,1234556)
                print(hoho1)
                ans2 = (hoho1, usrer_info.user_id(),adi_spl,1,None,datetime.now())
                print(ans2)
                adi_conn.execute(query2,ans2)
                if train_id:
                    adi_conn.execute("Select transport_id from trains where train_no = (%s)",(train_id,))
                    lop = adi_conn.fetchall()
                    lop = lop[0][0]
                    adi_conn.execute("update transport set vacany = (%s) where transport_id = (%s)",(vac-int(quantity),lop))
                else:
                    adi_conn.execute("Select transport_id from flight where flight_no = (%s)",(flight_id,))
                    lop = adi_conn.fetchall()
                    lop = lop[0][0]
                    adi_conn.execute("update transport set vacany = (%s) where transport_id = (%s)",(vac-int(quantity),lop))
                    print("hsods",int(quantity))
                # adi_conn1.commit()
                # adi_conn.execute
                # adi_conn.execute()
            except Exception as e:
                print(e)
                return render(request,'error.html')
        elif package_id != None:
            print("hi",hotel_id)
            adi_conn.execute("Select price from holidaypackage where package_id = %s",(package_id,))
            tyyy = adi_conn.fetchall()
            owl = int(tyyy[0][0])
            # adi_conn.execute()
            query = "INSERT INTO TICKETS (ticket_no, train_no, flight_no, amount, date_of_journey, quantity, userid, is_valid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            query2 = "INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) VALUES (%s,%s,%s,%s,%s,%s)"
            price1 = request.POST.get('price')
            print("scnsnsldsmsdms",price1)
            adi_conn.execute("Select ticket_no from tickets")
            s = [x[0] for x in adi_conn.fetchall()]
            print(s)
            adi_spl = s[0]
            while adi_spl in s:
                adi_spl = random.randint(99,12345)
            print(adi_spl)
            p =[]
            print(train_id)
            if train_id:
                print("NO")
            if train_id:
            # p = []:
                adi_conn.execute("Select price,timings,vacany from transport,trains where transport.transport_id = trains.transport_id and trains.train_no = (%s) ",(int(train_id),))
                p = adi_conn.fetchall()
            # print("Select price,timings from transport,trains where transport.transport_id = trains.transport_id and trains.train_no = (%s) ",(int(train_id),))
            # p = adi_conn.fetchall()
            if not(p):
                adi_conn.execute("Select price,timings,vacany from transport, flight where transport.transport_id = flight.transport_id and flight.flight_no = (%s) ",(int(flight_id),))
                p = adi_conn.fetchall()
            print(p)
            q = p[0][1]
            vac = p[0][2]
            if vac<0:
                return render("error.html")
            elif vac==0 or (vac-int(quantity))<0:
                return redirect("/home/?seats_full=True")
            adi_conn.execute("Select vacancy,pricing from Hotels where Hotel_id = %s",(hotel_id,))
            rt = adi_conn.fetchall()
            print(rt)
            p = rt[0][1]
            rt = rt[0][0]
            if rt<0:
                return render(request,'error.html')
            elif rt==0 or rt-int(quantity)<0:
                return redirect("/home/?seats_full=True")
            adi_conn.execute("update hotels set vacancy = %s where hotel_id = %s",(rt-int(quantity),hotel_id))
            adi_conn.execute("Insert Into hotel_invoice (Date_of_entering,Hotel_id,userid) values (%s, %s, %s)",(datetime.now(),hotel_id,int(usrer_info.user_id())))
            adi_conn.execute("select payment_id from payments")
            hoho = adi_conn.fetchall()
            hoho = [x[0] for x in hoho]
            hoho1 = hoho[0]
            while hoho1 in hoho:
                hoho1 = random.randint(1,1234556)
            print(hoho1)
            ans = (adi_spl,train_id,flight_id,int(owl)*int(quantity),q,int(quantity),int(usrer_info.user_id()),1)
            print(ans)
            # exit()
            adi_conn.execute(query,ans)
            ans2 = (hoho1, int(usrer_info.user_id()),adi_spl,1,hotel_id,datetime.now())
            adi_conn.execute(query2,ans2)
            adi_conn.execute("Select transport_id from flight where flight_no = (%s)",(flight_id,))
            lop = adi_conn.fetchall()
            lop = lop[0][0]
            adi_conn.execute("update transport set vacany = (%s) where transport_id = (%s)",(vac-int(quantity),lop))
            print("hsods",int(quantity))
            price = {"price":int(quantity)*(int(owl))}
        else:
            print("hi",hotel_id)
            adi_conn.execute("Select vacancy,pricing from Hotels where Hotel_id = %s",(hotel_id,))
            rt = adi_conn.fetchall()
            p = rt[0][1]
            rt = rt[0][0]
            if rt<0:
                return render(request,'error.html')
            elif rt==0 or rt-int(quantity)<0:
                return redirect("/home/?seats_full=True")
            else:
                adi_conn.execute("update hotels set vacancy = %s where hotel_id = %s",(rt-int(quantity),hotel_id))
                adi_conn.execute("Insert Into hotel_invoice (Date_of_entering,Hotel_id,userid) values (%s, %s, %s)",(datetime.now(),hotel_id,int(usrer_info.user_id())))
                adi_conn.execute("select payment_id from payments")
                hoho = adi_conn.fetchall()
                hoho = [x[0] for x in hoho]
                hoho1 = hoho[0]
                while hoho1 in hoho:
                    hoho1 = random.randint(1,1234556)
                print(hoho1)
                query2 = "INSERT INTO Payments (Payment_Id, User_id, Ticket_id, Payment_Status, Hotel_id, Date_of_payment) VALUES (%s,%s,%s,%s,%s,%s)"
                ans2 = (hoho1, int(usrer_info.user_id()),None,1,hotel_id,datetime.now())
                adi_conn.execute(query2,ans2)
                price = {"price": p*int(quantity)}
        return render(request, 'payment.html',{"price": price})
def spl_comm(request):
    # adi_conn.execute("Select transport_id from flight where flight_no = (%s)",(,))
    adi_conn1.commit()
    return render(request,'home.html')
def Tickets(request):
    adi_conn1 = mysql_bckens()
    adi_conn = adi_conn1.cursor()
    try:
        usr = usrer_info  # Assuming this is a valid variable containing user information
    except:
        return render(request, 'login.html', {"alert_message": "Please Login to see upcoming Journeys"})
    ty = usr.user_id()
    adi_conn.execute("SELECT * FROM tickets WHERE userid = (%s) AND is_valid = (%s)", (ty, 1))
    r = adi_conn.fetchall()
    for i in range(len(r)):
        if r[i][1] == None:
            adi_conn.execute("SELECT * FROM transport,flight WHERE transport.transport_id = flight.transport_id and flight_no = (%s)",(r[i][2],))
            ui = adi_conn.fetchall()
            r[i] = r[i]+(ui[0][1],ui[0][2])
        else:
            adi_conn.execute("SELECT * FROM transport,trains WHERE transport.transport_id = trains.transport_id and train_no = (%s)",(r[i][1],))
            ui = adi_conn.fetchall()
            r[i] = r[i]+(ui[0][1],ui[0][2])
        
    print(r)  # Check to ensure you're getting the expected data
    upcoming_journeys = {'tickets': r}  # Assuming r is a list of dictionaries
    return render(request, 'ticket.html', upcoming_journeys)


def profile(request):
    try:
        user = usrer_info
        print("userifo defined")
    except:
        alert_message = "Please Login first"
        return render(request, 'login.html', {'alert_message': alert_message})
    # user = user.all_details()
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
    return render(request,"profile.html",{'user':d})

def logout(request):
    global usrer_info
    del usrer_info 
    return redirect("http://127.0.0.1:8000/")