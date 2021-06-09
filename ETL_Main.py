import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
import datetime
username = input("username: ")
password = input("password: ")
ip_address = "aws-mysql-ssaca.cssuvkukhmkq.us-east-2.rds.amazonaws.com"
port_id = "3306"
database_name = "test_database"

engine = create_engine(f'mysql+pymysql://{username}:{password}@{ip_address}:{port_id}/{database_name}')
connection = engine.connect()

Base = declarative_base()


class Date(Base):
    __tablename__ = 'Date'

    Date_id = Column(Integer, autoincrement=True, primary_key=True)
    Date = Column(DateTime)
    Inflation = Column(Float)
    GDP = Column(Float)
    Metal_Price = Column(Float)
    NASDAQ = Column(Float)


# %%

class Price(Base):
    __tablename__ = 'Price'
    id = Column(Integer, autoincrement=True, primary_key=True)
    Date_id = Column(Integer, ForeignKey('Date.Date_id'))
    Area_Code = Column(String)
    Total_Condo_Sold_Number = Column(Integer)
    Avg_Price = Column(Float)
    Med_Price = Column(Integer)


# %%
class Toronto(Base):
    __tablename__ = 'Toronto'
    id = Column(Integer, autoincrement=True, primary_key=True)
    Date_id = Column(Integer, ForeignKey('Date.Date_id'))
    Prime_Rate = Column(Float)
    Median_Age = Column(Float)
    Participation_Rate = Column(Float)
    Employment_Rate = Column(Float)
    Population = Column(Float)
    UT_Total_Enrollment = Column(Integer)


# %%

class New(Base):
    __tablename__ = 'New'
    id = Column(Integer, autoincrement=True, primary_key=True)
    Date_id = Column(Integer, ForeignKey('Date.Date_id'))
    Units_Number_Planned = Column(Integer)
    Units_Number_Construction = Column(Integer)


# %%

class All(Base):
    __tablename__ = 'All'
    id = Column(Integer, autoincrement=True, primary_key=True)
    Date_id = Column(Integer, ForeignKey('Date.Date_id'))
    Condo_Sold_Number = Column(Integer)
    Avg_Price = Column(Float)


# %%
class Ontario(Base):
    __tablename__ = 'Ontario'
    id = Column(Integer, autoincrement=True, primary_key=True)
    Date_id = Column(Integer, ForeignKey('Date.Date_id'))
    Immigrants_International = Column(Float)


df = pd.read_json("files/raw_data.json")

df1 = df.T

df1['Date'] = df1['Date'].astype('datetime64')

session = Session(engine)

datelist = df1['Date'].unique()
start_time_total = datetime.datetime.now()
for i in range(len(datelist)):
    start_time_each = datetime.datetime.now()
    df1_date = df1[df1['Date'] == datelist[i]]


    date1 = Date(
        Date=datelist[i],
        Inflation=df1_date['Inflation'].tolist()[0],
        GDP=df1_date['GDP'].tolist()[0],
        Metal_Price=df1_date['Metal_Price'].tolist()[0],
        NASDAQ=df1_date['NASDAQ'].tolist()[0],
    )
    session.add(date1)
    session.commit()

    new1 = New(
        Date_id=date1.Date_id,
        Units_Number_Planned=df1_date['New_Units_Number_Planned'].tolist()[0],
        Units_Number_Construction=df1_date['New_Units_Number_Construction'].tolist()[0],
    )
    session.add(new1)

    Toronto1 = Toronto(
        Date_id=date1.Date_id,
        Prime_Rate=df1_date['Toronto_Participation_Rate'].tolist()[0],
        Median_Age=df1_date['Toronto_Median_Age'].tolist()[0],
        Participation_Rate=df1_date['Toronto_Participation_Rate'].tolist()[0],
        Employment_Rate=df1_date['Toronto_Employment_Rate'].tolist()[0],
        Population=df1_date['Toronto_Population'].tolist()[0],
        UT_Total_Enrollment=df1_date['UT_Total_Enrollment'].tolist()[0],
    )
    session.add(Toronto1)

    ontario1 = Ontario(
        Date_id=date1.Date_id,
        Immigrants_International=df1_date['Ontario_Immigrants_International'].tolist()[0]
    )
    session.add(ontario1)

    all1 = All(
        Date_id=date1.Date_id,
        Condo_Sold_Number=df1_date[df1_date['Area_Code'] == 'All']['Total_Condo_Sold_Number'].tolist()[0],
        Avg_Price=df1_date[df1_date['Area_Code'] == 'All']['Avg_Price'].tolist()[0],
    )
    session.add(all1)

    for i in range(df1_date.shape[0]):
        if df1_date.iloc[i]['Area_Code']!='All':
            price1 = Price(
                Date_id=date1.Date_id,
                Area_Code=df1_date.iloc[i]['Area_Code'],
                Total_Condo_Sold_Number=df1_date.iloc[i]['Total_Condo_Sold_Number'],
                Avg_Price=df1_date.iloc[i]['Avg_Price'],
                Med_Price=df1_date.iloc[i]['Med_Price'],
            )
            session.add(price1)

    session.commit()
    print(datetime.datetime.now()-start_time_each)

print("Finished. "+"Total time used"+str(datetime.datetime.now()-start_time_total))
