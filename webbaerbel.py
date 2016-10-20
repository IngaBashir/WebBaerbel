from flask import Flask
app = Flask(__name__)

@app.route('/')
def start_page():
    return 'Startpage'

@app.route('/group')
def group_view():
   	return 'Group View'

@app.route('/create')
def create_group():
	return 'Create a group' 

@app.route('/group/add_member')
def add_member():
	return 'Add a new member'

@app.route('/group/add_restaurant')
def add_restaurant():
	return 'Add a new restaurant'	

@app.route('/group/delete')
def delete_member():
	return 'Are you sure you want to delete this member?'

