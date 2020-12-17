import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

with open("requirements.txt", 'r') as f:
    modulos = f.read().splitlines()

for modulo in modulos:
    install(modulo)
