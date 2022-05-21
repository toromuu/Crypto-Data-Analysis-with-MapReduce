#!/usr/bin/bash

python ../make_custom_dataset.py ../datasets_urls.txt
cat custom_dataset.txt | python mapper.py | sort -k 1,1 | python reducer.py