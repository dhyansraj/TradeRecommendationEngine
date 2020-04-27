#!/bin/bash

source ~/my_env/bin/activate

python historical_data_manager.py 
# for file in daily_rates/*
# do
#     if [[ -f $file ]]; then
# 	filename=$(basename -- "$file")
# 	filename="${filename%.*}"
# 	result=$(curl -s -L http://127.0.0.1:5000/predict/$filename)
# 	echo $filename $(echo $result | jq -r '.date') $(echo $result | jq -r '.prediction')
#     fi
# done
