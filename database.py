from sqlalchemy import QueuePool, create_engine , text
from sqlalchemy.engine import result 

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://admin:Denon123!!@database-1.cfukce60iucr.us-east-1.rds.amazonaws.com:3306/dhoom"
engine = create_engine(DATABASE_URL)


# Create a session class using sessionmaker
Session = sessionmaker(bind=engine)

# Instantiate a session object
session = Session()

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs  


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()
      Base = declarative_base()

Base = declarative_base()
class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer)
    full_name = Column(String)
    email = Column(String)
    linkedin_url = Column(String)
    education = Column(String)
    work_experience = Column(String)
    resume_url = Column(String)

def add_application_to_db(job_id, data):
  application = Application(job_id=job_id,
                            full_name=data['full_name'],
                            email=data['email'],
                            linkedin_url=data['linkedin_url'],
                            education=data['education'],
                            work_experience=data['work_experience'],
                            resume_url=data['resume_url'])

  # Add the application to the session and commit
  session.add(application)
  session.commit()
