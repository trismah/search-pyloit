import subprocess

search = input("Search for: ")
output = subprocess.check_output(f"searchsploit {search}", shell=True).decode("utf-8")
 
output = [(x.split("|")) for x in output.split("\n")[3:-3]]

for i, (name, _) in enumerate(output):
    print(f"{i+1}. {name}")

print("Leave blank to exit.")
if choice := input("> ") != "":
    feedback = subprocess.check_output(f"searchsploit -m {output[choice-1][1]}", shell=True).decode("utf-8")
    print(f"Saved: {feedback}")
