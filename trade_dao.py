from util import fromisoformat

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Numeric, desc
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
    data0 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data1 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data2 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data3 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data4 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data5 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data6 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data7 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data8 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data9 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data10 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data11 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data12 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data13 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data14 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data15 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data16 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data17 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data18 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data19 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data20 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data21 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data22 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data23 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data24 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data25 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data26 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data27 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data28 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data29 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data30 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data31 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data32 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data33 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data34 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data35 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data36 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data37 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data38 = Column(Numeric(15, 2, asdecimal=False), default=0.0)
    data39 = Column(Numeric(15, 2, asdecimal=False), default=0.0)


def create_table():
    """Create HistoricalRatesTable. """
    Base.metadata.create_all(bind=engine)


def create_record(hrt):
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


def update_record(hrt):
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


def get_records(symbol):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        row = (
            session.query(HistoricalRatesTable)
            .filter(HistoricalRatesTable.symbol == symbol)
            .order_by(HistoricalRatesTable.date.desc())
        )

        return row.all()
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()


def get_symbols_list():
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    try:
        row = (
            session.query(HistoricalRatesTable.symbol)
            .distinct(HistoricalRatesTable.symbol)
            .group_by(HistoricalRatesTable.symbol)
        )

        return row.all()
    except SQLAlchemyError as e:
        print(e)
    finally:
        session.close()


def get_unique_record(symbol, date):
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
