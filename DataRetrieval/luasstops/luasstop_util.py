import pandas as pd
import datetime

class LuasStopUtil():

    @staticmethod
    def get_luas_stop_coordinates():
        try:
            stops = pd.read_csv("./static/data/csv/LuasStops.csv", encoding="ISO-8859-1")
        except FileNotFoundError:
            stops = None
            return stops
        return stops

    @staticmethod
    def format_data(data):
        timestamp = str(datetime.datetime.now())
        formatted_data = []
        for s in range(data.shape[0]):
            records = {
                "StopID": data.iloc[s, 0],
                "StopName": data.iloc[s, 1],
                "lat": data.iloc[s, 2],
                "long": data.iloc[s, 3],
                "timestamp": timestamp
            }
            formatted_data.append(records)
        return formatted_data