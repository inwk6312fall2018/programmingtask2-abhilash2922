def list_crimes(file): #function for list of unique crime numbers
 data = open(file,"r") # reading data from csv
 d = dict()
 lot = []
 for line in data:
    line=line.strip()
    array = line.split(',')
    lot.append(array[-1])  #appending data (only crime name data to list)
 for i in lot: #looping list
    if i not in d:  #checking list data in dictinary
      d[i]=1         # if no exists appending  
    else:
      d[i]+=1           # if  exists adding count value
 print("crimename",' '*16,"crimecount")  #printing headers 
 for k, v in d.items():   # printing tabular format
    label= v
    print("{:<28} {:<35}".format(k, label))      
file_name="Crime.csv" 
list_crimes(file_name) # calling function
