import os, csv, time, sys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def main():
    website_number = sys.argv[1]
    #print(website_number)
    with open("/home/etc/visit.csv") as csvfile:
        list_reader = csv.reader(csvfile)
        totalurllist = next(list_reader)
        visit_url = totalurllist[0]
        print(visit_url)

    for i in range(0,5):
        try:
            options = FirefoxOptions()
            options.add_argument("--headless")
            
##          uncomment the next 3 lines to use Tor on the host as a proxy
            options.set_preference('network.proxy.type',1)
            options.set_preference('network.proxy.socks', '172.17.0.1')
            options.set_preference('network.proxy.socks_port',9050)
            
            visit_page_driver = webdriver.Firefox(options=options)

            start_time = time.perf_counter()
            visit_page_driver.get(visit_url)
            end_time = time.perf_counter()

            #filename of the screenshot as: website-number_visit-number_loadtime.png
            screenshot_save_path = '/home/results/tor-like/screenshots/site_'+str(website_number)+"_"+str(i+1)+"_"+str(f"{end_time-start_time:0.6f}")+'.png'
            visit_page_driver.get_screenshot_as_file(screenshot_save_path)
            difference = end_time - start_time
            record = str(website_number) + "," + str(i+1)+","+str(difference)
            os.system("echo %s >> /home/results/tor-like/time.csv" % record)
            #print(visit_page_driver.page_source)
        except KeyboardInterrupt:
            print("Quiting...")
            visit_page_driver.quit()
            sys.exit()
        except:
            print("Page could not open!")
        finally:
            try:
                visit_page_driver.quit()
            except:
                print("Error on quiting web driver...")
                pass
        output = "echo 'No." + str(i+1) +" finished.'"
        os.system(output)
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) == 1:
      print("It doesn't seems like you are using the program as it was designed to be used. Please run the Start.py in the root folder.")
      sys.exit(1)
    main()
