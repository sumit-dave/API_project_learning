from flask import Flask, request, jsonify

app=Flask(__name__)


@app.route('/testfun')
def test():
    get_name= request.args.get("name")
    moblie_no=request.args.get("mobile")
    Email_id=request.args.get("Email")
    return 'this is my function for get {} {} {}'. format(get_name, moblie_no, Email_id)

# This is the URL we have to use for upper code.
# http://127.0.0.1:5002/testfun?name=Sumit Kumar Gupta &mobile=8178448308 &Email=sumit@gmail.com

# important Question: need to show database data on website


import mysql.connector as conn

@app.route("/fetching")
def Data():
    database=request.args.get("db")
    table=request.args.get('table')
    try:
        mydb = conn.connect(host='localhost', user='root', passwd='12345')
        cursor = mydb.cursor()
        cursor.execute("select * from {}.{}".format(database, table))
        data=cursor.fetchall()
        mydb.commit()
        return jsonify(data)
    except Exception as e:
        return jsonify(str(e))

# This is the URL we have to use for upper code.
# http://127.0.0.1:5002/fetching?db=fitbit &table=fitbitdata



if __name__=="__main__":
    app.run(port=5002)