import os
import json
import solver

if not os.path.isdir("Nonograms"):
    os.mkdir("Nonograms")

def load(path: str) -> solver.Nonogram:
    file = open(path)
    data = json.load(file)
    return solver.Nonogram(data["rows"], data["columns"])

non = load("Nonograms/test.json")
non.show()