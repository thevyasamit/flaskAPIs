from flask import Flask,jsonify
import requests

app = Flask(__name__)

'''
This is a home route which accepts 'GET' requests and returns a JSON formatted data
'''
@app.route("/home", methods=['GET'])
def hello_world():
    sample_data = [
        {
            'id':101,
            'name': 'Abc',
            'company': 'Google'
        },
        {
            'id':102,
            'name': 'Xyz',
            'company': 'Apple'
                       
        }] 
    return jsonify({'data':sample_data}),200

@app.route("/about", methods=['GET'])
def about():
    return 'Its about damn time'

'''
This route is used to check if the requested data is 
'''
@app.route("/data_check", methods =['POST'])
def data():
    try:
        obj = testDB()
        return 'Ok', 201
    except:
        status = 500
        return 'Database not found',status
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
