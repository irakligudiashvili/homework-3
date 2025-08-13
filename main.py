from app import App
from db import MySQLDatabase
from config import Config


def main():
    app = App(
        Config.db_host,
        Config.db_user,
        Config.db_password,
        Config.db_name,
        MySQLDatabase()
    )

    app.run()


if __name__ == "__main__":
    main()
