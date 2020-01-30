import kronos
import random
from DataRetrieval.pollution import pollution_job
from DataRetrieval.bike import bikes_job

@kronos.register('* * * * *')
def execute_pollution_job():
    pollution_job.PollutionJob().exec()

@kronos.register('* * * * *')
def execute_bikes_job():
    bikes_job.BikeJob().exec()