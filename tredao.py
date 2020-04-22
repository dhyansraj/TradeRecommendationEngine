from util import fromisoformat

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

db_uri = "mysql://tre:admin@127.0.0.1/TRE"
engine = create_engine(db_uri)

Base = declarative_base()

# Declare a table
class HistoricalRatesTable(Base):
    __tablename__ = "HistoricalRates"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    symbol = Column(String(16))
    data0 = Column(Numeric(20, 6, asdecimal=True))
    data1 = Column(Numeric(20, 6, asdecimal=True))
    data2 = Column(Numeric(20, 6, asdecimal=True))
    data3 = Column(Numeric(20, 6, asdecimal=True))
    data4 = Column(Numeric(20, 6, asdecimal=True))
    data5 = Column(Numeric(20, 6, asdecimal=True))
    data6 = Column(Numeric(20, 6, asdecimal=True))
    data7 = Column(Numeric(20, 6, asdecimal=True))
    data8 = Column(Numeric(20, 6, asdecimal=True))
    data9 = Column(Numeric(20, 6, asdecimal=True))
    data10 = Column(Numeric(20, 6, asdecimal=True))
    data11 = Column(Numeric(20, 6, asdecimal=True))
    data12 = Column(Numeric(20, 6, asdecimal=True))
    data13 = Column(Numeric(20, 6, asdecimal=True))
    data14 = Column(Numeric(20, 6, asdecimal=True))
    data15 = Column(Numeric(20, 6, asdecimal=True))
    data16 = Column(Numeric(20, 6, asdecimal=True))
    data17 = Column(Numeric(20, 6, asdecimal=True))
    data18 = Column(Numeric(20, 6, asdecimal=True))
    data19 = Column(Numeric(20, 6, asdecimal=True))
    data20 = Column(Numeric(20, 6, asdecimal=True))
    data21 = Column(Numeric(20, 6, asdecimal=True))
    data22 = Column(Numeric(20, 6, asdecimal=True))
    data23 = Column(Numeric(20, 6, asdecimal=True))
    data24 = Column(Numeric(20, 6, asdecimal=True))
    data25 = Column(Numeric(20, 6, asdecimal=True))
    data26 = Column(Numeric(20, 6, asdecimal=True))
    data27 = Column(Numeric(20, 6, asdecimal=True))
    data28 = Column(Numeric(20, 6, asdecimal=True))
    data29 = Column(Numeric(20, 6, asdecimal=True))
    data30 = Column(Numeric(20, 6, asdecimal=True))
    data31 = Column(Numeric(20, 6, asdecimal=True))
    data32 = Column(Numeric(20, 6, asdecimal=True))
    data33 = Column(Numeric(20, 6, asdecimal=True))
    data34 = Column(Numeric(20, 6, asdecimal=True))
    data35 = Column(Numeric(20, 6, asdecimal=True))
    data36 = Column(Numeric(20, 6, asdecimal=True))
    data37 = Column(Numeric(20, 6, asdecimal=True))
    data38 = Column(Numeric(20, 6, asdecimal=True))
    data39 = Column(Numeric(20, 6, asdecimal=True))


def createTable():
    """Create HistoricalRatesTable. """
    Base.metadata.create_all(bind=engine)


def createRecord(hrt):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        session.add(hrt)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()


def updateRecord(hrt):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        session.merge(hrt)
        session.commit()
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()


def getRecords(symbol):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        row = session.query(HistoricalRatesTable).filter(
            HistoricalRatesTable.symbol == symbol
        )

        return row
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()


def getUniqueRecord(symbol, date):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        row = (
            session.query(HistoricalRatesTable)
            .filter(HistoricalRatesTable.symbol == symbol)
            .filter(HistoricalRatesTable.date == date)
            .first()
        )

        return row
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()
