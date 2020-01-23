import kronos
import random
from data_retrieval.pollution import pollution_job

@kronos.register('* * * * *')
def execute_pollution_job():
    pollution_job.PollutionJob().exec()