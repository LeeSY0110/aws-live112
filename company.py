from flask import Flask, render_template, request
from pymysql import connections
import os
import boto3
from config import *



app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'company'


#if call / then will redirect to that pg

#new

@app.route("/", methods=['POST'])
def companyReg():
    companyName = request.form['companyName']
    companyEmail = request.form['companyEmail']
    companyContact = request.form['companyContact']
    companyAddress = request.form['companyAddress']
    typeOfBusiness = request.form['typeOfBusiness']
    numOfEmployee = request.form['numOfEmployee']
    overview = request.form['overview']
    companyPassword = request.form['companyPassword']
    status = "Pending Approval"


    insert_sql = "INSERT INTO company VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()



    try:

        cursor.execute(insert_sql, (companyName, companyEmail, companyContact, companyAddress, typeOfBusiness, numOfEmployee, overview, companyPassword, status))
        db_conn.commit()


    except Exception as e:
        return str(e) 


    finally:
        cursor.close()

    print("all modification done...")
    return render_template('CompanyLogin.html')

@app.route("/studRegister", methods=['POST'])
def studRegister():
    cohort = request.form['cohort']
    internPeriod = request.form['internPeriod']
    studName = request.form['studName']
    studId = request.form['studId']
    studIc = request.form['studIc']
    studGender = request.form['studGender']
    programme = request.form['programme']
    studEmail = request.form['studEmail']
    studContact = request.form['studContact']
    uniSupervisor = request.form['uniSupervisor']
    uniEmail = request.form['uniEmail']

   
    insert_sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor = db_conn.cursor()

     

    try:

        cursor.execute(insert_sql, (cohort, internPeriod, studName, studId, studIc, studGender, programme, studEmail, studContact, uniSupervisor, uniEmail))
        db_conn.commit()
        

    except Exception as e:
        return str(e) 
        

    finally:
        cursor.close()

    print("all modification done...")
    return render_template('StudRegister.html')


@app.route("/StudViewCompany")
def StudViewCompany():
    status = "Approved"

    fetch_company_sql = "SELECT * FROM company WHERE status = %s"
    cursor = db_conn.cursor()

    try:
        cursor.execute(fetch_company_sql, (status))
        companyRecords = cursor.fetchall()
    
        return render_template('StudViewCompany.html', company=companyRecords)    

    except Exception as e:
        return str(e)      

    finally:
        cursor.close()



@app.route("/companyLogin")
def companyLogin():
    return render_template('CompanyLogin.html') 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
