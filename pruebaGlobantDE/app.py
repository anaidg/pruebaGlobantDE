from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime as datetime
import pandas as pd
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:user2023@localhost:3306/stage'
db = SQLAlchemy(app)

class Hired_Employees(db.Model):
    __tablename__= 'hired_employees'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))
    datetime    = db.Column(db.String(255))
    department_id  = db.Column(db.Integer)
    job_id         = db.Column(db.Integer)

class Departments(db.Model):
    __tablename__= 'departments'
    id           = db.Column(db.Integer, primary_key=True)
    department   = db.Column(db.String(255))

class Jobs(db.Model):
    __tablename__= 'jobs'
    id           = db.Column(db.Integer, primary_key=True)
    job          = db.Column(db.String(255))

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        with app.app_context():
            # Obtener los archivos CSV del request
            csv_files = request.files.getlist('files')
            
            if not csv_files:
                return jsonify({"message": "No se proporcionaron archivos CSV"}), 400

            for index, csv_file in enumerate(csv_files, start=1):
                # Cargar el CSV en un DataFrame de pandas
                                
                # Insertar los datos en la tabla correspondiente
                if index == 1:
                    df = pd.read_csv(csv_file,header=None)
                                        
                    # Renombrar las columnas del DataFrame para que coincidan con los nombres de la tabla
                    df.columns = ['id', 'name', 'datetime', 'department_id', 'job_id']
                    df.to_sql(Hired_Employees.__tablename__, db.engine, if_exists='append', index=False)

                elif index == 2:
                    df = pd.read_csv(csv_file,header=None)
                    df.columns = ['id', 'department']
                    df.to_sql(Departments.__tablename__, db.engine, if_exists='append', index=False)

                elif index == 3:
                    df = pd.read_csv(csv_file,header=None)
                    df.columns = ['id', 'job']
                    df.to_sql(Jobs.__tablename__, db.engine, if_exists='append', index=False)
            
            return jsonify({"message": "Datos CSV insertados en las tablas de la base de datos correctamente"}), 201
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

