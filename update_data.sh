#!/bin/bash

source ~/my_env/bin/activate

rm -f last_run.log 
python historical_data_manager.py 
