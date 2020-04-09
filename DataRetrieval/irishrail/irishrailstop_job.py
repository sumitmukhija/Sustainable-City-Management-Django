from DataRetrieval import cron_job
from DataRetrieval.irishrail import irishrailstop_util
from SCMBackend.env import Environ
from DataInteractions.test_utils import TestUtils
import requests
import json
import datetime

class IrishRailJob(cron_job.CronJob):

    def run_job(self):
        headers = {"Authorization": TestUtils().get_valid_auth()}
        url = Environ().get_base_irish_rail_stop_url()
        stops = irishrailstop_util.IrishRailUtil().get_irish_rail_stop_coordinates()
        if (stops is not None):
            data = irishrailstop_util.IrishRailUtil.format_data(stops)
            response = requests.post(url, json={"data": json.dumps(data)}, headers=headers)