import os
import platform
import subprocess

print("Fira server launcher")
print("Is port forwarding currently enabled on your network, and pointing to your machine (yes / no)")
while(True):
    choice = input(": ")
    if(choice == "yes"):
        break
    elif(choice == "no"):
        print("Make sure that is set up before tyring to make this publically accessible")
        print("Pocketbase will now serve on the default localhost address (127.0.0.1:8090)")
        break
    else:
        print("Invalid choice. Try again")
operating_sys = platform.system()
architecture = platform.processor()
print(f"Detected Operating System: {operating_sys}")
print(f"Detected architecture: {platform.processor()}")
correct = True
while(True):
    print("Is this right? (yes / no)")
    choice = input(": ")
    if(choice == "yes"):
        break
    elif(choice == "no"):
        correct = False
        break
    else:
        print("Invalid choice. Try again")

if(not correct):
    while(True):
        print("New operating system")
        print("(Windows, Darwin, Linux)")
        operating_sys = input(": ")
        if(operating_sys in ["Windows", "Darwin", "Linux"]):
            break
        else:
            print("Invalid choice. Try again")
    while(True):
        print("New architecture")
        print("(amd, x86_64)")
        architecture = input(": ")
        if(architecture in ["amd", "x86_64"]):
            break
        else:
            print("Invalid choice. Try again")
print(f"Running pocketbase for {operating_sys} on {architecture}")
print("Press ^ + c to stop, or close terminal window")
process = subprocess.run([f"./pocketbase-{operating_sys}-{architecture}", "serve"])