import platform
import uuid
import socket
import time
import calendar
import os

def clr():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

clr()


def calander(): print(calendar.month(2019,10))


def todays_date():
    print('\033[35;0;42m', time.asctime(time.localtime(time.time())),'\033[0m')


def macaddress():
    print('\033[30;0;44m MAC Address in HEX\t:\033[31;1;40m ', hex(uuid.getnode()),'\033[0m')
    #print(" add :--", end="")
    #print("\033[31;1;40m The MAC Address is formatted way is :", end="")
    #print(': '.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
    #print('\033[0m')
    x = ': '.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    print('\033[30;0;44m MAC Address\t\t: \033[31;1;40m', x ,'\033[0m')

def get_system_IP():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    #print(s)
    print('\033[30;0;44m IP Address \t\t: \033[31;1;40m',s.getsockname(), '\033[0m')
    return s.getsockname()[0]

def welcome():
    print('     \033[1;32;47m WELCOME\033[0m\033[1;34;47m TO\033[0m'
          '\033[1;31;47m FORTIFY SOLUTIONS\033[0m\n')
    print('\033[0;31;40m\n <<This Program is to Get Your System Information>>\n\n'
          '\033[0m \n')


def option_lists():
    print('The options are:-')
    print('\033[2;31;40m================================================\033[0m')
    print('[1]System infomation\t\t[2] machine infomation\n'
          '[3]version infomation\t\t[4] uname infomation\n'
          '[5]processor infomation\t\t[6] platform infomation\n'
          '[7]architecture infomation\t[8] Node infomation\n'
          '[9]python version infomation\t[10] release infomation\n'
          '[11]system version infomation\t[12] system version infomation\n'
          '[13]IP Address\t\t[14] MAC Address\n'
          '[15] All Parameters\t\t[16] EXIT\n')
    print('\033[2;31;40m================================================\033[0m')


print('\033[1;31m ______ ____  _____ _______ _____ ________     __\n'
'|  ____/ __ \|  __ \__   __|_   _|  ____\ \   / /\n'
'| |__ | |  | | |__) | | |    | | | |__   \ \_/ / \n'
'|  __|| |  | |  _  /  | |    | | |  __|   \   /  \n'
'| |   | |__| | | \ \  | |   _| |_| |       | |   \n'
'|_|    \____/|_|  \_\ |_|  |_____|_|       |_|   \033[0m\n'
'\n'
  '_____  ____  _     _    _ _______ _____ ____  _   _  _____\n' 
 '/ ____|/ __ \| |   | |  | |__   __|_   _/ __ \| \ | |/ ____|\n'
'| (___ | |  | | |   | |  | |  | |    | || |  | |  \| | (___  \n'
 '\___ \| |  | | |   | |  | |  | |    | || |  | | . ` |\___ \ \n'
' ____) | |__| | |___| |__| |  | |   _| || |__| | |\  |____) |\n'
'|_____/ \____/|______\____/   |_|  |_____\____/|_| \_|_____/ \n')

welcome()
#macaddress()
#get_system_IP()
todays_date()
#calander()
option_lists()

while True:
    try:
        x = int(input('Enter your option :'))
        time.sleep(1)
    except ValueError:
        todays_date()
        print('Enter Valid INPUT')

    if x == 1:
        print(f'System info: {platform.system()}')  # Linux
    elif x==2:
        print(f'Machine info: {platform.machine()}') #x86_64 Returns the machine type, e.g. 'i386'. An empty string is returned if the value cannot be determined.
    elif x==3:
        print(f'Version info: {platform.version()}')  # 1 SMP Debian 4.19.28-2kali1 (2019-03-18)
    elif x==4:
        print(f'uname info: {platform.uname()}') #uname_result(system='Linux', node='FortifySolutions', release='4.19.0-kali4-amd64', version='#1 SMP Debian 4.19.28-2kali1 (2019-03-18)', machine='x86_64', processor='')
    elif x==5:
        print(f'processor info: {platform.processor()}')
    elif x==6:
        print(f'platform info: {platform.platform()}')
    elif x==7:
        print(f'architecture info: {platform.architecture()}')
    elif x==8:
        print(f'Node info: {platform.node()}')
    elif x==9:
        print(f'Python version info: {platform.python_version()}')
    elif x==10:
        print(f'Release info: {platform.release()}')
    elif x==11:
        print(f'System version info: {platform._sys_version()}')
    elif x==12:
        print(f'system version info: {platform.mac_ver()}')
    elif x==15:
        #platform
        # — Access to underlying platform’s identifying data
        print(f'System info     : {platform.system()}') #Linux
        print(f'Machine info    : {platform.machine()}') #x86_64 Returns the machine type, e.g. 'i386'. An empty string is returned if the value cannot be determined.
        print(f'Version info    : {platform.version()}') #1 SMP Debian 4.19.28-2kali1 (2019-03-18)
        print(f'uname info      : {platform.uname()}') #uname_result(system='Linux', node='FortifySolutions', release='4.19.0-kali4-amd64', version='#1 SMP Debian 4.19.28-2kali1 (2019-03-18)', machine='x86_64', processor='')
        print(f'Processor info  : {platform.processor()}')
        print(f'Platform info   : {platform.platform()}')
        print(f'Architecture info: {platform.architecture()}')
        print(f'Node info       : {platform.node()}')
        print(f'Python version info: {platform.python_version()}')
        print(f'Release info    : {platform.release()}')
        print(f'System version info: {platform._sys_version()}')
        print(f'System version info: {platform.mac_ver()}')
    elif x == 13:
        get_system_IP()
    elif x == 14:
        macaddress()
    elif x == 16:
        clr()
        print('\033[1;31;42m Thank You....HAVE A NICE TIME!!!!! \033[0m\n\n\033[1;31;40m Fortify Solutions\033[0m')
        todays_date()
        break
    elif x >= 17:
        print('Please select input from 1 to 16')
        option_lists()
