import requests, psycopg2, csv, sys, os

for j in range (int(sys.argv[1]), 101):

    RCR = []
    PMID = []
    FCR = []
    CPY = []
    pmid = []

    pid = os.getpid()

    pmidCSV = "split/" + str(j) + ".csv"

    with open (pmidCSV, 'r') as myFile:

        reader = csv.reader(myFile)

        for row in reader:

            PMID.append(row)

        for i in range (0, len(PMID)):

            try:

                response = requests.get(
                    "/".join([
                    "https://icite.od.nih.gov/api",
                    "pubs",
                    PMID[i][0],
                    ]),
                )

            except requests.exceptions.HTTPError as errh:

                print ("Http Error:",errh)
                print (j)

                os.system("python iCite.py " + str(j) + " && kill " + str(pid))

            except requests.exceptions.ConnectionError as errc:

                print ("Error Connecting:",errc)
                print (j)

                os.system("python iCite.py " + str(j) + " && kill " + str(pid))

            except requests.exceptions.Timeout:

                print ("Timeout Error:",errt)
                print (j)

                os.system("python iCite.py " + str(j) + " && kill " + str(pid))

            except requests.exceptions.RequestException as err:

                print ("OOps: Something Else",err)
                print (j)

                os.system("python iCite.py " + str(j) + " && kill " + str(pid))

            pub = response.json()

            if 'error' not in pub:

                pmid.append(pub["pmid"])
                RCR.append(pub["relative_citation_ratio"])
                FCR.append(pub["field_citation_rate"])
                CPY.append(pub["citations_per_year"])

    with open ("OncologyCorpus/" + str(j) + ".csv", "w") as corpus:

        writer = csv.writer(corpus)
        writer.writerow(['pmid','relative_citation_ratio','field_citation_rate','citations_per_year'])
        writer.writerows(zip(pmid, RCR, FCR, CPY))

    print(j)


