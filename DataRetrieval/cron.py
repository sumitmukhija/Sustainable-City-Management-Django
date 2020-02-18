import kronos
from DataRetrieval.pollution import pollution_job
from DataRetrieval.bike import bikes_job
from DataRetrieval.traffic import traffic_job

@kronos.register('* * * * *')
def execute_pollution_job():
    pollution_job.PollutionJob().exec()

@kronos.register('* * * * *')
def execute_bikes_job():
    bikes_job.BikeJob().exec()

@kronos.register('* * * * *')
def execute_traffic_job():
    traffic_job.TrafficJob().exec()