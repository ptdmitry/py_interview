from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Goods

path_db = 'database.sqlite3'


class Repository:

    def __init__(self, path_db):
        self.engine = create_engine(fr'sqlite:///{path_db}?check_same_thread=False')
        self.session = self.get_session()
        self.session.execute('PRAGMA foreign_keys=ON')
        self.create_base()

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def create_base(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    rep = Repository(path_db)
    print(Base.metadata.tables.keys())
    print(Goods.__table__.columns.keys())
