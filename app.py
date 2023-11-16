
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Python Developer',
        'location': 'New York',
        'salary': 50000,
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi',
        'salary': 60000,
    },
    {
        'id': 3,
        'title': 'Machine Learning Engineer',
        'location': 'New York',
        'salary': 70000,
    },
    {
        'id': 4,
        'title': 'Software Engineer',
        'location': 'Dubai',
        'salary': 80000,
    }
]

@app.route('/')
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name='Jovian')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)