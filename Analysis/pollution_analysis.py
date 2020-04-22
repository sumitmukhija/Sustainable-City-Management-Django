"""
This file is a test file for creating and formatting of the Pollution Data in the CSV
Also, running the main function creates all the models. 
This file creates the models on the local machine which we have pushed to the working branch
This file is not useful while the project is running as model update takes place through pollution job
"""

import os
import requests
import pandas as pd
from datetime import datetime, timedelta

from dotenv import load_dotenv

from time_series_utils import TimeSeriesUtils

load_dotenv()

#boundary co-ordinates for Dublin
SOUTH_MOST = 53.2447
NORTH_MOST = 53.44193
EAST_MOST = -6.037327
WEST_MOST = -6.465722

class PollutionAnalysis:
    @staticmethod
    def get_city_sections(filename="CityClusters.csv"):
        try:
            contents = pd.read_csv("../static/data/csv/"+filename, encoding="ISO-8859-1")
            if contents is None:
                raise Exception(filename, "either empty or cannot be read.")
            sections = [tuple(x) for x in contents.values]
            return sections
        except FileNotFoundError:
            print(filename, "not found")

    @staticmethod
    def format_pollution_data_and_make_csv():
        #format date
        END_DATETIME = datetime.now() - timedelta(days=1)
        START_DATETIME = END_DATETIME - timedelta(days=28)
        END_DATETIME = datetime.strftime(END_DATETIME, "%Y-%m-%d %H:%M:%S")
        START_DATETIME = datetime.strftime(START_DATETIME, "%Y-%m-%d %H:%M:%S")
        END_DATETIME = END_DATETIME.replace(" ", "T")
        START_DATETIME = START_DATETIME.replace(" ", "T")

        df = pd.DataFrame(columns = ['DATETIME'])
        sections = PollutionAnalysis().get_city_sections()
        for section in sections:
            lat = section[0]
            lng = section[1]
            latlng = "{} {}".format(lat, lng)
            URL = os.getenv("BREEZOMETER_HISTORICAL_DATA_BASE_URL").format(lat, lng, os.getenv("BREEZOMETER_KEY"),
                        START_DATETIME, END_DATETIME)
            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()['data']
                datetime  = [record['datetime'] for record in data]
                aqi  = [record['indexes']['baqi']['aqi'] if record['data_available'] == True else 0 for record in data]
                df['DATETIME'] = pd.Series(datetime)
                df[latlng] = pd.Series(aqi)
                df[latlng] = df[latlng].replace(0, round(df[latlng].mean()))
                print(df)
            else:
                print("FAIL")
        df["DATETIME"] = pd.to_datetime(df["DATETIME"], format='%Y-%m-%d %H:%M:%S')
        df.to_csv(r'../static/data/csv/Pollution.csv', index = False) 

    @staticmethod
    def create_pollution_analysis_models():
        file_path = './static/data/csv/Pollution.csv'
        data = pd.read_csv(file_path)
        data.fillna(data.mean(), inplace=True)
        for location in data:
            if(location == 'DATETIME'):
                pass
            else:
                model_path = "./static/models/pollution/" + location
                # if not os.path.exists(model_path):
                #     os.makedirs(model_path)
                TimeSeriesUtils.create_model(data[location].values, model_path, 24)
                pred = TimeSeriesUtils.prediction(model_path, 24)

    @staticmethod
    def make_pollution_analysis_prediction(location):
        model_path = "./static/models/pollution/" + location
        pred = TimeSeriesUtils.prediction(model_path, 24)
        return pred


# if __name__ == '__main__':
#     PollutionAnalysis().format_pollution_data_and_make_csv()
    # PollutionAnalysis().create_pollution_analysis_models()
#     PollutionAnalysis().make_pollution_analysis_prediction()
