# Now task answers
# 1 . Write a program to insert a record in MongoDB table via api
# 2.  Write a program to update a record via api
# 3 . Write a program to delete a record via api
# 4 . Write a program to fetch a record via api

from flask import Flask, request, jsonify
import pymongo
client = pymongo.MongoClient("mongodb+srv://user:root@cluster.a5ybbld.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database=client['task_database']
collection=database['task_table']

app=Flask(__name__)

# Answer 1: Write a program to insert a record in MongoDB table via api

@app.route('/insert/mongo', methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        # We can regularly change name and number value in Postman
        collection.insert_one({name:number})
        return jsonify(str("insert completed"))

# Answer 2: Write a program to update a record via api

@app.route('/update/mongo', methods=["POST"])
def update():
    if request.method=='POST':
        get_name = request.json["get_name"]
        new_name= request.json["new_name"]
        collection.update_one({"name":get_name}, {'$set':{"name":new_name}})
        return jsonify(str('Updated successfully'))





if __name__=='__main__':
    app.run(port=5001)
