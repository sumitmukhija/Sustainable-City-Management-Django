import pandas as pd

class BusStopUtil():

    @staticmethod
    def get_bus_stop_coordinates():
        try:
            stops = pd.read_csv("./DublinBusStops.csv")
        except FileNotFoundError:
            return "Bus Stop Data Unavailable"
        return stops