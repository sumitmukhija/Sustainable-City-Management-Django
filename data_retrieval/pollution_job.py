from . import cron_job
from . import pollution_util as pol

class PollutionJob(cron_job.CronJob):

    def run_job(self):
        sections = pol.get_city_sections()
        responses = [pol.get_geo_pollution_data(section[0], section[1]) for section in sections]
        print(responses)
    
