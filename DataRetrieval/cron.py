import kronos
import random
from DataRetrieval.pollution import pollution_job

@kronos.register('* * * * *')
def execute_pollution_job():
    pollution_job.PollutionJob().exec()
