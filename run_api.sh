#!/bin/bash

. ./venv/bin/activate
nohup python main.py > log/api.log &