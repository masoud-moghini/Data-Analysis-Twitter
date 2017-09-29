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
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

database_filename = 'tweeter.sqlite3'
directory = path.abspath(path.dirname(__file__))

database_filepath = path.join(directory, database_filename)

engine_url = "sqlite:///{}".format(database_filepath)

engine = create_engine(engine_url)

Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

hashtag_tweets = Table('hashtag_tweets', Base.metadata,
                       Column('hashtag_id', Integer, ForeignKey('hashtags.id'), nullable=False),
                       Column('tweet_id', Integer, ForeignKey('tweets.id'), nullable=False)
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

    def __repr__(self):
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
    favourites_count = Column(Integer)
    listed_count = Column(Integer)
    geo_enabled = Column(Boolean)
    lang = Column(String)

    def __repr__(self):
        return '<tweet {}>'.format(self.id)


class Hashtag(Base):
    __tablename__ = 'hashtags'
    id = Column(Integer, primary_key=True)
    text = Column(String(200), nullable=False, unique=True)
    tweets = relationship('Tweet',
                          secondary='hashtag_tweets',
                          back_populates='hashtags')

    def __repr__(self):
        return '<tweet {}>'.format(self.id)


def init_db():
    Base.metadata.create_all()


init_db()

"""
import pandas as pd 
from dateutil.parser import *
from datetime import datetime


db_url='sqlite:///tweeter.sqlite3'
users=pd.read_sql_table("users",db_url)
tweets=pd.read_sql_table("tweets",db_url)
users['start_year']=users.created_at.apply(parse)
users['start_year']=users['start_year'].dt.year
users['start_month']=users.created_at.apply(parse).dt.month
users.groupby('start_year').size()



users['start_month'].value_counts().sort_index()== users.groupby('start_month').size()
users[users.start_year==2012].start_month.value_counts().sort_index()
tweets.merge(left_on='user_id',right_on='id')




"""

"""

def returnDate(created_at):
    # created_at=created_at.apply(parse)
    subtract = datetime(2006, 1, 3)
    subtractedDate = pd.Series()
    years = []
    months = []
    days = []
    print(type(created_at))
    print(created_at)
    for i, the_date in created_at.iteritems():
        years.append(the_date.year)
        months.append(the_date.month)
        days.append(the_date.day)
        date = datetime(years[i], months[i], days[i])
        date = date - subtract;
        print date
        subtractedDate.add(date)
    return subtractedDate
    
"""



"""
order no longer works use sort_values instead
iloc [[indices]] returns the element in specified indices
created_at.sort_values().iloc[[0,-1,-5]]



"""


"""

users.sort_values('favourites_count',ascending=False)[['name','favourites_count']]
name_influentials.to_json('name_influentials.json')
name_influentials.to_csv('name_influentials.csv')

"""


