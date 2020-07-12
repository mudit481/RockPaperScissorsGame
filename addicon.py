# Create RockPaperScissors Icon In Your Launcher
import os
os.system("chmod +x launch")
Path = os.getcwd()
with open("RockPaperScissors.desktop","w") as fh:
    with open("desktopTemplate", "r") as template:
        fh.write(template.read())
    fh.write("\nPath={path}/\n".format(path = Path))
    fh.write("Exec={path}/launch\n".format(path = Path))

os.system("chmod +x RockPaperScissors.desktop")

os.system("cp RockPaperScissors.desktop ~/.local/share/applications/")