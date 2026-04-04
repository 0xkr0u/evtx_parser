from Evtx.Evtx import Evtx
import json
import argparse

initiate_args= argparse.ArgumentParser(description="evtx to xml parser")
initiate_args.add_argument("-f","--file_name",help="enter filename")
args = initiate_args.parse_args()

file = args.file_name


with Evtx(file) as logs:
    records = []
    for lines in logs.records():
        records.append(lines.xml())

    print(json.dumps(records,indent=2))

