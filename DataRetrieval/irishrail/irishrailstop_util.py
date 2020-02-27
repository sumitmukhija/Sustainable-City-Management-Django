import pandas as pd

class IrishRailUtil():

    @staticmethod
    def get_irish_rail_stop_coordinates():
        try:
            stops = pd.read_csv("./static/data/csv/IrishRailStops.csv", encoding="ISO-8859-1")
        except FileNotFoundError:
            stops = None
            return stops
        return stops
