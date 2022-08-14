"""
Task: First compute the normalized difference vegetation index
(NDVI; see formula below). Using your output, then find the peak-of-season
(POS; maximum value observed over the year) and date that the POS occurred.

NDVI formula: (nir – red) / (nir + red)

Desired data: POS value and date of POS (for NDVI) by tile for the year 2021.
Please save as a csv file with the following headers: tile_id, tile_geometry, pos, pos_date.
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


def read_in_spectral_data():
    """
    To read in spectral data
    maybe should have made a filtering function
    :return:
    """
    file_path = get_root_path() + '/inputs/spectral.csv'
    spectral_data = pd.read_csv(file_path)
    return spectral_data

def quick_data_process(spectral):
    """
    function to get the year since we are interested in the POS for the year
    :param spectral:
    :return:
    """
    spectral['year'] = spectral['date'].str[:4]
    return spectral

def get_nvdi(spectral):
    """
    function to calculate the NDVI
    :param spectral:
    :return:
    """
    spectral['ndvi'] = (spectral['nir'] - spectral['red']) / \
                       (spectral['nir'] + spectral['red'])
    return spectral


def get_pos(spectral):
    """
    Function to get the POS of the year by tile_id
    :param spectral:
    :return:
    """
    spectral['pos'] = spectral.groupby(['tile_id','year'], as_index=False)['ndvi'].transform(max)
    spectral = spectral[spectral['pos'] == spectral['ndvi']]
    return spectral

def output_spectral_data(spectral):
    """
    To output task 2 spectral data
    """
    out_path = get_root_path() + f'/outputs/task_2.csv'
    spectral.to_csv(out_path, index=False)


def task_2_process():
    """
   wrapper function to run task_3
   :return:
   """
    s = read_in_spectral_data()
    s = quick_data_process(s)
    s = get_nvdi(s)
    s = get_pos(s)
    output_spectral_data(s)
