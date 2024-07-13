#!/bin/bash
for file in /dev/input/event*; do echo "$file $(cat /sys/class/input/${file##*/}/device/name)"; done