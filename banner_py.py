import os
import time

def print_ashen_rain_banner():
    banner = '''
===============================
        A S H E N   R A I N
-------------------------------
  Silent. Disciplined. Clean.
  Forged in ash, falling in rain.
  Walking shadows with purpose.
===============================
'''
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(banner)
    time.sleep(1)  


print_ashen_rain_banner()
