from flask import Flask
from flask import request
app = Flask(__name__)

from ViewRenderer import ViewRenderer
from models import CareGiver
from models import Data
@app.route("/")
def hello():
	    return "Hello World!"

#creates new users and gets existing users
@app.route("/caregivers", methods=['GET','POST'])
def users():	
	if request.method == 'GET':
		v = ViewRenderer("showCaregivers")
		c = CareGiver.CareGiver()
		_all = c.all(toList=True)
		_result = ""
		return str(_all)
		#return v.render()
	elif request.method == 'POST':
		_c = CareGiver.CareGiver()
		_name = request.form['name']
		_username = request.form['username']
		_password = request.form['password']
		#TODO:validate
		_res =_c.insert(_name,_username,_password).toJson()
		return _res
	else:
		return "Method not supported"
@app.route("/caregivers/<int:caregiver_id>/data",methods=['GET','POST'])
def careGiverData(caregiver_id):
	if request.method == 'GET':
		_D = Data.Data()
		_all = _D.all(caregiver_id,toList=True)
		_result = ""
		return str(_all)
	elif request.method == 'POST':
		_d = Data.Data()
		_datatype = request.form['datatype']
		_value = request.form['value']
		_extra = request.form['extra']
		_location = request.form['location']
		_timestamp = request.form['timestamp']
		_res = _d.insert(caregiver_id,_datatype,_value,_extra,_location,_timestamp)
		return _res.toJson()
	else:
		return "Method not supported"
if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0')
