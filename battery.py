#!/usr/bin/env python3
import psutil

def print_battery_status(battery):
    percent = round(battery.percent)
    if battery.power_plugged:
        icon = '\uf0e7'
    elif percent >= 80:
        icon = '\uf240'
    elif percent >= 60:
        icon = '\uf241'
    elif percent >= 40:
        icon = '\uf242'
    elif percent >= 15:
        icon = '\uf243'
    else:
        icon = '\uf244'
    print(f"<span font='Font Awesome'>{icon} {percent}%</span>")   

def main():
    battery = psutil.sensors_battery()
    print_battery_status(battery)
    print_battery_status(battery)

if __name__ == "__main__":
     main()   