from flask import Flask  , request , jsonify
app=Flask(__name__)

@app.route("/test", methods=["GET" , "POST"])
def home():

    # for get method
    if request.method=="GET":
        return jsonify({"response ": "GET request responed"})

    # for post method
    elif request.method=="POST":
        json_req=request.json
        name=json_req["name"]
        return jsonify({"response " :"HI "+name +" With post request"})
 



if __name__=="__main__":
     app.run(debug=True , port=100)
