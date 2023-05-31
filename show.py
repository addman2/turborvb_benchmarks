import os
import sys
import json
import math

def c_filter(d, c):
    try:
        return d["computer"]["name"] == c
    except:
        pass
    return False

def s_filter(d, c):
    try:
        return d["softwarestack"]["name"] == c
    except:
        pass
    return False

def w_filter(d, c):
    try:
        return d["workload"] == c
    except:
        pass
    return False

def print_data(data):
    try:
        import tabulate
        headers = [ 'gitrev', 'time', 'workload', 'user', 'computer', 'software stack',
                    'walkers', 'mpi', 'omp', 'vmc', 'fn', 'vmc_forces', 'fn_forces']

        def process(l):
            ret = []
            ret.append(l['results']['gitrev'])
            ret.append(l['time'])
            ret.append(l['workload'])
            ret.append(l['user'])
            ret.append(l['computer']['name'])
            ret.append(l['softwarestack']['name'])
            ret.append(l['results']['walkers'])
            ret.append(l['results']['mpi'])
            ret.append(l['results']['omp'])
            try:
                ret.append(l['results']['vmc'])
            except:
                ret.append(None)
            try:
                ret.append(l['results']['fn'])
            except:
                ret.append(None)
            try:
                ret.append(l['results']['vmc_forces'])
            except:
                ret.append(None)
            try:
                ret.append(l['results']['fn_forces'])
            except:
                ret.append(None)
            return ret

        data = list(map(process, data))
        table = tabulate.tabulate(data, headers)
        print(table)

    except Exception as e:
        print(e)
        for d in data:
            line = f"{d['results']['gitrev']}\t{d['workload']}\t{d['user']}\t{d['computer']['name']}"
            n = "NA"
            try:
                n = f"{d['results']['walkers']}"
            except:
                pass
            line = line + f"\t{n}"
            n = "NA"
            try:
                n = f"{d['results']['vmc']:8.5f}"
            except:
                pass
            line = line + f"\t{n}"
            n = "NA"
            try:
                n = f"{d['results']['fn']:8.5f}"
            except:
                pass
            line = line + f"\t{n}"
            n = "NA"
            try:
                n = f"{d['results']['vmc_forces']:8.5f}"
            except:
                pass
            line = line + f"\t{n}"
            n = "NA"
            try:
                n = f"{d['results']['fn_forces']:8.5f}"
            except:
                pass
            line = line + f"\t{n}"
            print(line)

def accumulate(data, s):
    sortopt = { kv.split(":")[0]: kv.split(":")[1] for kv in s.split(",") }
    _data = [*data]

    value = "vmc"

    if "c" in sortopt:
        _data = [ d for d in _data if c_filter(d, sortopt["c"]) ]
    if "s" in sortopt:
        _data = [ d for d in _data if s_filter(d, sortopt["s"]) ]
    if "w" in sortopt:
        _data = [ d for d in _data if w_filter(d, sortopt["w"]) ]
    if "v" in sortopt:
        value = sortopt["v"]

    times = [ d["results"][value] / d["results"]["walkers"] / d["results"][f"gens_{value}"] for d in _data ]

    ave = sum(times) / len(times)
    std = math.sqrt(sum([ x*x for x in times ]) - ave*ave)

    return s, ave, std

def filter_data(data, s):
    k, v = s.split(":")
    if k == "c":
        data = [ d for d in data if c_filter(d, v) ]
    if k == "s":
        data = [ d for d in data if s_filter(d, v) ]
    if k == "w":
        data = [ d for d in data if w_filter(d, v) ]
    return data

def print_accdata(data):
    try:
        import tabulate

        headers = ["Accumulate", "Average", "Std"]
        print(tabulate.tabulate(data, headers = headers))
    except:
        for d in data:
            print(f"{d[0]}: {d[1]} +/- {d[2]}")

if __name__ == "__main__":
    data = []

    for d, dn, fn in os.walk("data/experiments"):
        for f in fn:
            if f.endswith(".json"):
                with open(f"{d}/{f}", "r") as fi:
                    entry = json.load(fi)
                    data.append(entry)

    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--acc",
                        type=str,
                        action="append",
                        help="Accumulate")

    parser.add_argument("-f", "--filter",
                        type=str,
                        action="append",
                        help="Accumulate")

    args = parser.parse_args()

    if args.filter:
        for f in args.filter:
            data = filter_data(data, f)

    if not args.acc:
        print_data(data)
        sys.exit(0)
    else:
        accdata = [ accumulate(data, acc) for acc in args.acc ]
        print_accdata(accdata)
