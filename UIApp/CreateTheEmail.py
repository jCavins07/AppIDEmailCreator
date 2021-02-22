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



partOne = "All,\n Here is the test report for the : " 

fullString = partOne + device + " " + radio + " AppID: " +  appID + " Firmware: " + firmware

partTwo = "\n\n\nWhat was tested for this release:\n ATE PASS Test ID: " + str(atePass)

fullString += partTwo 
partThree = "\nP/N: " + str(partNumber)

fullString += partThree

print("************************************")
print("Full text")
print("************************************")
print("\n")


print(fullString)

print("\n")
print("************************************")
print("END")
print("************************************")

