#!/bin/bash
pip install -r requirements.txt
while true; do
  pip install chatterbot==1.0.2
  python3 main.py
  sleep 5
done
