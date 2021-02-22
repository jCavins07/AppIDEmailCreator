import os, sys

device = input("What kind of device is it: ")
print("The device is " + str(device))
radio = input("What kind of radio: ")
print("The radio is " + str(radio))
appID = input("What App ID are you working with: ")
print("You are working with " + str(appID))
firmware = input("What is the firmware: ")
print("The firmware you put is: " str(firmware))


partOne = "All,\n Here is the test report for the : " 

fullString = partOne + device + " " + radio + " AppID: " +  appID + " Firmware: " + firmware

print("************************************")
print("Full text")
print("************************************")
print("\n")


print(fullString)

print("\n")
print("************************************")
print("END")
print("************************************")

