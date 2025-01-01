import sqlite3

con = sqlite3.connect('kp.db')
db = con.cursor()

db.executescript("""
CREATE TABLE TB_PKEY (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (300),
    description TEXT (500),
    url TEXT (200),
    passtoken TEXT (300),
    date_audite DATATIME
);
                 
CREATE TABLE TB_user(
    UUID TEXT PRIMARY KEY,
    email VARCHAR(120),
    description TEXT (300)
    date_audite DATATIME    
);
""")

con.commit()
con.close()