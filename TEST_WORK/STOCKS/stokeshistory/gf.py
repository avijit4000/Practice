import csv
import os
# path="D:\Pyn\online learning\INURAN_DATA\FSDS_September\TEST_WORK\STOCKS\stokeshistory"
# dict={"python":".py","c++":".cpp","Java":".java"}
# w=csv.writer(open(path+os.sep+'out.csv','w'))
# for key,val in dict.items():
#     w.writerow([key,val])


with open('out.csv',newline="") as csvfile:
    data=csv.DictReader(csvfile)
    for row in data:
        print(row)