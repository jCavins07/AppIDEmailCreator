import os, sys
import re

file = 'AppIDFile.txt'
path = 'C:\\Users\\labuser\\Documents\\GitHub\\AppIDEmailCreator\\UIApp'

filePath = open(path + '\\' + file)

# fileStr= filePath.read()

# print(fileStr)


# device = input("What kind of device is it: ")
deviceStr = filePath.readline().strip()
device = deviceStr[2:]
print("The device is " + str(device))
# radio = input("What kind of radio: ")
radioStr = filePath.readline().strip()
radio = radioStr[2:]
print("The radio is " + str(radio))
# appID = input("What App ID are you working with: ")
appIDStr = filePath.readline().strip()
appID = appIDStr[2:]
print("You are working with " + str(appID))
prevFirmwareStr = filePath.readline().strip()
prevFirmware = prevFirmwareStr[2:]
print("The previous firmware was " + str(prevFirmware)) 

partNumberStr = filePath.readline().strip()
partNumber = partNumberStr[2:]
print("The partnumber is " + str(partNumber))
# firmware = input("What is the firmware: ")
firmwareStr = filePath.readline().strip()
firmware = firmwareStr[2:]
print("The firmware you put is " + str(firmware))
print("The previous firmware was " + str(prevFirmware)) 
# atePass = input("What is the ATE pass number: ")
atePassStr = filePath.readline().strip()
atePass = atePassStr[2:]
print("The ate pass number is " + str(atePass))

otaConfigStr = filePath.readline().strip()
updateFwStr = firmware[:-1] + 'z'
print("The update firmware is " + updateFwStr + "\n")



partOne = "All,\n Here is the test report for the : " 

fullString = partOne + device + " " + radio + " AppID: " +  appID + " Firmware: " + firmware

partTwo = "\n\n\nWhat was tested for this release:\n ATE PASS Test ID: " + str(atePass)

fullString += partTwo 
partThree = "\nP/N: " + str(partNumber) + "\n"

fullString += partThree


automatedTestsOneStr = "\nAutomated-\n\nDNS Lookup\nAccumulator gps off\nAccumulator gps on\nAccumulator restore on wakeup\nAutoconnect on powerup\nFill log reset\nLog batchmode\nInfo commands\nPeg event report\nPeg id report\nRecover system time after wakeup"

automatedTestsTwoStr = "\nPeg sleep wakeup timer\nWakeup on time of day\nComm on/off\nGPS on/off\nSystem time src 3D GPS\nSystem time src reject Cell Network\nSystem time src reject Server\nSystem time src reject None 3D GPS\nSystem time src reject RTC"

automatedTestsThreeStr = "\nSystem time src reject 3D GPS\nSystem time src Server\nLong motion logs \nParam 300\nTCP (Establish Connection)\nReplay attack protection\nAccumulator During Sleep\nNewcommArchitecture\n"

automatedTestsStr = automatedTestsOneStr + automatedTestsTwoStr + automatedTestsThreeStr

fullString += automatedTestsStr

paramMigrationStr = prevFirmware + " -> " + firmware # This string is for the previous fw and current fw
OTAFwStr = paramMigrationStr + " -> " + updateFwStr # This takes prev fw current and updated fw
serialDNLDStr = firmware + " -> " + OTAFwStr + " -> " + firmware
manualTestsStr = "\nManual Testing-\nParameter Migration: " + paramMigrationStr + "\n"
manualTestsStr += "OTAConfig Update: " + otaConfigStr + "\n"
manualTestsStr += "OTAFirmware Update: " + OTAFwStr + "\n"
manualTestsStr += "SMS\nSMSParamMigration\n"
manualTestsStr += "Serial Download: " + serialDNLDStr + "\n"
manualTestsStr += "ICN\nLMU Direct Sequence\n"




fullString += manualTestsStr

skippedTestsStr = "\nWhat you didn't have time to test but feel is ok to skip with low risk:\n\n\t None \n\n"
issuesStr = "List of issues found:\n\n\t None\n\nAny issues that are assigned to release in Jira that you feel can be deferred (and why)  if not already validated by you:\n\n\tNone\n"                 
fullString += skippedTestsStr
fullString += issuesStr

notesStr = "\n Any other notes you feel need to be included as part of your testing:\n\nNotes:\n\n Logs can be found here:"
fileFolder = "S:\\Validation\\Releases\\" + firmware + "\\AppIDRelease Doc\\" + appID
notesStr += fileFolder

fullString += notesStr

migratingFwStr = "\n\nParameter Migration:\n\n\n-\t have copied all the parameter migration files into the shared folder between" + prevFirmware + " -> " + firmware + " haven't seen any issues.\n\n"

fullString += migratingFwStr

fullString += "ATI0 - from Testing: \n\n\n\n"
fullString += "ATI0 - from PULS: \n\n\n\n"
 
print("************************************")
print("Full text")
print("************************************")
print("\n")


print(fullString)

print("\n")
print("************************************")
print("END")
print("************************************")

