#!/bin/bash

. ./venv/bin/activate
cd BK_chatbot_20200821
export RASA_X_PASSWORD=cuscsoft
nohup rasa x > ../log/rasax.log &