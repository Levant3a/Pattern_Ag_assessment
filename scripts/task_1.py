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
    return crop_data


def quick_filter(crop):
    """
    used to filter crop data for year user input wants
    :param crop:
    :return:
    """
    inp = input("Would you like to filter the data by year? [Y/N]: ")
    if inp.upper() in ['Y', 'YES']:
        inp = input("What year would you like?: ")
        year_filter = int(inp)
        crop_filtered = crop[crop['year'] == year_filter].copy()
        crop_filtered = crop_filtered.drop(['year'], axis=1)
    else:
        print("Im going to filter for 2021 anyways")
        crop_filtered = crop[crop['year'] == 2021].copy()
        crop_filtered = crop_filtered.drop(['year'], axis=1)
    return crop_filtered


def output_crop_data(crop):
    """
    To output target crop data
    """
    out_path = get_root_path() + f'/outputs/task_1.csv'
    crop.to_csv(out_path, index= False)


def task_1_process():
    """
    wrapper function to read in crop data and write out target crop data
    """
    crop_df = read_in_crop_data()
    crop_df = quick_filter(crop_df)
    output_crop_data(crop_df)
    return crop_df