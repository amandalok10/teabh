







# for each in list:
#     while each[0] == k:
#         dict[k] = [each]
#         k = k + 1


list = [(1, 'amanda', 'loka'),
(1, 'sue', 'sue@'),
(1, 'friend', 'friend@'),
(1, 'bob', 'bob@'),
(2, 'group 2', '2@'),
(4, 'sam', 'sam@'),
(3, 'john', 'john@')]



# dict = {}
#
# for each in list:
#     if not each[0] in dict:
#         dict[each[0]] = [each]
#     else:
#         dict[each[0]].append(each)
#
# for key, value in dict.items():
#     print(value[1])


def getid():
    for each in list:
        print("curor", each[-1])

getid()
















# #Amanda Lok
# #ITP 499
# #loka@usc.edu
# #Final Project
#
# import requests
# import mysql.connector
# import os
#
# host = os.environ.get('MYSQL_HOST')
# database = os.environ.get('MYSQL_DATABASE')
# password = os.environ.get('MYSQL_PASSWORD')
# user = os.environ.get('MYSQL_USER')
#
# connection = mysql.connector.connect(host=host, user=user, password=password, database=database, port=25060)
#
#
# from flask import Flask, render_template, request, Response
#
# cursor = connection.cursor()
#
# app = Flask(__name__)
#
# @app.route('/home', methods=['GET'])
# def home():
#     list = []
#     sql = "SELECT * FROM clusters"
#     cursor.execute(sql)
#     for x in cursor:
#         list.append(x)
#     return render_template('home.html', results = list)
#
#
#
#
# @app.route('/postendpoint', methods=['POST'])
# def post():
#     resp = Response(status=200)
#     print(request.data)
#     return resp
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# #Amanda Lok
# #ITP 499
# #loka@usc.edu
# #Final Project
#
# import requests
# import mysql.connector
# import os
#
# host = os.environ.get('MYSQL_HOST')
# database = os.environ.get('MYSQL_DATABASE')
# password = os.environ.get('MYSQL_PASSWORD')
# user = os.environ.get('MYSQL_USER')
#
# connection = mysql.connector.connect(host=host, user=user, password=password, database=database, port=25060)
#
# from flask import Flask, render_template, request, Response
#
# cursor = connection.cursor()
#
# #dont foregt to impletment error handling
#
# app = Flask(__name__)
#
# countries = []
#
# @app.route('/home', methods=['POST'])
# def my_form_post():
#     fname = request.form["fname"]
#     lname = request.form["lname"]
#     birthday = request.form["birthday"]
#     origin = request.form["origin"]
#     # sql = "INSERT INTO users(firstname, lastname, birthday, origin) VALUES (%s, %s, %s, %s)"
#     # val = (fname, lname, birthday, origin)
#     # cursor.execute(sql, val)
#     connection.commit()
#     return "howdy"
#
# @app.route('/view', methods=['GET'])
# def view():
#     r = requests.get('https://restcountries.eu/rest/v2/name/?fullText=true')
#     resp = r.json()
#     capital = resp[0]['capital']
#     population = resp[0]['population']
#     region = resp[0]['region']
#     flag = resp[0]['flag']
#     return render_template('view.html')
#
# @app.route('/home')
# def home():
#     jsonresp = requests.get('https://www.boredapi.com/api/activity?participants=1')
#     respresults = jsonresp.json()
#     print(respresults["activity"])
#     return render_template('home.html')
#
# @app.route('/add', methods=['GET'])
# def add():
#     jsonresp = requests.get('https://restcountries.eu/rest/v2/all')
#     respresults = jsonresp.json()
#     for each in respresults:
#         countries.append(each['name'])
#     return render_template('add.html', countries = countries)
#
#
#
# @app.route('/postendpoint', methods=['POST'])
# def post():
#     resp = Response(status=200)
#     print(request.data)
#     return resp
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

