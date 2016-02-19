import hug

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    dbname = 'db.sqlite'
else:
    dbname = ':memory:'

engine = create_engine('sqlite:///'+dbname, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Quote(Base):
    __tablename__ = 'quotes'

    qid = Column(Integer, primary_key=True)
    author = Column(String)
    text = Column(String)

    def __repr__(self):
        return "<Quote(author='%s' text='%s')>" % (self.author, self.text[:10])


Base.metadata.create_all(engine)


@hug.get('/quotes')
def quotes():
    session = Session()
    return [quote.text for quote in session.query(Quote).order_by(Quote.qid)]

@hug.post('/quotes')
def quotes(text):
    session = Session()
    quote = Quote(text=text)
    session.add(quote)
    session.commit()
