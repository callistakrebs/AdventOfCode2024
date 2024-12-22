import re
from scipy.optimize import linprog
import numpy as np

def findXandY(line):
    pattern = r"Button .: X\+(\d+), Y\+(\d+)"
    return list(map(int,re.findall(pattern, line)[0]))

def findPrize(line):
    pattern = r"Prize: X=(\d+), Y=(\d+)"
    return list(map(int,re.findall(pattern, line)[0]))

if __name__ == "__main__":
    with open("day13.txt") as f:
        machines = [machine.split("\n") for machine in f.read().split("\n\n")]
    
    machine_rules = []
    for machine in machines:
        machine_rules.append({"A": findXandY(machine[0]), "B": findXandY(machine[1]), "Prize": findPrize(machine[2])})

    tokens_min = 0
    c = [3, 1] # A B
    for rule in machine_rules:
        A_eq = np.array([[rule["A"][0], rule["B"][0]], # Ax + Bx + X
                [rule["A"][1], rule["B"][1]],  # Ay + By + Y
                ], dtype=np.uint64)
        b_eq = np.array([rule["Prize"][0]+10000000000000, rule["Prize"][1]+10000000000000], dtype=np.uint64)
        bounds = [(0,None), (0,None)]
        result = linprog(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=[1,1],method="highs", options={"autoscale":True, "presolve":False})

        if result["success"]:
            tokens_min += int(result["fun"]) # This machine is winable, add its tokens to total
    
    print(tokens_min)