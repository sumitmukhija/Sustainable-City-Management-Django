from DataRetrieval import cron_job
from DataRetrieval.luasstops import luasstop_util
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils
import requests
import json

class LuasJob(cron_job.CronJob):

    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        url = Environ().get_base_luas_stop_url()
        stops = luasstop_util.LuasStopUtil().get_luas_stop_coordinates()
        if (stops is not None):
            data = luasstop_util.LuasStopUtil.format_data(stops)
            response = requests.post(url, json={"data": json.dumps(data)}, headers=headers)
        else:
            pass
