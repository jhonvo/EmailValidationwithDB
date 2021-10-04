from survey_app.config.mysqlconnection import connectToMySQL
from survey_app import app
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Survey:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def savingform(cls,data):
        query = "INSERT INTO email (email) VALUES (%(email)s);"
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return results

    @classmethod
    def getsubmission(cls,email):
        query = "SELECT * FROM email WHERE email = %(email)s;"
        data = {
            'email' : email
        }
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        # submission = []
        # for line in results:
        #     submission.append(Survey(line))
        return results

    @classmethod
    def remove (cls,id):
        query = "DELETE FROM email WHERE id = %(id)s"
        data = {
            'id' : id
        }
        results = connectToMySQL("dojo_survey_schema").query_db(query,data)
        return results

    @classmethod
    def getall(cls):
        query = "SELECT * FROM email;"
        results = connectToMySQL("dojo_survey_schema").query_db(query)
        submission = []
        for line in results:
            submission.append(Survey(line))
        return submission

    @staticmethod
    def validate_survey(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Please provide a valid email address")
            is_valid = False
        return is_valid
