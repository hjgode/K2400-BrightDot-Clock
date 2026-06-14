# K2400-BrightDot-Clock
Firmware for the BrightDot Clock K2400

The firmware uses the following libraries:

- [Neopixelbus](https://github.com/Makuna/NeoPixelBus)
- [ESPAsyncWebServer](https://github.com/me-no-dev/ESPAsyncWebServer)
- [ESPAsyncTCP](https://github.com/me-no-dev/AsyncTCP)
- [ArduinoJson](https://github.com/bblanchon/ArduinoJson)

If you replace another same device, you may find the following save/restore options useful:

Get settings (json):

    curl -x POST -H "Content-Type: application/text" http://<ip-adress>/data

Response (json):
    {"brightness":161,"hourRed":255,"hourGreen":0,"hourBlue":0,"minuteRed":0,"minuteGreen":255,"minuteBlue":0,"secondRed":0,"secondGreen":0,"secondBlue":255,"pendRed":0,"pendGreen":0,"pendBlue":0,"minRed":0,"minGreen":0,"minBlue":0,"quarterRed":216,"quarterGreen":215,"quarterBlue":215,"mode":1,"invert":0,"hour":"14","min":"15","sec":"16","NTP":"ptbtime1.ptb.de","GMT":1,"DST":1,"devicename":"K2400","alarmOn":0,"minAlarm":0,"hourAlarm":0,"dimOn":1,"hourStartDim":17,"hourStopDim":8,"valueDim":37}

To apply all color settings use:

    curl -X POST -d 'brightness=60&hourRed=255&hourGreen=0&hourBlue=0&minuteRed=0&minuteGreen=255&minuteBlue=0&secondRed=0&secondGreen=0&secondBlue=255&pendRed=0&pendGreen=0&pendBlue=0&minRed=0&minGreen=0&minBlue=0&quarterRed=216&quarterGreen=215&quarterBlue=215&mode=1&invert=0' http://<ip-adress>/colorsave

This a GET syntax. The Response is as above the full json settings.

Set NTP settings:

    curl -X POST -d 'gmtOffsetHour=<float>&NTPData=<float>&NTPString=<string>[&NTPTZString=<string>]' http://<ip-adress>/ntpsave
    
NTPTZString is optinal.

DimSave

    curl -X POST -d 'dimOn=<0|1>&hourStartDim=<int>&hourStopDim=<int>&valueDim=<int>' http://<ip-adress>/dimsave

Restart K2400 Clock:

    curl -X POST http://<ip-adress>/globalrestart

