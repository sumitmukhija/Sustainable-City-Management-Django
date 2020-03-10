import pandas as pd

class BusStopUtil():

    @staticmethod
    def get_bus_stop_coordinates():
        try:
            stops = pd.read_csv("./static/data/csv/DublinBusStops.csv", encoding="ISO-8859-1")
        except FileNotFoundError:
            stops = None
            return stops
        return stops
