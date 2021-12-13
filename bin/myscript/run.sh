#!/bin/bash

#compile
arduino-cli compile -fqbn arduino:avr:mega ./$1
killall putty

#upload
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega ./$1
