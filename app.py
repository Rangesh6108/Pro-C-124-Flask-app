from flask import Flask,jsonify,request

app=Flask(__name__)

datas=[
    {
        'Contact':'9987644456',
        'name':'Raju',
        'done':False,
        'id':1
    },
    {
        'Contact':'9876543222',
        'name':'Rahul',
        'done':False,
        'id':2
    }
]

@app.route("/add-data",methods=['POST'])

def add_task():

    if not request.json:
        return jsonify({"status":"error","message":"Please provide the data!"},400)

    data={
        'id':datas[-1]['id']+1,
        'name':request.json['name'],
        'Contact':request.json.get("Contact",""),
        'done':False
    }
    datas.append(data)

    return jsonify({'status':'success','message':'Task added succesfully'})

@app.route("/get-data")

def get_data():
    return jsonify({
        "data":datas
    })

if (__name__=='__main__'):
    app.run(debug=True)


