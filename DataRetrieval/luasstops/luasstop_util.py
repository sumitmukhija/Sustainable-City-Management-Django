import pandas as pd

class LuasStopUtil():

    @staticmethod
    def get_luas_stop_coordinates():
        try:
            stops = pd.read_csv("./LuasStops.csv", encoding="ISO-8859-1")
        except FileNotFoundError:
            stops = None
            return stops
        return stops