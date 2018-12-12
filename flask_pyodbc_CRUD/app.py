"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from flask_restful import Api, Resource
from flask import jsonify
import pyodbc

app = Flask(__name__)
api = Api(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

server = 'vminformdev01' 
database = 'GI_VS_SC_Test' 

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()

class FOOS(Resource):
    def get(self):
        cursor.execute("SELECT * FROM FOO;")       
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return jsonify(results)
        
class FOO(Resource):
    def get(self, id):
        cursor.execute("SELECT * FROM FOO WHERE fooKey =" + id)
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return jsonify(results)


api.add_resource(FOO, '/FOO/<id>')
api.add_resource(FOOS,'/FOOS')

if __name__ == '__main__':
    app.run(debug=True)



