'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import render_template,request,redirect,url_for,Flask
from gpt import GPT
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'
app = Flask(__name__)


# entry pages
@app.route('/')
def redirect_page():
    return render_template('index.html')

# required pages of the assignment 
@app.route('/index')
def display_index_page():
    return render_template('index.html')

@app.route('/team')
def display_team_page():
    return render_template('team.html')


@app.route('/about')
def display_about_page():
    root_dir = app.root_path
    return send_from_directory(root_dir + '/static/', "about.txt")


# set up from each member
@app.route('/trista', methods=['GET', 'POST'])
def display_trista_page():
    if request.method == 'POST':
        prompt = request.form['birthday']
        answer = gptAPI.tristaDemo(prompt)
        #write in the html code
        catPhoto_html= gptAPI.trista_catImage()
        
        return render_template('tristaDemo.html', prompt = prompt, answer = answer,catPhoto_html = catPhoto_html)
    else:
        root_dir = app.root_path
        return send_from_directory(root_dir + '/static/', "trista_form.html")
    
#Ran's part
@app.route('/ran', methods=['GET', 'POST'])
def display_ran_page():
    if request.method == 'POST':
        birthday = request.form['birthday']
        birthtime= request.form['birthtime']
        location= request.form['birthlocation']
        answer = gptAPI.ranDemo(birthday, birthtime, location)

        return render_template('ranDemo.html', answer = answer)
    else:
        root_dir = app.root_path
        return send_from_directory(root_dir + '/static/', "ran_form.html")


if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

 