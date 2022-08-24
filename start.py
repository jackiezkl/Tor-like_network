import os,csv,subprocess
  
#pop the first 2 website from the top 50 list, save to a new file, 
for n in range(0,50):
    line = []

    with open("./docker_home_folder/etc/list.csv") as csvfile:
        try:
            os.system("rm ./docker_home_folder/etc/visit.csv")
            os.system("touch ./docker_home_folder/etc/visit.csv")
        except:
            os.system('touch ./docker_home_folder/etc/visit.csv')

        clist = list(csv.reader(csvfile))

        line.append(clist[n])

    with open("./docker_home_folder/etc/visit.csv", 'w', newline='') as crawllist:
        linewriter = csv.writer(crawllist)
        linewriter.writerow(line[0])


    commd = "make run args='"+str(n+1)+"'" 
    subprocess.run(commd,shell=True)
