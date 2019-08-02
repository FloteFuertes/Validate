# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 20:43:08 2019

@author: FloteFuertes
"""

#!flask/bin/python
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify


db_connect = create_engine('sqlite:///conn.db')
app = Flask(__name__)
api = Api(app)



class GetCode(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from Reg_Ip")
        result = {'Data':[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    
class GetCodebyIP(Resource):
    def get(self,UserNumber):
        conn = db_connect.connect()
        query = conn.execute("select * from Reg_Ip where UserNumber = %d"  %int(UserNumber))
        result = {'Data':[dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(GetCode, '/Getcode')
api.add_resource(GetCodebyIP,'/Getcode/<UserNumber>')

if __name__ == '__main__' :
    app.run(port=5002)