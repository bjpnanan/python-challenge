import os
import csv 

total_voters=0
total=0
i=0
Avg_change=0
Total_change=0
change=0
list_candidate=[]
Dict_candidate={}
Dict_Percent={}
Final_Result=[]
winnercount=0

budget_file=os.path.join(".","Resources","election_data.csv")
output_file = os.path.join("output.txt")

with open(budget_file,newline="") as csvfile:
	csv_reader=csv.reader(csvfile,delimiter=",")
	csv_header=next(csvfile)
	#print(f"Header:{csv_header}")

	for row in csv_reader:
		total_voters=total_voters+1
		if row[2] not in list_candidate:
			list_candidate.append(row[2])
			Dict_candidate[row[2]]=1
			Dict_Percent[row[2]]=0
		else:
			Dict_candidate[row[2]]= Dict_candidate[row[2]]+1	
	#	total=total+int(row[1])
		i=i+1	
	#print(f"i{i}")

Final_Result.append("Election results \n-----------------------------\n Total number of voters:"+str(total_voters)+"\n-----------------------------\n")
#Final_Result.append("\nTotal number of voters:"+str(total_voters))
#Final_Result.append("\n-----------------------------")


for candidate in Dict_candidate:
	Dict_Percent[candidate]=Dict_candidate[candidate]/total_voters *100
	Final_Result.append(candidate)
	Final_Result.append(Dict_candidate[candidate])
	Final_Result.append(Dict_Percent[candidate])

for candidate in Dict_Percent:
	if Dict_Percent[candidate]>winnercount:
		winnercount=Dict_Percent[candidate]
		winner=candidate
Final_Result.append("\nWinner : \n")

Final_Result.append(winner)

print(f"{Final_Result}")

with open(output_file, "w", newline="") as datafile:

    writer = csv.writer(datafile)
    writer.writerow(Final_Result)

#print(f"{winnercount}")
#print(f"{winner}")	
#print(f"Winner : {winner}")



#print(f"candidates : {list_candidate}")
#print(f"Dict_candidate : {Dict_candidate}\n")
#print(f"Dict_Percent:{Dict_Percent}")
#print("Election results\n-----------------------------\n")
#print(f"Total number of voters:{str(total_voters)}")
	