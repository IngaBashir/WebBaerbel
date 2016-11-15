from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

db={
	'LIQD':{'restaurants': ['Tschuesch', 'Sahara', 'Pizza'], 'members': ['Inga', 'Üffes', 'Bengfort']},
	'Mörike32':{'restaurants': ['mama'], 'members': []}
	}

@app.route('/')
def start_page():
	return render_template('startpage.html')

@app.route('/group/<groupname>')
def group_view(groupname):
	return render_template('group.html', groupname=groupname, restaurants=db[groupname]['restaurants'], members=db[groupname]['members'])

@app.route('/create')
def create_group():
	return render_template('create.html') 

@app.route('/group/<groupname>/add_member', methods=['GET', 'POST'])
def add_member(groupname):
	if request.method == 'POST': 
		db[groupname]['members'].append(request.form['member'])
		return 'wurde hinzugefügt'
	else:  	
		return render_template('add_member.html', groupname=groupname)

@app.route('/group/<groupname>/add_restaurant')
def add_restaurant(groupname):
	return render_template('add_restaurant.html', groupname=groupname)

@app.route('/group/<groupname>/delete_member')
def delete_member(groupname):
	return render_template('delete_member.html', groupname=groupname)

@app.route('/group/<groupname>/delete_member/terminate_group')
def terminate_group(groupname):
	return render_template('terminate_group.html', groupname=groupname)

