# read params
# process
# return dataframe

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path, 'r') as f:
        config=yaml.safe_load(f)
    return config


def get_data(config):
    config=read_params(config_path=config)
    data_path=config['data_source']['s3_source']
    df=pd.read_csv(data_path)
    return df




if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    parsed_args=args.parse_args()

    get_data(config=parsed_args.config)

