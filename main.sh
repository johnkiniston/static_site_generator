#!/bin/bash

# 1. Run the Python generation process
python3 src/main.py

# 2. Change directory into public AND start the server on port 8888
cd public && python3 -m http.server 8888
