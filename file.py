import os, time
from shutil import copy2
from os import listdir
from os.path import isfile, join
while(1):
    mypath1=input("Enter the file: ")
    mypath = r"{}".format(mypath1)


    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    count = 0

    for i in onlyfiles:
        photo_file = f"{mypath}\{i}"
        time1 = os.path.getmtime(photo_file)
        year_file = time.strftime("%m",time.localtime(time1))
        create_folder_year = f"{mypath}\{year_file}"
        if not os.path.isdir(create_folder_year):
            os.mkdir(create_folder_year)
        copy2(photo_file,f"{create_folder_year}\{i}")
        count += 1
        print(i, " Count: ", count)
    

    
