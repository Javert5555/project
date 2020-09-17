
from flask import Flask, request, json
import  requests, data_content
app = Flask(__name__)


@app.route('/', methods = ["GET"])
def request_get():
    data = request.args
    a = data_content.open_content()
    response  = {} 
    response["response"] ={}
    response["response"]["text"] = a
    return response
 @app.royte('/content', methods = ["GET"])   
def parse():
    

if __name__ == "__main__":
    app.run()





