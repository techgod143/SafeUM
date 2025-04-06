"""
    @ code by ---( Tech God )---
    @ Github : https://github.com/techgod143
    @ YouTube : https://www.youtube.com/@techgod143
    @ WhatsApp : https://whatsapp.com/channel/0029Va9Ufzi8kyyEnEHvOm1h
    
"""
import os, sys,time, platform
os.system('clear') 
print('\033[0m [💸] \033[92m Follow Our WhatsApp channel For More Updates👿☠️ ') 
time.sleep(3)
os.system('xdg-open https://whatsapp.com/channel/0029Va9Ufzi8kyyEnEHvOm1h')
print('\n\033[0m [\033[92m✓\033[97m] \033[92m Checking For Updates ....\n') 

bit = platform.architecture()[0]
if bit == '64bit':
    import SafeUM
elif bit == '32bit':
    print("\033[0m\033[91m Sorry Your Device Is 32bit, This Tool 32bit Not Sported, Only For \033[92m64Bit\033[0m ]");exit() 
 
