import os,sys,csv,subprocess
  
def main(visit_type):
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


    commd = "make run arg1='"+str(n+1)+"' arg2='"+visit_type+"'"
    subprocess.run(commd,shell=True)

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print("Usage: %s <regular> | <tor> | <tor-like>" % (sys.argv[0]))
    sys.exit(1)

  try:
    visit_type = str(sys.argv[1])
    if len(sys.argv) > 2:
      raise Exception
    if visit_type != "regular":
      if visit_type != "tor":
        if visit_type != "tor-like":
          print("Entered wrong option!")
          print("Usage: %s <regular> | <tor> | <tor-like>" % (sys.argv[0]))
          sys.exit(1)
  except Exception as e:
      print("Too many args were sent!")
      print("Usage: %s <regular> | <tor> | <tor-like>" % (sys.argv[0]))

  main(visit_type)
