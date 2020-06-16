# -*- coding: utf-8 -*-
# indicator.py
# based on python 3.6+
"""\
This module is a simple status indicator which liked systemd initialization style
We provide four styles of status include OK/FAILED/PASS/WARN/InProgress and also
support black&white style mode for some old console like Windows 7‘s cmd you can
watch the demo at github page.
(https://github.com/bleach103/SystemdLike-CLI-StatusIndicator/tree/master)
This module followed  License
"""

import sys
import time
import threading
from enum import Enum


class ColorMode(Enum):
    BW = 0
    COLORFUL = 1


class Staus(Enum):
    OK = 200
    FAILED = 500
    PASS = 202
    WARN = 203
    INPROGRESS = 100


class Sindicator(object):

    def __init__(self, colormode):
        self.__lastMsgLen = 0
        self.__currentMsg = ""
        self.__updater = None
        self.__endFlag = True
        self.__colormode = colormode

    def __printMsg(self, msg):
        sys.stdout.write(msg)
        if len(msg) < self.__lastMsgLen:
            numOfSpace = self.__lastMsgLen - len(msg)
            for i in range(numOfSpace):
                sys.stdout.write(" ")

    def displayOK(self, msg):
        sys.stdout.write("\r")
        sys.stdout.write("[  ")
        if self.__colormode == ColorMode.COLORFUL:
            sys.stdout.write("\033[1;32mOK\033[0m")
        elif self.__colormode == ColorMode.BW:
            sys.stdout.write("OK")
        sys.stdout.write("  ] ")
        self.__printMsg(msg)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def displayFAIL(self, msg):
        sys.stdout.write("\r")
        sys.stdout.write("[")
        if self.__colormode == ColorMode.COLORFUL:
            sys.stdout.write("\033[1;31mFAILED\033[0m")
        elif self.__colormode == ColorMode.BW:
            sys.stdout.write("FAILED")
        sys.stdout.write("] ")
        self.__printMsg(msg)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def displayWARN(self, msg):
        sys.stdout.write("\r")
        sys.stdout.write("[ ")
        if self.__colormode == ColorMode.COLORFUL:
            sys.stdout.write("\033[1;33mWARN\033[0m")
        elif self.__colormode == ColorMode.BW:
            sys.stdout.write("WARN")
        sys.stdout.write(" ] ")
        self.__printMsg(msg)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def displayPASS(self, msg):
        sys.stdout.write("\r")
        sys.stdout.write("[ ")
        if self.__colormode == ColorMode.COLORFUL:
            sys.stdout.write("\033[1;33mPASS\033[0m")
        elif self.__colormode == ColorMode.BW:
            sys.stdout.write("PASS")
        sys.stdout.write(" ] ")
        self.__printMsg(msg)
        sys.stdout.write("\n")
        sys.stdout.flush()

    def displayPROG(self, msg):
        self.__endFlag = False
        self.__currentMsg = msg
        self.__updater = threading.Thread(target=self.__progUpdater, name='prog_updater')
        self.__updater.start()

    def __progUpdater(self):
        step = 0
        while True:
            sys.stdout.write("\r")
            sys.stdout.write("[ ")
            if self.__colormode == ColorMode.COLORFUL:
                if step == 0:
                    sys.stdout.write("\033[1;37m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                elif step == 1:
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[1;37m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                elif step == 2:
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[1;37m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                elif step == 3:
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[0;31m*\033[0m")
                    sys.stdout.write("\033[1;37m*\033[0m")
            elif self.__colormode == ColorMode.BW:
                if step == 0:
                    sys.stdout.write("*")
                    sys.stdout.write(" ")
                    sys.stdout.write(" ")
                    sys.stdout.write(" ")
                elif step == 1:
                    sys.stdout.write(" ")
                    sys.stdout.write("*")
                    sys.stdout.write(" ")
                    sys.stdout.write(" ")
                elif step == 2:
                    sys.stdout.write(" ")
                    sys.stdout.write(" ")
                    sys.stdout.write("*")
                    sys.stdout.write(" ")
                elif step == 3:
                    sys.stdout.write(" ")
                    sys.stdout.write(" ")
                    sys.stdout.write(" ")
                    sys.stdout.write("*")
            sys.stdout.write(" ] ")
            self.__printMsg(self.__currentMsg)
            sys.stdout.flush()
            if self.__endFlag:
                break
            time.sleep(0.25)
            if step == 3:
                step = 0
            else:
                step += 1

    def __endPROG(self):
        self.__endFlag = True
        if self.__updater is not None:
            self.__updater.join()
            self.__updater = None

    def updateStatus(self, status=Staus.INPROGRESS, msg=""):

        if msg != "":
            self.__lastMsgLen = len(self.__currentMsg)
            self.__currentMsg = msg

        if self.__updater is None:
            if msg != "":
                self.displayPROG(msg)

        if status == Staus.OK:
            self.__endPROG()
            self.displayOK(self.__currentMsg)
        elif status == Staus.FAILED:
            self.__endPROG()
            self.displayFAIL(self.__currentMsg)
        elif status == Staus.PASS:
            self.__endPROG()
            self.displayPASS(self.__currentMsg)
        elif status == Staus.WARN:
            self.__endPROG()
            self.displayWARN(self.__currentMsg)
        elif status == Staus.INPROGRESS:
            pass
