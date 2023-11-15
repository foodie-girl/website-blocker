import time
import datetime

end_time = datetime.datetime(2023, 11, 20)
site_block = ["www.google.com", "www.facebook.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking...")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for websites in site_block:
                if websites not in content:
                    host_file.write(redirect+" "+websites+"\n")
                else:
                    pass
    else:
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(websites in lines for website in site_block):
                    host_file.write(lines)

                host_file.truncate()

        time.sleep(5)