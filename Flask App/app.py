from flask import Flask , jsonify , request

app = Flask(__name__)

data = [
    {
        "id":1,
        "contact":"1234567890",
        "name":"Raju",
        "done":False
    },
    {
        "id":2,
        "contact":"0987654321",
        "name":"Rahul",
        "done":False
    }
]

@app.route("/add_data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide The Data"
        },400)
    
    contact = {
        "id":data[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    
    data.append(contact)
    return jsonify({
        "status":"success",
        "message":"Data Added Succesfully"
    })
    
    
if __name__ == "__main__":
    app.run(debug=True)
