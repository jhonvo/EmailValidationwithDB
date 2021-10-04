from flask import Flask, render_template, session, redirect, request
from survey_app import app
from survey_app.models.survey import Survey
from flask import flash


@app.route('/', methods=['GET'])
def index():
    # print(session)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def route():
    print (request.form)
    data = request.form
    user_in_db = Survey.getsubmission(data['email'])
    print ("user in db", user_in_db)
    if user_in_db:
        flash("The email already exists...")
        return redirect ('/')
    if not Survey.validate_survey(data):
        return redirect ('/')
    newsubmission = Survey.savingform(data)
    return redirect('/results')

@app.route('/results', methods=['GET'])
def resultpage():
    information = Survey.getall()
    return render_template('results.html', submission = information)

@app.route('/remove/<int:id>')
def remove(id):
    removing = Survey.remove(id)
    return redirect ('/results')

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')