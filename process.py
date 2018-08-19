import subprocess


def getDets():
    with open("ss.txt", "w") as outfile:
        subprocess.call("top -bn1", shell=True, stdout=outfile)

getDets()