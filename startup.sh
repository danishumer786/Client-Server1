#!/bin/bash
# Azure startup script
cd /home/site/wwwroot
export FRONTEND_URL=${FRONTEND_URL:-"http://localhost:3000"}
python app.py