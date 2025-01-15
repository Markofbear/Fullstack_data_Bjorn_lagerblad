from backend.connect_to_api import ResRobot
from pprint import pprint

resrobot = ResRobot()
pprint(resrobot.access_id_from_location("onsala"))