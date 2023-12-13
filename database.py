from sqlalchemy import create_engine, text
import os

db_connection_string =  "mysql+pymysql://admin:GAToSLGOVNUBu6gBziLA@jovian.c9ztkzyavckv.ap-south-1.rds.amazonaws.com/joviancareer"

engine = create_engine(db_connection_string)


def load_jobs_from_db():
    with engine.connect() as conn:
     result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
        jobs.append(dict(row._asdict()))
    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
     result = conn.execute(text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id))
     rows = result.all()
     if len(rows) == 0:
        return None
     else:
        return rows[0]