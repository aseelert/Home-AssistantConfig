#!/bin/bash

cd /home/pi/.homeassistant
source /home/pi/homeassistant/bin/activate
hass --script check_config

git add .
git status
git commit -am "Daily commit `date`"
git push origin master

exit
