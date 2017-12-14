import requests, psycopg2, csv, sys, os
import signal

check = []

with open("corpus.csv",'r') as csvFile:

    read = csv.reader(csvFile)

    for row in read:

        check.append(row)

stored = []

for i in range (0, len(check)):

        stored.append(int(check[i][0]))

sortList = sorted(stored)

for j in range (int(sys.argv[1]), len(sortList)):

    RCR = []
    PMID = []
    FCR = []
    CPY = []
    pmid = []

    if (int(sys.argv[2]) != 0):

        os.kill(int(sys.argv[2]), signal.SIGKILL)

    pid = os.getpid()

    pmidCSV = "split/" + str(sortList[j]) + ".csv"

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

                os.system("python iCiteCheck.py " + str(j) + " " + str(pid))

            except requests.exceptions.ConnectionError as errc:

                print ("Error Connecting:",errc)
                print (j)

                os.system("python iCiteCheck.py " + str(j) + " " + str(pid))

            except requests.exceptions.Timeout:

                print ("Timeout Error:",errt)
                print (j)

                os.system("python iCiteCheck.py " + str(j) + " " + str(pid))

            except requests.exceptions.RequestException as err:

                print ("OOps: Something Else",err)
                print (j)

                os.system("python iCiteCheck.py " + str(j) + " " + str(pid))

            pub = response.json()

            if 'error' not in pub:

                pmid.append(pub["pmid"])
                RCR.append(pub["relative_citation_ratio"])
                FCR.append(pub["field_citation_rate"])
                CPY.append(pub["citations_per_year"])

    with open ("OncologyCorpus/" + str(sortList[j]) + ".csv", "w") as corpus:

        writer = csv.writer(corpus)
        writer.writerow(['pmid','relative_citation_ratio','field_citation_rate','citations_per_year'])
        writer.writerows(zip(pmid, RCR, FCR, CPY))

    print(str(sortList[j]) + " " + str(j))


