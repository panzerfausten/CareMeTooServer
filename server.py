from flask import Flask
from flask import request
app = Flask(__name__)

from ViewRenderer import ViewRenderer
@app.route("/")
def hello():
	    return "Hello World!"

#creates new users and gets existing users
@app.route("/users", methods=['GET','POST'])
def users():	
	if request.method == 'GET':
		v = ViewRenderer("showCaregivers")
		return v.render()
	elif request.method == 'POST':
		return "NEW USER"
	else:
		return "Method not supported"
	    
if __name__ == "__main__":
	app.run(debug=True)
