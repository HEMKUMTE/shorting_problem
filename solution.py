import csv

# This function is used to yield all the company
def get_company(c):
	for name in c:
		yield name





def short_data_of_file(filename):
	# read the csv file from current dir path
	with open(filename) as f:
    		reader = csv.reader(f)
    		names = next(reader)[2:]

   		 # call function to get all company from the csv file	
    		company = get_company(names)
	

    		hlist = []
    		hyearList=[]		
    		hlistCount = 0 
    		upYear = True		
    		for row in reader:
			year, month = row[:2]

			for i,r in enumerate(row[2:]):
	
				r = float(r)
				if hlistCount == 0:
					hlist.append(r)
					tempYearMonth = (year,month)
					hyearList.append(tempYearMonth)
				else:
					if r > hlist[i]:
						hlist[i] = r
						tempYearMonth = (year,month)
						hyearList[i] = (tempYearMonth)
				
				
			hlistCount = 1

    		# delete all reference of variable 
    		del hlistCount, reader, names, row, year, month, r, tempYearMonth
    
		i = 0
    		for name in company:
			print 'Company Name = ' + `name` + ', Heighest Price = ' + `hlist[i]` + ', Year = ' + `hyearList[i][0]` + ', Month = '+`hyearList[i][1]`
			print "-------------------------"
			i=i+1 


filename='data.csv'
short_data_of_file(filename)		
