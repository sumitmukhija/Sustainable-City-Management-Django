import numpy as np
import copy
import os
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.ar_model import ARResults


class TimeSeriesUtils:
    """
    Class contains functions used to create and time series forecasting models
    """

    # Default size of window in the forecasting model
    WINDOW_SIZE = 504

    # create a difference transform of the dataset
    @staticmethod
    def difference(dataset):
        diff = list()
        for i in range(1, len(dataset)):
            value = dataset[i] - dataset[i - 1]
            diff.append(value)
        return np.array(diff)

    @staticmethod
    def predict(coef, history):
        """
        Make a prediction give regression coefficients and lag obs
        :param coef: coefficients for time series forecasting model
        :param history: historical data
        :return: next one prediction
        """
        yhat = coef[0]
        for i in range(1, len(coef)):
            yhat += coef[i] * history[-i]
        return yhat

    @staticmethod
    def predict_n(coef, hist, n):
        """
        Make the next n predictions
        :param coef: coefficients for time series forecasting model
        :param hist: historical data
        :param n: number of predictions
        :return: next n predictions
        """
        predictions = list()
        history = list(copy.copy(hist))
        for t in range(n):
            yhat = TimeSeriesUtils.predict(coef, history)
            predictions.append(yhat)
            history.append(yhat)
        return predictions

    @staticmethod
    def addition(dataset, start_val):
        sum = list()
        init_val = start_val + dataset[0]
        sum.append(init_val)
        for i in range(1, len(dataset)):
            value = dataset[i] + sum[-1]
            sum.append(value)
        return sum

    @staticmethod
    def save_model(diff, series, path, window_size=WINDOW_SIZE):
        """
        Save model to disk
        :param diff: difference of series
        :param series: original series.
        :param path:
        :param window_size:
        :return:
        """
        # fit model
        model = AR(diff)
        model_fit = model.fit(maxlag=window_size, disp=False)
        # save coefficients
        coef = model_fit.params
        np.save(path + '/man_model.npy', coef)
        # save lag
        lag = diff[-window_size:]
        np.save(path + '/man_data.npy', lag)
        # save the last ob
        np.save(path + '/man_obs.npy', [series[-1]])

    @staticmethod
    def create_model(series, path, window_size=WINDOW_SIZE):
        """
        Creates time series forecasting model
        :param series: the series for which the model is to be created.
        :param path: folder path of the model and associated numpy files.
        :param window_size: window size in the forecasting model.
        :return:
        """
        os.mkdir(path)
        X = TimeSeriesUtils.difference(series)
        TimeSeriesUtils.save_model(X, series, path, window_size)

    @staticmethod
    def update_model(series, path, window_size=WINDOW_SIZE, replace=False):
        """
        Update model and associated files for this particular series.
        :param series: new entries in historical data
        :param path: folder path of the model and associated numpy files
        :param window_size: window size in the forecasting model.
        :param replace: if true, the model historical data will be replaced, otherwise appended.
        :return:
        """
        """
        TODO: fix/test Code to update model
        update series into the model instead of just one observation
        """
        observation = 48
        data = np.load('ar_data.npy')
        last_ob = np.load('ar_obs.npy')
        # update and save differenced observation
        diffed = observation - last_ob[0]
        data = np.append(data, [diffed], axis=0)
        np.save('ar_data.npy', data)
        # update and save real observation
        last_ob[0] = observation
        np.save('ar_obs.npy', last_ob)

    @staticmethod
    def prediction(path, n):
        """
        Generate predictions for a particular model
        :param path: folder path of the model related info
        :param n: number of predictions
        :return: next n predictions
        """
        coef = np.load(path + '/man_model.npy')
        lag = np.load(path + '/man_data.npy')
        last_ob = np.load(path + '/man_obs.npy')
        # make prediction
        predictions = TimeSeriesUtils.predict_n(coef, lag, n)
        # transform prediction
        final_predictions = TimeSeriesUtils.addition(predictions, last_ob[0])
        return final_predictions
