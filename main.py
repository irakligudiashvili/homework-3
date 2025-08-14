from app import App
from db import MySQLDatabase


def main():
    app = App(MySQLDatabase())

    app.run()


if __name__ == "__main__":
    main()
