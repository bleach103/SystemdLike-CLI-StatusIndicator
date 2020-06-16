# SyetemdLike-CLI-StatusIndicator
This module is a simple status indicator which liked systemd initialization style
We provide four styles of status include OK/FAILED/PASS/WARN/InProgress.<br>
![image](asset/color.png)<br>
also support black&white style mode for some old console like Windows 7‘s cmd<br>
![image](asset/B&W.png)<br>

## Usage
You can watch the demo.py for example
```python
#Copy the indicator.py to your project
#and import the module like this

from indicator import *

#Create an indicator under colorful mode
indicator = Sindicator(ColorMode.COLORFUL)
#Or create an indicator under B&w mode
indicator = Sindicator(ColorMode.BW)

#if you want to show the result directly you can use
indicator.displayOK("message")
indicator.displayFAIL("message")
indicator.displayPASS("message")
indicator.displayWARN("message")

#if you want to show the progress indicator you need using
indicator.displayPROG("message")
#to show the progress indicator

#when you want to end the progree indicator you need using
indicator.updateStatus(Status.OK,"message")

#This function contains two parameters. The first parameter is 
#the Status type, which represents the execution of the current 
#progress. This is an Enum type in the class Sindicator.
#It contains several states of OK/ FAILED/ WARN/ PASS/ INPOGRESS.
#When this parameter is OK/ FAILED/ WARN/ PASS, calling the function
#will result The indicator disappears and displays the final
#result. When this parameter is INPOGRESS, the progress indicator
#will not change after the function is called. The second parameter
#is a string that represents the information about the final result
#or the update of the current progress. just like that

indicator.updateStatus(Status.INPROGRESS,"message")
    
```