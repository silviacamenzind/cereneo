from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash
import dash_bootstrap_components as dbc


# Flask App
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/silvia/project.db'  # database URI is where the database is stored (sqlite3 project.db, .databases)

# SQLAlchemy
db = SQLAlchemy(server)  # Create the database instance

class patient(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)

class test(db.Model):
    test_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(255))

def print_test_data():
    # Create an application context
    with server.app_context():
        # Query all rows from the "test" table
        test_data = test.query.all()

        # Print the data
        for row in test_data:
            print("Test ID:", row.test_id)
            print("Name:", row.name)
            print("------------------------")

if __name__ == '__main__':
    # Call the function to print the data before running the server
    print_test_data()
    # Run the Flask app
    server.run(host='localhost', port=8055, debug=True)
