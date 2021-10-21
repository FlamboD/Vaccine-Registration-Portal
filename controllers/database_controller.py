import sqlite3


class DatabaseController:
    PATH = "/../database/VaccineRegistration.db"

    @classmethod
    def create(cls):
        print(cls.PATH)
        conn = sqlite3.connect(cls.PATH)
        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS gender
            (
                [gender] TEXT PRIMARY KEY
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS contact_details
            (
                [id] INTEGER PRIMARY KEY,
                [email] TEXT,
                [phone_number] TEXT
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS location
            (
                [id] INTEGER PRIMARY KEY,
                [province] TEXT NOT NULL,
                [municipality] TEXT NOT NULL,
                [address] TEXT
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS vaccine_time_preference
            (
                [id] INTEGER PRIMARY KEY,
                [weekday] INTEGER NOT NULL,
                [morning] INTEGER NOT NULL
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS medical_aid
            (
                [id] INTEGER PRIMARY KEY,
                [scheme_name] TEXT NOT NULL,
                [number] TEXT NOT NULL
            )
            """
        )
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS user
            (
                [id_number] INTEGER PRIMARY KEY,
                [first_names] TEXT,
                [surname] TEXT,
                [passport_number] TEXT,
                [gender] TEXT,
                [contact_details] INTEGER,
                [location] INTEGER,
                [vaccine_time_preference] INTEGER,
                [medical_aid] INTEGER,
                FOREIGN KEY(gender) REFERENCES gender(gender),
                FOREIGN KEY(contact_details) REFERENCES contact_details(id),
                FOREIGN KEY(location) REFERENCES location(id),
                FOREIGN KEY(vaccine_time_preference) REFERENCES vaccine_time_preference(id),
                FOREIGN KEY(medical_aid) REFERENCES medical_aid(id),\
            )
            """
        )
        conn.commit()
        conn.close()

    @classmethod
    def connect(cls):
        cls.create()
        conn = sqlite3.connect(cls.PATH)
