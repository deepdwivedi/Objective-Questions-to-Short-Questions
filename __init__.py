from flask import Flask,render_template,request,json
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

# class ReusableForm(Form):
	# ques = TextField("Question:",validators=[validators.required()])

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/courses')
def courses():
	# select = request.form.get('myfield')
	# print(str(select)) # just to see what select is
	return render_template("courses.html")

# @app.route('/is',methods=['GET', 'POST'])
# def in_ques():
# 	out = ""
# 	temp = ""
# 	form = ReusableForm(request.form)

# 	if(request.method=="POST"):
# 		if("pesticides" in request.form['name']):
# 			temp = "What is the form of pesticides"
# 		else:
# 			temp = "What is your mood right now?"
# 		print(request.form['name'])

# 	if(form.validate()):
# 		print("Done")
# 	else:
# 		print("Not Done")

# 	out=temp
# 	return render_template("is.html",form=form,out = out)

@app.route("/handler",methods=['POST'])
def handler():

	if request.method == 'POST':
		query = request.get_json()
		print(query)
	return json.jsonify({ 
        'ans': "final output" 
    }) 	
	
	#Your action goes here with corresponding ID
	# return render_template("courses.html","Action Completed | This gets returned to JavaScript Call")

if __name__ == '__main__':
    app.run(debug=True)