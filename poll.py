# import modules
import os
import csv

#set the path for BudgetData.csv in LearnPython > PyBank
data = os.path.join("ElectionData.csv")

candidates = []


votes = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0


with open(data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        votes = votes + 1

        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            Khan = Khan +1
        elif row[2] == "Correy":
            Correy = Correy +1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "O'Tooley":
            OTooley = OTooley +1
    

        KhanPer = Khan/votes *100
        CorreyPer = Correy/votes *100
        LiPer = Li/votes *100
        OTooleyPer = OTooley/votes *100

        winner = [Khan, Correy, Li, OTooley]

                


    print(int(votes))
    print(candidates)
    print(Khan)
    print(Correy)
    print(Li)
    print(OTooley)
    print(KhanPer)
    print(CorreyPer)
    print(LiPer)
    print(OTooleyPer) 
    print(max(winner))

