import subprocess
import json
print("Fira Server Launcher")
try:
    with open('config.json') as f:
        settings = json.load(f)
except:
    print("Malformed config.json. Run setup.py again to fix")
    exit()


operating_sys = settings["os"]
architecture = settings["architecture"]
if(settings["extracted"]):
    print(f"Running pocketbase for {operating_sys} on {architecture}")
    print("Press ^ + c to stop, or close terminal window")
    process = subprocess.run([f"./pocketbase-{operating_sys}-{architecture}", "serve"])
else:
    print("Pocketbase not extracted yet. Re-run setup.py to fix")