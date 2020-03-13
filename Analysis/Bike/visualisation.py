import os
import pandas as pd
import matplotlib.pyplot as plt


class Visualisation:
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
                # new_file = pd.read_csv(file_path, encoding='utf-8')
                new_file = pd.read_csv(file_path, encoding='utf-8')
                new_file = new_file.iloc[::5, :]
                new_file.rename(columns={"Unnamed: 0": "DATETIME"}, inplace=True)
                new_file["DATETIME"] = file[6:16] + " " + new_file["DATETIME"]
                new_file["DATETIME"] = pd.to_datetime(new_file["DATETIME"], format='%Y-%m-%d %H:%M:%S')
                bikes = pd.concat([bikes, new_file])
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
        series = data.loc[0:1000, [x, y]]
        series.plot()
        plt.show()


if __name__ == '__main__':
    folder_path = '/Users/Dhruv/Downloads/bikeData2'
    write_file_path = '/Users/dhruv/Projects/sustainable-city-management/Sustainable-City-Management-Django/static/data/csv/BikesHistData2.csv'
    Visualisation().combine_files(folder_path, write_file_path)
    # file_path = '/Users/Dhruv/Downloads/bikes_2017-01-24.csv'
    # file_path = '/Users/dhruv/Projects/sustainable-city-management/Sustainable-City-Management-Django/static/data/csv/BikesHistData.csv'
    # data = pd.read_csv(file_path)
    # Visualisation().visualise_time_series(data, 'GRAND_CANAL_DOCK', 'DATETIME')
    # Visualisation().visualise_time_series(data, 'HIGH_STREET', 'DATETIME')
