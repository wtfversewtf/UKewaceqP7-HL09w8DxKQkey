import subprocess,os
import sys

#------------------XOA MAN HINH-------------------------#

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Thêm dòng thông báo
print("Please wait, we are checking for the libraries...")
clrscr()


# Hàm để cài đặt thư viện
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Danh sách các thư viện cần kiểm tra và cài đặt
libraries = [
    "requests",
    "psutil",
]

for library in libraries:
    try:
        __import__(library)
    except ImportError:
        print(f"{library} is not installed. Installing now...")
        install(library)
        clrscr()

import requests
import platform
import psutil
import uuid
import datetime
import time
import socket
import json
import random
import string
import os
import sys

def run_banner(text, delay=0.0001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_key(key):
    url = "https://pidkey.vip/PidKey.aspx?key=" + key
    response = requests.get(url)
    
    if response.status_code == 200:
        start_index = response.text.find("{")
        end_index = response.text.rfind("}") + 1
        json_data = response.text[start_index:end_index]
        result = json.loads(json_data)
        return result
    else:
        return {"error": "Lỗi kết nối: %d" % response.status_code}

def main():
    while True:
        try:
            clear_screen()
            run_banner("\033[1;37m\033[1m┌────────────────────────────────────────────────────────────────────────────┐")
            run_banner("\033[1;37m\033[1m|Windows activation key validator\033[1;37m\033[1m                                                 |")
            run_banner("\033[1;37m\033[1m|Note: Only check 1 key each!\033[1;37m\033[1m                                                 |") 
            run_banner("\033[1;37m\033[1m|----------------------------------------------------------------------------|") 
            run_banner("\033[1;37m\033[1m|Support for:\033[1;37m\033[1m                                                                |")
            run_banner("\033[1;37m\033[1m|\x1b[38;5;226mWin 11 RTM IoTEnterpriseSK\033[1;37m\033[1m                                                  |")
            run_banner("\033[1;37m\033[1m|\x1b[38;5;226mWindows 10\033[1;37m\033[1m                                                                  |")
            run_banner("\033[1;37m\033[1m|\x1b[38;5;226mWindows 8\033[1;37m\033[1m                                                                   |")
            run_banner("\033[1;37m\033[1m|\x1b[38;5;226mWindows 7\033[1;37m\033[1m                                                                   |")
            run_banner("\033[1;37m\033[1m|\x1b[38;5;226mOffice\033[1;37m\033[1m                                                                      |")
            run_banner("\033[1;37m\033[1m|----------------------------------------------------------------------------|") 
            run_banner("\033[1;37m\033[1m|Be sure the key in format \033[1;31m\033[1m\033[1mxxxxx-xxxxx-xxxxx-xxxxx-xxxxx\033[1;37m\033[1m                     |")
            run_banner("\033[1;37m\033[1m|Example: \033[1;31m\033[1m\033[1m26QN8-828KP-V62WD-C86V7-9BXVX \033[1;37m\033[1mhoặc \033[1;31m\033[1m\033[1mY6JNK-P2XWX-6B9KJ-8FWDV-DRR94\033[1;37m\033[1m |")
            run_banner("\033[1;37m\033[1m└────────────────────────────────────────────────────────────────────────────┘")
            key = input("\n\033[1;37m\033[1mEnter the activation key: ")
            result = check_key(key)
            if "error" in result:
                print("Error!", result["error"])
            else:
                print("\n\n ╔═════════════════════════════════════════════════════════════════════")
                print("╔╣Key:\033[1m\033[38;5;51m", result["Key"])
                print("\033[1;37m\033[1m║║Description:\033[1m\033[38;5;51m", result["Description"])
                print("\033[1;37m\033[1m║║Remain:\033[1m\033[38;5;51m", result["Remain"])
                print("\033[1;37m\033[1m║║ErrorCode:\033[1m\033[38;5;51m", result["ErrorCode"])
                print("\033[1;37m\033[1m║║IID:\033[1m\033[38;5;51m", result["IID"])
            
            current_time = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
            print("\033[1;37m\033[1m║║Time:\033[1m\033[38;5;51m", current_time)
            print("\033[1;37m\033[1m╚╩═════════════════════════════════════════════════════════════════════")
        except KeyboardInterrupt:
            print("\n\x1b[38;5;203mExit.")
            sys.exit()

if __name__ == "__main__":
    main()
