from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource): # inherit from resource class. Student is a new resource
    def get(self, name):
        return {'student': name}


api.add_resource(Student, '/student/<string:name>')

app.run()