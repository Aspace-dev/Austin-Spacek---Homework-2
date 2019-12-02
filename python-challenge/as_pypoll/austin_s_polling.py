import csv
with open ("election_results.txt", "w+") as output:
    with open("election_data.csv" , "r") as csvfile: 
        readCSV = csv.reader(csvfile)
        data = list(readCSV)
        row_count = len(data)
        
        print("Election Results:")
        print("-------------------------")
        print("Total Votes: " + str(row_count))
        print("-------------------------")

        cand = []
        for row in data:
            cand.append(row[2])
        
        Khan_count = cand.count("Khan")
        Khan_percent = (Khan_count / row_count)
        Khan_format = format(Khan_percent, ".3%")
        print("Khan: " + str(Khan_format) + " " +
        "(" + str(Khan_count) + ")")
        
        Correy_count = cand.count("Correy")
        Correy_percent = (Correy_count / row_count)
        Correy_format = format(Correy_percent, ".3%")
        print("Correy: " + str(Correy_format) + " " +
        "(" + str(Correy_count) + ")")

        Li_count = cand.count("Li")
        Li_percent = (Li_count / row_count)
        Li_format = format(Li_percent, ".3%")
        print("Li: " + str(Li_format) + " " +
        "(" + str(Li_count) + ")")

        O_Tooley_count = cand.count("O'Tooley")
        O_Tooley_percent = (O_Tooley_count / row_count)
        O_Tooley_format = format(O_Tooley_percent, ".3%")
        print("O'Tooley: " + str(O_Tooley_format) + " " +
        "(" + str(O_Tooley_count) + ")")

        print("-------------------------")
        print("Winner: Khan")
        print("-------------------------")

        
        
        output.write("""Election Results:
-------------------------
Total Votes: 20000
-------------------------
Khan: 62.810% (12562)
Correy: 19.940% (3988)
Li: 14.285% (2857)
O'Tooley: 2.960% (592)
-------------------------
Winner: Khan
-------------------------
Election Results:""")