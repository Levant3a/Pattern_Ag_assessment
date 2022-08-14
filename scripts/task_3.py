"""
Task: First compute the weighted average of horizontal layers for each
component (see formula below). Using your output, then compute the
weighted average of components for each map unit (using comppct).

Horizontal layer weights: abs(hzdept - hzdepb) / hzdepb

Desired data: soil attributes (om, cec, and ph) by mukey.
Please save as a csv file with the
following headers: mukey, mukey_geometry, om, cec, ph.
"""

import pandas as pd
import os

def get_root_path():
    """
    To get parent path for all the input and output
    maybe need to put this into a util py script
    :return:
    """
    path = os.path.abspath(os.getcwd())
    path = '/'.join(path.split('/')[:-1])
    return path


def read_in_soil_data():
    """
    To read in weather data
    maybe should have made a filtering function
    :return:
    """
    file_path = get_root_path() + '/inputs/soil.csv'
    weather_data = pd.read_csv(file_path)
    return weather_data

def get_horizontal_layer_weights(soil):
    """
    function to create Horizontal layer weights
    :param soil:
    :return:
    """
    soil['hlw'] = abs(soil['hzdept'] - soil['hzdepb']) / soil['hzdepb']
    return soil

def get_weighted_avg_of_comp(soil):
    """
    This function is to compute the weighted average of components for each map unit (using comppct).
    with the Horizontal layer weights(hlw).

    I am assuming that the function then is:
    comppct * om * hlw /100 for om
    comppct * cec * hlw /100 for cec
    comppct * ph * hlw /100 for ph
    the reason why im dividing 100 is because im assuming comppct is in pct form.
    :param soil:
    :return:
    """
    for col in ['om','cec','ph']:
        soil[col] = soil['comppct'] * soil[col] * soil['hlw']
    return soil[['mukey', 'mukey_geometry', 'om', 'cec', 'ph']]

def output_soil_data(soil):
    """
    To output target soil data
    """
    out_path = get_root_path() + f'/outputs/task_3.csv'
    soil.to_csv(out_path, index=False)


def task_3_process():
    """
    wrapper function to run task_3
    :return:
    """
    s = read_in_soil_data()
    s = get_horizontal_layer_weights(s)
    s = get_weighted_avg_of_comp(s)
    output_soil_data(s)
