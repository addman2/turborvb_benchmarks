import os
import json

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

data = []

for d, dn, fn in os.walk("data/experiments"):
    for f in fn:
        if f.endswith(".json"):
            with open(f"{d}/{f}", "r") as fi:
                entry = json.load(fi)
                data.append(entry)

print_data(data)
