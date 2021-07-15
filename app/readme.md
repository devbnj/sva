pip3 install -r requirements.txt

flask run -h 0.0.0.0 -p 8080

CREATE TABLE user (
        id INTEGER NOT NULL, 
        email VARCHAR(100), 
        password VARCHAR(100), 
        name VARCHAR(1000), rigved text, 
        PRIMARY KEY (id), 
        UNIQUE (email)
);

create table vivek (id integer not null, sayings text);

#### sqlite3 
.tables -- list all tables
.schema -- list all schema and indices

'info@devb.com', '123456'

/usr/local/lib/python3.6/dist-packages/