
from flask import Flask, render_template, jsonify, request

from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)



@app.route('/')
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs)

@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    return render_template('jobpage.html', job=job)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)