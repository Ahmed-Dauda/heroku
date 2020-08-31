
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

app = Flask(__name__)



app = Flask(__name__)

@app.route('/posts')

def posts():
	
	posts = [
	{
	 'title' : 'post 1',
	  'body' : 'i am learnig flask app',
	  'image': "src = static/images/book2.jpeg  "
	  
	},
	{
	 'title' : 'post 2',
	  'body' : 'i am learnig flask app',
	  'image': "src = static/images/book6.jpeg  "
	  
	},
		{
	 'title' : 'post 2',
	  'body' : 'i am learnig flask app',
	  'image': "src = static/images/book4.jpeg  "
	  
	}
	]
	return render_template('home.html', posts = posts)

@app.route('/hello/<string:name>/post/<int:id>')

def hello (name, id):
	return 'hello ,! ' + name + '  your id is: ' + str(id)



if __name__=='__main__':
	app.run(debug=True)


