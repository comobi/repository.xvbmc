#!/bin/sh

cp -rav /storage/.kodi/addons/script.xvbmc.update/resources/data/SettingsSystemInfo-turbo.xml /storage/.kodi/addons/skin.nox4beginners/1080i/SettingsSystemInfo.xml

mount -o remount,rw /flash/
cp -rav /storage/.kodi/addons/script.xvbmc.update/resources/data/config-turbo.txt /flash/config.txt
 
kodi-send -a "Notification(XvBMC NL Turbo-overclock Pi,FINISHED! PLEASE REBOOT...,4000,special://home/addons/script.xvbmc.update/icon.png)"
 
sleep 1
# reboot
