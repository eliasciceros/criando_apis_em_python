from os import getenv


DB_URL = getenv("DB_URL", "sqlite:///requests.db")
