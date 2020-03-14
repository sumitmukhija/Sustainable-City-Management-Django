import kronos
from DataRetrieval.pollution import pollution_job
from DataRetrieval.bike import bikes_job
from DataRetrieval.traffic import traffic_job
from DataRetrieval.busstops import busstop_job
from DataRetrieval.irishrail import irishrailstop_job
from DataRetrieval.luasstops import luasstop_job

@kronos.register('* * * * *')
def execute_pollution_job():
    pollution_job.PollutionJob().exec()

@kronos.register('* * * * *')
def execute_bikes_job():
    bikes_job.BikeJob().exec()

@kronos.register('* * * * *')
def execute_traffic_job():
    traffic_job.TrafficJob().exec()

@kronos.register('* * * * *')
def execute_irishrail_job():
    irishrailstop_job.IrishRailJob().exec()

@kronos.register('* * * * *')
def execute_bikestop_job():
    busstop_job.BusJob().exec()

@kronos.register('* * * * *')
def execute_luasstop_job():
    luasstop_job.LuasJob().exec()