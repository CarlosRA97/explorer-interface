#!/usr/bin/env python

from subprocess import call, Popen
from platform import system


def scanWifi():
    proc = Popen(['iwlist' ,'wlan0' ,'scan'], stdout=subprocess.PIPE)
    tmp = proc.stdout.read()

    for line in tmp.splitlines():
        if "ESSID:" in line:
            print(line)

    ask = raw_input("Se quiere conectar a alguna wifi?: ( s | n ): ")
    if str(ask) == "s":
        connectWifi()
    else:
        exit()

def connectWifi():
    ssid = raw_input("Introduce el nombre de tu wifi: ")
    passwd = raw_input("Introduce la contrasena de tu wifi: ")
    cfile = "/etc/wpa_supplicant/wpa_supplicant.conf"
    doc = '\n\nnetwork={{\n\tssid="{0:s}"\n\tpsk="{1:s}"\n}}'.format(ssid, passwd)

    with open(cfile,'a+') as f:
        f.write(doc)

def restartWifi():
    call(['sudo','ifdown','wlan0'])
    call(['sudo','ifup','wlan0'])

if system() == "Linux":
    scanWifi()
    call(['ifconfig','wlan0'])
else:
    print("Este script solo funciona en Linux")