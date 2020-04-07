import requests
from SCMBackend.env import Environ
import json

class TimetableDataInteractions():
    def get_busstop_timetable(self, stopid):
        params = {'stopid': stopid}
        timetable = requests.get(url=Environ().get_base_bus_stop_tt_url(), params=params)
        return timetable.text
