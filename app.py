import hug

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Quote(Base):
    __tablename__ = 'quotes'

    qid = Column(Integer, primary_key=True)
    author = Column(String)
    text = Column(String)

    def __repr__(self):
        return "<Quote(author='%s' text='%s')>" % (self.author, self.text[:10])


Base.metadata.create_all(engine)
for text in ['a', 'b', 'c']:
    quote = Quote(text=text)
    session.add(quote)
# session.commit()


@hug.get('/quotes')
def quotes():
    return [quote.text for quote in session.query(Quote).order_by(Quote.qid)]
