import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    # db.execute("DROP TABLE IF EXISTS books;")
    db.execute("CREATE TABLE IF NOT EXISTS books "
               "(isbn VARCHAR PRIMARY KEY , title VARCHAR NOT NULL , author VARCHAR NOT NULL , pubyear INT);")
    f = open("books.csv")

    reader = csv.reader(f)
    for isbn, title, author, pubyear in reader:
        db.execute("INSERT INTO books (isbn, title, author, pubyear) VALUES (:isbn, :title, :author, :pubyear)",
                   {
                       "isbn": isbn,
                       "title": title,
                       "author": author,
                       "pubyear": pubyear
                   })
    db.commit()


if __name__ == "__main__":
    main()
