#Amanda Lok
#ITP 499
#loka@usc.edu
#Final Project


#
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']


import requests
import mysql.connector
import os

host = os.environ.get('MYSQL_HOST')
database = os.environ.get('MYSQL_DATABASE')
password = os.environ.get('MYSQL_PASSWORD')
user = os.environ.get('MYSQL_USER')

namelist = []

connection = mysql.connector.connect(host=host, user=user, password=password, database=database, port=25060)

from flask import Flask, render_template, request, Response

cursor = connection.cursor()

#dont foregt to impletment error handling

app = Flask(__name__)


def updatehome():
    sql = "SELECT * FROM clusters ORDER BY clusterid ASC"
    cursor.execute(sql)
    dict = {}
    for each in cursor:
        if not each[0] in dict:
            dict[each[0]] = [each]
        else:
            dict[each[0]].append(each)
    return dict

def getid():
    getdict = updatehome()
    print(getdict)
    if getdict == {}:
        return 1
    else:
        return list(getdict.keys())[-1] + 1



@app.route('/home', methods=['POST'])
def entry():
    if request.form["friend1name"] and request.form["friend1email"] is not None:
        f1name = request.form["friend1name"]
        f1email = request.form["friend1email"]
    else:
        f1name = ""
        f1email = ""

    if request.form["friend2name"] and request.form["friend2email"] is not None:
        f2name = request.form["friend2name"]
        f2email = request.form["friend2email"]
    else:
        f2name = ""
        f2email = ""

    if request.form["friend3name"] and request.form["friend3email"] is not None:
        f3name = request.form["friend3name"]
        f3email = request.form["friend3email"]
    else:
        f3name = ""
        f3email = ""

    if request.form["friend4name"] and request.form["friend4email"] is not None:
        f4name = request.form["friend4name"]
        f4email = request.form["friend4email"]
    else:
        f4name = ""
        f4email = ""

    id = getid()
    print("id", id)


    if f1name and f1email != "":
        print("f1 in")
        sql = "INSERT INTO clusters VALUES (%s, %s, %s)"
        val = (id, f1name, f1email)
        cursor.execute(sql, val)
        connection.commit()
    else:
        print("f1 empty")


    if f2name and f2email != "":
        print("f2 in")
        sql = "INSERT INTO clusters VALUES (%s, %s, %s)"
        val = (id, f2name, f2email)
        cursor.execute(sql, val)
        connection.commit()
    else:
        print("f2 empty")

    if f3name and f3email != "":
        print("f3 in")
        sql = "INSERT INTO clusters VALUES (%s, %s, %s)"
        val = (id, f3name, f3email)
        cursor.execute(sql, val)
        connection.commit()
    else:
        print("f3 empty")

    if f4name and f4email != "":
        print("f4 in")
        sql = "INSERT INTO clusters VALUES (%s, %s, %s)"
        val = (id, f4name, f4email)
        cursor.execute(sql, val)
        connection.commit()
    else:
        print("f4 empty")

    newhome = updatehome()
    return render_template('home.html', results = newhome)


@app.route('/home')
def home():
    names = updatehome()
    return render_template('home.html', results=names)



@app.route('/view', methods=['GET'])
def view():
    clusterid = request.args.get("clusterid")
    fulldict = updatehome()
    clusterid = int(clusterid)
    if clusterid not in fulldict.keys():
        return "Error. Cluster does not exist."
    else:
        global namelist
        namelist = fulldict[clusterid]
    participants = str(len(namelist))
    # BORED API
    jsonresp = requests.get('http://www.boredapi.com/api/activity?participants=' + participants)
    respresults = jsonresp.json()
    act = respresults["activity"]
    return render_template('view.html', activity = act, details = namelist, number = participants)

@app.route('/view', methods=['POST'])
def my_link():
    global namelist
    emails = [x[2] for x in namelist]
    participants = str(len(namelist))
    # BORED API
    jsonresp = requests.get('http://www.boredapi.com/api/activity?participants=' + participants)
    respresults = jsonresp.json()
    act = respresults["activity"]
    print ('I got clicked!')
    creds = None
    # GOOGLE CALENDAR API
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file  (
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': 'You received an invite!',
        'location': 'Los Angeles, California',
        'description': act,
        'start': {
            'dateTime': '2020-05-29T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2020-05-29T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': 'a@gmail.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    event = service.events().insert(calendarId='project.tea8@gmail.com', body=event, sendNotifications=True).execute()
    print('Event created: %s' % (event.get('htmlLink')))

    return render_template('confirm.html')


@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

@app.route('/add')
def add():
    return render_template('add.html')




@app.route('/postendpoint', methods=['POST'])
def post():
    resp = Response(status=200)
    print(request.data)
    return resp


if __name__ == '__main__':
    app.run(debug=True)


#I used a default calendar as the main user of the website. The event auto-populates the main user's
# (in this case, project.tea8@gmail.com) and sends a Google Calendar invite to the other people in the cluster.

#for loop the email json
#hw9 grade

