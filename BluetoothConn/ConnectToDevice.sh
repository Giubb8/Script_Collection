#!/bin/bash

# Indirizzo del dispositivo Bluetooth
device_address="74:A7:EA:FB:4B:30"

# Connetti al dispositivo
echo -e "connect $device_address\nquit" | bluetoothctl
