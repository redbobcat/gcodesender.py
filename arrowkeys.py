from msvcrt import getch
import sys, os
import time

magnitude = 50
speed = 2000

xCount = 3
xCountTemp = xCount

yCount = 3
yCountTemp = yCount

while True:
    key = ord(getch())
    # print(key)
    if key == 27: #ESC
        break
    elif key == 119:
        print("W")
        os.system("sendRunner.sh 'G1 X110Y"+str(magnitude)+" F"+str(speed)+"'")
    elif key == 97:
        print("A")
        os.system("sendRunner.sh 'G1 X"+str(110+magnitude)+"Y0 F"+str(speed)+"'")
    elif key == 115:
        print("S")
        os.system("sendRunner.sh 'G1 X110Y"+str(magnitude*-1)+" F"+str(speed)+"'")
    elif key == 100:
        print("D")
        os.system("sendRunner.sh 'G1 X"+str(110+magnitude*-1)+"Y0 F"+str(speed)+"'")
    elif key == 13: #Enter
        print("enter")
        if xCountTemp > 0:
            os.system("sendRunner.sh 'G1 X"+str(110+magnitude*-1)+"Y0 F"+str(speed)+"'")
            xCountTemp -= 1
        elif yCountTemp > 0:
            xCountTemp = xCount
            os.system("sendRunner.sh 'G1 X"+str(110+magnitude*xCount)+"Y0 F"+str(speed)+"'")
            time.sleep(10)
            os.system("sendRunner.sh 'G1 X110Y"+str(magnitude*-1)+" F"+str(speed)+"'")
            yCountTemp -= 1
        else:
            os.system("sendRunner.sh 'G1 X"+str(110+magnitude*xCount)+"Y0 F"+str(speed)+"'")
            time.sleep(10)
            os.system("sendRunner.sh 'G1 X110Y"+str(magnitude*-1)+" F"+str(speed)+"'")