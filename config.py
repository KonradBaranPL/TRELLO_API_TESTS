import os

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("TRELLO_API_KEY")

API_TOKEN = os.getenv("TRELLO_API_TOKEN")

BASE_URL = "https://api.trello.com/1/"