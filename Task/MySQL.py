# Now task answers
# 1 . Write a program to insert a record in sql table via api
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api


from flask import Flask, request, jsonify

import mysql.connector as conn
mydb=conn.connect(host='localhost', user='root', passwd='12345')
cursor=mydb.cursor()
cursor.execute('create database if not exists tasksql')
cursor.execute("create table if not exists tasksql.table1( Name varchar(30), Number int(10))")


app=Flask(__name__)

# Answer 1: Write a program to insert a record in sql table via api
@app.route('/insert', methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        # We can regularly change name and number value in Postman
        cursor.execute("insert into tasksql.table1 values(%s , %s)",(name, number))
        mydb.commit()
        return jsonify(str("insert completed"))


# Answer 2: Write a program to update a record via api
@app.route("/update", methods=['POST'])
def update():
    if request.method=='POST':
        get_name=request.json['get_name']
        cursor.execute('update tasksql.table1 set number=number+500 where name = %s', (get_name,))
        mydb.commit()
        return jsonify(str('Updated successfully'))


# Answer 3: Write a program to delete a record via api
@app.route("/delete", methods=['POST'])
def delete():
    if request.method=='POST':
        number_del=request.json['number_del']
        cursor.execute('delete from tasksql.table1 where number= %s', (number_del,))
        mydb.commit()
        return jsonify(str('deleted successfully'))


# Answer 4: Write a program to fetch a record via api

@app.route("/fetch", methods=['POST'])
def fetch():
    cursor.execute('select * from tasksql.table1')
    l=[]
    all= cursor.fetchall()
    for i in all:
        l.append(i)
    return jsonify(str(l))



if __name__=='__main__':
    app.run()












