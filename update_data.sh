#!/bin/bash

source ~/my_env/bin/activate

rm -f last_run.log
P=$(hostname);
N=${P:4}
python historical_data_manager.py $N
				    
