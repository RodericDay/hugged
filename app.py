import sys
import hug

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker


if 'test' in sys.argv[0]:
    dbname = ':memory:'
else:
    dbname = 'db.sqlite'


engine = create_engine('sqlite:///'+dbname)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quotes'

    qid = Column(Integer, primary_key=True)
    author = Column(String)
    text = Column(String)

    def as_dict(self):
        return {k:v for k,v in self.__dict__.items() if k is not '_sa_instance_state'}

    def __repr__(self):
        return "<Quote(author='%s' text='%s')>" % (self.author, self.text[:10])


Base.metadata.create_all(engine)


@hug.get('/quotes')
def quotes():
    session = Session()
    return [quote.as_dict() for quote in session.query(Quote).order_by(-Quote.qid).limit(30)]

@hug.post('/quotes')
def quotes(text):
    session = Session()
    quote = Quote(text=text)
    session.add(quote)
    session.commit()

@hug.response_middleware()
def CORS(request, response, resource):
    response.set_header('Access-Control-Allow-Origin', '*')
    response.set_header('Access-Control-Allow-Headers', 'Content-Type')
