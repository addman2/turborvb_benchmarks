import os
import sys
import json
import argparse
import subprocess
import datetime
import random
import string

now = datetime.datetime.now()
time_str = now.strftime("%H:%M:%S_%d-%m-%Y")

print(f" Time is: f{time_str}")

def load_stuf():
    with open("data/computers.json") as fi:
        computers = json.load(fi)
    with open("data/softwarestacks.json") as fi:
        softwarestacks = json.load(fi)
    return { **computers, **softwarestacks }

parser = argparse.ArgumentParser()

parser.add_argument("workload",
                    help="Set workload to run",
                    default="H-300-nopseudo")
parser.add_argument("-e", "--executable",
                    type=str,
                    help="Executable",
                    default="turborvb-serial.x")
parser.add_argument("-m", "--mpi",
                    type=str,
                    help="MPI prefix",
                    default="mpirun -np 1")
parser.add_argument("-c", "--computer",
                    type=str,
                    help="Select computer",
                    required=True)
parser.add_argument("-s", "--softwarestack",
                    type=str,
                    help="Select softwarestack",
                    required=True)
parser.add_argument("-w", "--number-of-walkers",
                    type=str,
                    help="Number of walkers",
                    required=True)
parser.add_argument("-u", "--user",
                    type=str,
                    help="User",
                    required=False,
                    default="Anonymous")

args = parser.parse_args()

executable = args.executable
workload = args.workload
mpi = args.mpi
computer = args.computer
softwarestack = args.softwarestack
number_of_walkers = args.number_of_walkers
user = args.user

stuff = load_stuf()

computer_info = [ x for x in stuff["computers"] if x["name"] == computer ][0]
softwarestack_info = [ x for x in stuff["softwarestacks"] if x["name"] == softwarestack ][0]

# Test executable
if not os.access(executable, os.X_OK):
    raise Exception(f"Cannot execute TurboRVB {executable}")

os.makedirs("laboratory", exist_ok=True)
os.system(f"tar xvzf Workloads/{workload}.tar.gz --directory laboratory")

experiment_command = f"cd laboratory/{workload} && export NW={number_of_walkers} && export EXE={executable} && MPI_PREFIX=\"{mpi}\" ./run && ./measure > output.json"
print(f"Executing {experiment_command}")
subprocess.run(experiment_command, shell=True)

with open(f"laboratory/{workload}/output.json") as fi:
    results = json.load(fi)

data = { "computer": computer_info,
         "time": time_str,
         "user": user,
         "workload": workload,
         "softwarestack": softwarestack_info,
         "results": results }

try:
    from icecream import ic
    ic(data)
except:
    pass

fname = "".join(random.choices(string.ascii_letters + string.digits, k=10))
with open(f"data/experiments/{fname}.json", "w") as fo:
    json.dump(data, fo, indent=4)
