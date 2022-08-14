"""
Task: Extract the data from the year 2021 from crop.csv

Desired data: crop type by field for the year 2021. Please save as a csv file with the following
headers: field_id, field_geometry, crop_type.
"""
import pandas as pd
import os

def get_root_path():
    """
    To get parent path for all the input and output
    :return:
    """
    path = os.path.abspath(os.getcwd())
    path = '/'.join(path.split('/')[:-1])
    return path


def read_in_crop_data():
    """
    To read in crop data and filter in this case 2021 data
    maybe should have made a filtering function
    :return:
    """
    file_path = get_root_path() + '/inputs/crop.csv'
    crop_data = pd.read_csv(file_path)
    inp = input("Would you like to filter the data by year? [Y/N]: ")
    if inp.upper() in ['Y','YES']:
        inp = input("What year would you like?: ")
        year_filter = int(inp)
        crop_filtered = crop_data[crop_data['year']==year_filter].copy()
        crop_filtered = crop_filtered.drop(['year'], axis=1)
        return crop_filtered, year_filter
    return crop_data, ''

def output_crop_data(crop, year):
    """
    To read output target crop data
    """
    if year != '':
        file_name = f'crop_{year}.csv'
    else:
        file_name = f'crop.csv'
    out_path = get_root_path() + f'/outputs/{file_name}'
    crop.to_csv(out_path, index= False)

def task_1_process():
    """
    wrapper function to read in crop data and write out target crop data
    """
    crop_df, yr_filter = read_in_crop_data()
    output_crop_data(crop_df, yr_filter)