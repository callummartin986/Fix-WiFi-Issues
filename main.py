import os

os.system("ipconfig")
os.system("ipconfig /release")
os.system("ipconfig /renew")
os.system("ipconfig /flushdns")
os.system("netsh winsock reset")
os.system("netsh int TCP reset")
os.system("shutdown -r")
