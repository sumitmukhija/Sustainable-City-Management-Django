"""
This file is a test file for changing the format of the Bike Data in the CSV
Also, running the main function creates all the models. 
This file creates the models on the local machine which we have pushed to the working branch
This file is not useful while the project is running as model update takes place through bike job
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

from time_series_utils import TimeSeriesUtils

def exponential_smoothing(series, alpha):
    result = [series[0]]  # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n - 1])
    return result


def plot_exponential_smoothing(series, alphas):
    plt.figure(figsize=(17, 8))
    for alpha in alphas:
        plt.plot(exponential_smoothing(series, alpha), label="Alpha {}".format(alpha))
    plt.plot(series.values, "c", label="Actual")
    plt.legend(loc="best")
    plt.axis('tight')
    plt.title("Exponential Smoothing")
    plt.grid(True)
    plt.show()


class BikeAnalysis:
    @staticmethod
    def combine_files(folder_path, write_file_path):
        """
        go through all the files and combine them with additional column datetime
        :return:
        """
        bikes = pd.DataFrame()
        for file in os.listdir(folder_path):
            if 'bikes' in file:
                file_path = folder_path + '/' + file
                new_file = pd.read_csv(file_path, encoding='utf-8')
                new_file = new_file.iloc[::5, :]
                new_file.rename(columns={"Unnamed: 0": "DATETIME"}, inplace=True)
                new_file["DATETIME"] = file[6:16] + " " + new_file["DATETIME"]
                new_file["DATETIME"] = pd.to_datetime(new_file["DATETIME"], format='%Y-%m-%d %H:%M:%S')
                bikes = pd.concat([bikes, new_file])
        bikes.sort_values(by=["DATETIME"], inplace=True)
        bikes.to_csv(write_file_path, index=False)

    @staticmethod
    def visualise_time_series(data, x, y):
        """
        view time series graphs. Data will have
        :param data: pandas dataframe
        :param x: field on x-axis
        :param y: field on y-axis
        :return: view graph
        """
        series = data.loc[5000:10000, [x, y]]
        series.plot()
        plt.show()


if __name__ == '__main__':
    file_path = './static/data/csv/BikesHistData30.csv'
    data = pd.read_csv(file_path)
    data.fillna(data.mean(), inplace=True)
    for stop in data:
        if(stop == 'DATETIME'):
            pass
        else:
            model_path = "./static/models/bikes/" + stop
            if(stop == "PRINCES STREET / O'CONNELL STREET"):
                model_path = "./static/models/bikes/PRINCES STREET - O'CONNELL STREET"
            TimeSeriesUtils.create_model(data[stop].values, model_path)
            pred = TimeSeriesUtils.prediction(model_path, 20)
    
    
    
