import platform
import json
import zipfile
import shutil
import subprocess
data = {
    "os": "",
    "architecture": "",
    "extracted": False,
    "executable": False,
}
print("Fira Server Setup")
print("Is port forwarding currently enabled on your network, and pointing to your machine (yes / no)")
while(True):
    choice = input(": ")
    if(choice == "yes"):
        break
    elif(choice == "no"):
        print("Make sure that is set up before tyring to make this publically accessible")
        print("Pocketbase will serve on a default localhost address instead (127.0.0.1:8090)")
        break
    else:
        print("Invalid choice. Try again")
operating_sys = platform.system()
print(f"Detected Operating System: {operating_sys}")
correct = True
while(True):
    print("Is this right?\n(yes / no)")
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
        print("Select operating system\n(Windows, Darwin, Linux)")
        operating_sys = input(": ")
        if(operating_sys in ["Windows", "Darwin", "Linux"]):
            break
        else:
            print("Invalid choice. Try again")
while(True):
    print("Select CPU architecture\n(arm, x86_64)")
    architecture = input(": ")
    if(architecture in ["arm", "x86_64"]):
        break
    else:
        print("Invalid choice. Try again")

data["os"] = operating_sys
data["architecture"] = architecture
print("Attempting to extract the proper version of pocketbase")
with zipfile.ZipFile(f"zips/pocketbase-{operating_sys}-{architecture}.zip", 'r') as zip:
    zip.extractall()
print("Pocketbase Extracted")
data["extracted"] = True
print("Delete unused pocketbase versions?\n(yes / no)")
while(True):
    choice = input(": ")
    if(choice == "yes"):
        print("Deleting files")
        shutil.rmtree("zips")
        break
    else:
        break

print("Saving data to config file")
conf_data = json.dumps(data, indent=2)

with open("config.json", "w") as f:
    f.write(conf_data)

if(operating_sys != "Windows"):
    print("Adding executable privleges to pocketbase binary")
    subprocess.run(['chmod', 'a+x', f'pocketbase-{operating_sys}-{architecture}'])
    print("Executable formatted")

data["executable"] = True

print("Data saved! Run main.py to begin")
    


