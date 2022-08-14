"""
Task: Extract the data from the year 2021 and then compute
the total (summed) precipitation and minimum, maximum, and mean
temperature observed over the year for each FIPS code. Using your output,
then map the provided fips_code to the correct field_id using the field_geometry given in
the crop.csv file. You may find the following code useful where the latitude and longitude can
be extracted from the center point of the field_geometry:

url = 'https://geo.fcc.gov/api/census/block/find?latitude=%s&longitude=%s&format=json' % (lat, lon)
response = requests.get(url)
data = response.json()
state = data['State']['FIPS']
county = data['County']['FIPS'][2:]


Desired data: total precipitation and minimum, maximum, and mean temperature by field for 2021.
Please save as a csv file with the following headers: field_id, precip, min_temp, max_temp, mean_temp.
"""

import pandas as pd
import os
import datetime
import task_1

def get_root_path():
    """
    To get parent path for all the input and output
    maybe need to put this into a util py script
    :return:
    """
    path = os.path.abspath(os.getcwd())
    path = '/'.join(path.split('/')[:-1])
    return path


def read_in_weather_data():
    """
    To read in weather data
    maybe should have made a filtering function
    :return:
    """
    file_path = get_root_path() + '/inputs/weather.csv'
    weather_data = pd.read_csv(file_path)
    return weather_data

def quick_data_filter(weather):
    """
    If I had more time i would ask user to filter what year
    :param weather: df
    :return:df filtered
    """
    return weather[weather['year'] ==2021]

def get_agg_req(weather):
    """
    function to do quick aggregation request
    :param weather:
    :return:
    """
    weather['max_temp'] = weather['temp']
    weather['mean_temp'] = weather['temp']
    weather = weather.groupby(['fips_code'],as_index=False).agg(
        {'precip':'sum','temp':'min','max_temp':'max','mean_temp':'mean'})
    weather.rename(columns={'temp':'min_temp'},inplace=True)
    return weather

def get_field_id(weather):
    """
    todo need to find way to read from url and pull
    :param weather:
    :return:
    """
    return weather

def write_out(weather):
    out_path = get_root_path() + f'/outputs/task_4.csv'
    weather.to_csv(out_path, index=False)

def task_4_process():
    w = read_in_weather_data()
    w = quick_data_filter(w)
    w = get_agg_req(w)
