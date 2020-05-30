# -*- coding: utf-8 -*-
from indicator import *
import time

print("COLORFUL mode:")
indic = Sindicator(ColorMode.COLORFUL)
indic.displayOK("This is a OK Demo!")
indic.displayFAIL("This is a FAILED Demo!")
indic.displayPASS("This a PASS Demo!")
indic.displayWARN("This is a WARN Demo!")
indic.displayPROG("This is a Progress Demo")
time.sleep(1)
n = 5
while n > 0:
    indic.updateStatus(Staus.INPROGRESS, "End in " + str(n) + " seconds")
    n -= 1
    time.sleep(1)
indic.updateStatus(Staus.OK, "Now Done!")

print("B&W mode:")
indicB = Sindicator(ColorMode.BW)
indicB.displayOK("This is a OK Demo!")
indicB.displayFAIL("This is a FAILED Demo!")
indicB.displayPASS("This a PASS Demo!")
indicB.displayWARN("This is a WARN Demo!")
indicB.displayPROG("This is a Progress Demo")
time.sleep(1)
n = 5
while n > 0:
    indicB.updateStatus(Staus.INPROGRESS, "End in " + str(n) + " seconds")
    n -= 1
    time.sleep(1)
indicB.updateStatus(Staus.OK, "Now Done!")
