import os
import csv 

total_months=0
total=0
i=1
Avg_change=0
Total_change=0
change=0
budget_file=os.path.join(".","Resources","budget_data.csv")
output_file = os.path.join("output.txt")
final_text=[]

with open(budget_file,newline="") as csvfile:
	csv_reader=csv.reader(csvfile,delimiter=",")
	csv_header=next(csvfile)
	#print(f"Header:{csv_header}")

	for row in csv_reader:
		total_months=total_months+1
		total=total+int(row[1])
		if(i==1):
			number1=int(row[1])
		#	print(number1)
		else:
			number2=int(row[1])
			change=number2-number1
			Total_change=Total_change+change
		#	print(number1)
			number1=number2
		#	print(number2)
		#	print(change)
			

		i=i+1	
	#print(f"i{i}")
	Avg_change=Total_change/(total_months-1)
	final_text.append("Financial Analysis \n Total number of months : " + str(total_months) +"\n Total Value :  " + str(total))
	final_text.append("\n Average Change : " + str(Avg_change))

	print("Financial Analysis")
	print(f"Total number of months:{str(total_months)}")
	print(f"Total value : {str(total)}")
	print(f"Average Change : {str(Avg_change)}")

with open(output_file, "w", newline="\n") as datafile:

    writer = csv.writer(datafile)
    writer.writerow(final_text)

