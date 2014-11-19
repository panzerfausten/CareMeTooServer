from flask import Flask
from flask import request
app = Flask(__name__,static_url_path="")
from flask import send_from_directory
from ViewRenderer import ViewRenderer
from models import CareGiver,Data,Event,Multimedia

######################upload files
import os
from flask import redirect, url_for
from werkzeug import secure_filename
import datetime
import time
UPLOAD_FOLDER = 'files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


###################
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
@app.route("/caregivers/<int:caregiver_id>/files")
def getFile(caregiver_id):
	if request.method == "GET":
		_filePath = request.args.get("filepath")
		return send_from_directory("files",_filePath)
@app.route("/caregivers/<int:caregiver_id>/event",methods=['GET','POST'])
def careGiverEvent(caregiver_id):
	if request.method == 'GET':
		_E = Event.Event()
		_all = _E.all(caregiver_id,toList=False,toJson=True)
		return str(_all)
	elif request.method == 'POST':
		_E = Event.Event()
		_activity               = request.form['activity']
		_mood                   = request.form['mood']
		_description            = request.form['description']
		_mdescription            = request.form['mdescription']
		print "file"
		_timestamp = request.form['timestamp']
		###MULTIMEDIA FILE
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		_ts_filename = "%s-%s"
		
		file = request.files['file']
		if file and allowed_file(file.filename):
			_ts_filename = _ts_filename % (st,file.filename)
			filename = secure_filename(_ts_filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			#if file uploaded, create multimedia entry
			_M = Multimedia.Multimedia()
			_m = _M.insert(caregiver_id,_mdescription,filename,"")
			_e = _E.insert(idcaregiver=caregiver_id,idmultimedia=_m.idmultimedia,activity=_activity,mood=_mood,description=_description,timestamp=_timestamp)
		else:
			_e = _E.insert(idcaregiver=caregiver_id,activity=_activity,mood=_mood,description=_description,timestamp=_timestamp)


		#_res = _e.insert(idcaregiver=caregiver_id,idmultimedia=-1,activity=_activity,mood=_mood,description=_description,timestamp=_timestamp)
		return _e.toJson()
	else:
		return "Method not supported"
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/files', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "file uploaded modafaka"#redirect(url_for('uploaded_file',
                    #                filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="../caregivers/1/event" method=post enctype=multipart/form-data>
      <p><input type=file name=file></br>
	 Caregiver ID:<input type=text name=caregiver_id></br>
	 Activity<input type=text name=activity></br>
	 Mood:<input type=text name=mood></br>
	 Description:<input type=text name=description></br>
	 Timestamp:<input type=text name=timestamp></br
         <input type=submit value=Upload>
    </form>
    '''



if __name__ == "__main__":
	app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	app.run(debug=True,host='0.0.0.0')
