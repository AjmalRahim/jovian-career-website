
from flask import Flask, render_template, request, redirect, url_for, flash
from database import load_jobs_from_db
from sqlalchemy.sql import text

app = Flask(__name__)



@app.route('/')
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='Jovian')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)