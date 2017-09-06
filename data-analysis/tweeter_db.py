from sqlalchemy import (
    create_engine,
    Column,
    Boolean,
    String,
    Integer,
    ForeignKey,
    Table
)
from os import path

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
database_filename='tweeter.sqlite3'
directory =path.abspath(path.dirname(__file__))

database_filepath = path.join(directory,database_filename)

engine_url="sqlite:///{}".format(database_filepath)

engine=create_engine(engine_url)


Base=declarative_base(bind=engine)
Session=sessionmaker(bind=engine,autoflush=False)

session=Session()


hashtag_tweets= Table('hashtag_tweets',Base.metadata,
    Column('hashtag_id',Integer,ForeignKey('hashtags.id'),nullable=False),
    Column('tweet_id',Integer,ForeignKey('tweets.id'),nullable=False)
    )


class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    tid = Column(String(100), nullable=False, unique=True)
    tweet = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    coordinates = Column(String(50), nullable=True)
    user = relationship('User', backref='tweets')
    created_at = Column(String, nullable=False)
    favorite_count = Column(Integer)
    in_reply_to_screen_name = Column(String)
    in_reply_to_status_id = Column(String)
    in_reply_to_user_id = Column(String)
    lang = Column(String)
    quoted_status_id = Column(String)
    retweet_count = Column(Integer)
    source = Column(String)
    is_retweet = Column(Boolean)
    hashtags = relationship('Hashtag',
                            secondary='hashtag_tweets',
                            back_populates='tweets')


    def __repr__ (self):
        return '<tweet {}>'.format(self.id)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uid = Column(String(50), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    screen_name = Column(String)
    created_at = Column(String)
    # Nullable
    description = Column(String)
    followers_count = Column(Integer)
    friends_count = Column(Integer)
    statuses_count = Column(Integer)
    favourites_count= Column(Integer)
    listed_count = Column(Integer)
    geo_enabled = Column(Boolean)
    lang = Column(String)

    def __repr__(self) :
        return '<tweet {}>'.format(self.id)

    
class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, primary_key=True)
    text = Column(String(200), nullable=False, unique=True)
    tweets = relationship('Tweet',
                          secondary='hashtag_tweets',
                          back_populates='hashtags')

    def __repr__ (self):
        return '<tweet {}>'.format(self.id)


def init_db():
    Base.metadata.create_all()

init_db()


   
"""
import pandas as pd 
import sqlite3 
con=sqlite3.connect("tweeter.sqlite3")
df=pd.read_sql_query("SELECT tid FROM tweets",con)
"""