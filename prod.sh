#!/bin/bash -x

# sencible params for production (recording talks) 

./dvs-mon.py -c dvswitch.py \
    source_fw.py \
    source_remote_fw.py \
    sink_find_dir.py \
    sink_ffplay.py 
