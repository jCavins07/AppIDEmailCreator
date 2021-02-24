import os, sys

device = input("What kind of device is it: ")
print("The device is " + str(device))
radio = input("What kind of radio: ")
print("The radio is " + str(radio))
appID = input("What App ID are you working with: ")
print("You are working with " + str(appID))
firmware = input("What is the firmware: ")
print("The firmware you put is " + str(firmware))
partNumber = input("What is the part number: ")
print("The partnumber is " + str(partNumber))
prevFirmware = input("What was the previous firmware: ")
print("The previous firmware was " + str(prevFirmware)) 
atePass = input("What is the ATE pass number: ")
print("The ate pass number is " + str(atePass))

otaConfigStr = "50.44"
updateFwStr = firmware[:-1] + 'z'
print("The update firmware is " + updateFwStr + "\n")



partOne = "All,\n Here is the test report for the : " 

fullString = partOne + device + " " + radio + " AppID: " +  appID + " Firmware: " + firmware

partTwo = "\n\n\nWhat was tested for this release:\n ATE PASS Test ID: " + str(atePass)

fullString += partTwo 
partThree = "\nP/N: " + str(partNumber) + "\n"

fullString += partThree


automatedTestsOne = "\nAutomated-\n\nDNS Lookup\nAccumulator gps off\nAccumulator gps on\nAccumulator restore on wakeup\nAutoconnect on powerup\nFill log reset\nLog batchmode\nInfo commands\nPeg event report\nPeg id report\nRecover system time after wakeup"

automatedTestsTwo = "\nPeg sleep wakeup timer\nWakeup on time of day\nComm on/off\nGPS on/off\nSystem time src 3D GPS\nSystem time src reject Cell Network\nSystem time src reject Server\nSystem time src reject None 3D GPS\nSystem time src reject RTC"

automatedTestsThree = "\nSystem time src reject 3D GPS\nSystem time src Server\nLong motion logs \nParam 300\nTCP (Establish Connection)\nReplay attack protection\nAccumulator During Sleep\nNewcommArchitecture\n"

automatedTests = automatedTestsOne + automatedTestsTwo + automatedTestsThree

fullString += automatedTests

paramMigrationStr = prevFirmware + " -> " + firmware 
OTAFwStr = paramMigrationStr + " -> " + updateFwStr
serialDNLDStr = firmware + " -> " + OTAFwStr + " -> " + firmware
manualTestsStr = "\nManual Testing-\nParameter Migration: " + paramMigrationStr + "\n"
manualTestsStr += "OTAConfig Update: " + otaConfigStr + "\n"
manualTestsStr += "OTAFirmware Update: " + OTAFwStr + "\n"
manualTestsStr += "SMS\nSMSParamMigration\n"
manualTestsStr += "Serial Download: " + serialDNLDStr + "\n"
manualTestsStr += "ICN\nLMU Direct Sequence\n"

fullString += manualTestsStr
print("************************************")
print("Full text")
print("************************************")
print("\n")


print(fullString)

print("\n")
print("************************************")
print("END")
print("************************************")

