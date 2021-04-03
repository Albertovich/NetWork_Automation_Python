import telnetlib
import getpass
import time

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()
timestr = time.strftime("%Y%m%d-%H%M%S")

f = open ('myswitches')

for IP in f:
        IP=IP.strip()
        print ("Creating Backup for: " + (IP))
        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")

        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        tn.write(b"terminal length 0\n")
        tn.write(b"show run\n")
        tn.write(b'exit\n')

        readoutput = tn.read_all()
        saveoutput = open(f"switch_{HOST}_" + timestr, "w")
        saveoutput.write(readoutput.decode('ascii'))
        saveoutput.write("\n")
        saveoutput.close
