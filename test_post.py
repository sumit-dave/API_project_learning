from flask import Flask, request, jsonify

app=Flask(__name__)

## GET means, we are posting a data in URL.
## POST means, we are posting a data in body.

@app.route('/abc', methods=['GET','POST'])
def test1():
    if(request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify(str(result))

@app.route('/efg/sumit', methods=['GET','POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify(str(result))






if __name__=='__main__':    ##invoke the Entire python project main classes
    app.run()



