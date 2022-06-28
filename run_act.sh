#!/bin/bash

. ./venv/bin/activate
cd BK_chatbot_20200821
nohup rasa run actions > ../log/act.log &