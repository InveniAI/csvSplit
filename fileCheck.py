#!/usr/bin/python

import os, sys, csv

path = "split/"
dirsPMID = os.listdir(path)
path = "OncologyCorpus/"
dirsMeta = os.listdir(path)

PMID = []
META = []
NOT = []

for file in dirsPMID:

    PMID.append(str(file))

for file in dirsMeta:

    META.append(str(file))

for pmid in PMID:

    if pmid not in META:

        NOT.append(pmid)

with open("corpus.csv", "w") as output:
    writer = csv.writer(output)

    for row in NOT:

        integer = row.replace(".csv","")
        writer.writerow([integer])
