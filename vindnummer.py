from tkinter import *
from selenium.webdriver.common.keys import Keys
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.filedialog
import pyautogui
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
import threading
from selenium.common.exceptions import TimeoutException
from tkinter import messagebox
global acontr
global bcontr
global ccontr
acontr = False
bcontr = False
ccontr = False
global acontr2
global bcontr2
global ccontr2
acontr2 = False
bcontr2 = False
ccontr2 = False
window = Tk()
window.title("vind nummer")
file = open("opsl.txt", "r")
global prog
prog = 0
global tes
tes = file.read().replace("\n", " ")
if tes:
    e3 = Label(window, text = tes)
    e3.grid(row=0,column=1)
else:
    e3 = Label(window, text = "")
    e3.grid(row=0,column=1)
file.close()
def clicked():

    path= tkinter.filedialog.askopenfilename(title="Kies een bestand", filetypes = (("exe","*.exe"),("all files","*.*")))
    e3.config(text = path)
    open('opsl.txt', 'w').close()
    file2 = open("opsl.txt", "w")
    n = file2.write(path)
    file2.close()
    file = open("opsl.txt", "r")
    global tes
    tes = file.read().replace("\n", " ")
    file.close()

btn = Button(window, text="Kies chromedriver bestand", command=clicked)
btn.grid(row=0,column=0)

lbl = Label(window, text="vul hier de stad in")
lbl.grid(column=0, row=1)
t = Text(window, height=20, width=40)
t.grid(column=0, row=2)

lbl2 = Label(window, text="vul hier de initialen in")
lbl2.grid(column=1, row=1)
t2 = Text(window, height=20, width=40)
t2.grid(column=1, row=2)

lbl3 = Label(window, text="vul hier de achternaam in")
lbl3.grid(column=2, row=1)
t3 = Text(window, height=20, width=40)
t3.grid(column=2, row=2)

lbl4 = Label(window, text="vul hier straat en huisnummer in")
lbl4.grid(column=3, row=1)
t4 = Text(window, height=20, width=40)
t4.grid(column=3, row=2)

def clicked2():
    global stad
    stad = t.get("1.0","end")
    stad = stad.splitlines()
    global init
    init = t2.get("1.0","end")
    init = init.splitlines()
    global naam
    naam = t3.get("1.0","end")
    naam = naam.splitlines()
    global straat
    straat = t4.get("1.0","end")
    straat = straat.splitlines()
    window.destroy()
btn = Button(window, text="start", command=clicked2)
btn.grid(row=3, column=3)

window.mainloop()
global p
global o
p = len(stad)
o = p + p
window2 = Tk()
window2.title("vind nummer")
progress=Progressbar(window2,orient='horizontal',mode='determinate',length=280, maximum=o)
progress['value']=0
progress.grid(column=0, row=0)
lk = Label(window2, text="0/"+str(o))
lk.grid(column=0,row=1)
def kopie():
    global telefnum
    global window3
    test = "\n".join(telefnum)
    window2.clipboard_clear()
    window2.clipboard_append (test)
def kopie2():
    global telefnum2
    global window3
    test = "\n".join(telefnum2)
    window2.clipboard_clear()
    window2.clipboard_append (test)
def eind():
    global telefnum
    global telefnum2
    global window3
    progress.destroy()
    lk.destroy()
    btn = Button(window2, text="kopie alle nummers van telefoongids", command=kopie)
    btn.grid(row=1, column=0)
    btn2 = Button(window2, text="kopie alle nummers van google", command=kopie2)
    btn2.grid(row=1, column=1)
def check():
    global p
    global acontr
    global bcontr
    global ccontr
    if p<501:
        if acontr == True:
            if acontr2 == True:
                eind()
    elif p<1001:
        if acontr == True:
            if acontr2 == True:
                if bcontr == True:
                    if bcontr2 == True:
                        eind()
    else:
        if acontr == True:
            if acontr2 == True:
                if bcontr == True:
                    if bcontr2 == True:
                        if ccontr == True:
                            if ccontr2 == True:
                                eind()
def telefoongids(i,maxi):
    try:
        global stad
        global p
        opt = Options()
        opt.add_argument("--headless")
        opt.add_argument('--no-sandbox')
        opt.add_argument('--no-proxy-server')
        opt.add_argument("--proxy-server='direct://'")
        opt.add_argument("--proxy-bypass-list=*")
        opt.add_argument('--window-size=1920,1080')  
        driver = webdriver.Chrome(options=opt, executable_path=tes)
        driver.get("https://www.detelefoongids.nl/de-jong-c-j/wp44490951/9-1/?sn=WP44490951")
        naam5 = driver.find_element_by_id('onetrust-accept-btn-handler')
        naam5.click()
        while i<maxi:
            global naam
            global init
            global o
            q = stad[i]
            if not q:
                global telefnum
                telefnum.insert(i,"")
                global prog
                prog = prog+1
                progress['value']=prog
                i = i+1
                lk.config(text = str(prog)+"/"+str(o))
            else:
                t = naam[i]
                r = init[i]
                w = WebDriverWait(driver, 10)
                w.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"test_what")))
                naam2 = driver.find_element_by_class_name('test_what')
                naam2.clear()
                naam2.send_keys(t + " "+ r)
                naam3 = driver.find_element_by_class_name('test_where')
                naam3.clear()
                naam3.send_keys(q)
                naam4 = driver.find_element(By.XPATH,'//button[@data-reactid="26"]')
                naam4.click()
                time.sleep(0.1)
                w = WebDriverWait(driver, 6)
                w.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"h2")))
                try:
                    w = WebDriverWait(driver, 6)
                    w.until(expected_conditions.presence_of_element_located((By.XPATH,'//a[contains(.,"?sn=")]')))
                    driver.find_element(By.XPATH, '//a[contains(.,"?sn=")]').click()
                    tabs = driver.window_handles
                    driver.close()
                    driver.switch_to.window(tabs[1])
                    w = WebDriverWait(driver, 10)
                    w.until(expected_conditions.presence_of_element_located((By.XPATH,'//p[@data-reactid="87"]')))
                    tek = driver.find_element(By.XPATH,'//p[@data-reactid="87"]').text
                    #voeg tek toe aan global list dmv index en voeg 1 punt aan prog bar toe
                    telefnum.insert(i,tek)
                    prog = prog+1
                    i = i+1
                    progress['value']=prog
                    lk.config(text = str(prog)+"/"+str(o))
                except TimeoutException as e:
                    telefnum.insert(i,"")
                    prog = prog+1
                    i = i+1
                    driver.get("https://www.detelefoongids.nl/de-jong-c-j/wp44490951/9-1/?sn=WP44490951")
                    progress['value']=prog
                    lk.config(text = str(prog)+"/"+str(o))
        global acontr
        global bcontr
        global ccontr
        if i<501:
            acontr = True
        elif i<1001:
            bcontr = True
        else:
            ccontr = True
        driver.quit()
        check()
    except:
        messagebox.showerror("Error", "app gecrashed, probeer app te sluiten en opnieu op te starten door alle windows te sluiten")
        

def ggl(i,maxi):
    try:
        global o
        opt = Options()
        opt.add_argument("--headless")
        opt.add_argument('--no-sandbox')
        opt.add_argument('--no-proxy-server')
        opt.add_argument("--proxy-server='direct://'")
        opt.add_argument("--proxy-bypass-list=*")
        opt.add_argument('--window-size=1000,600')  
        driver = webdriver.Chrome(options=opt, executable_path=tes)
        driver.get("https://www.google.com/")
        ggl1 = driver.find_element_by_id('L2AGLb')
        ggl1.click()
        while i<maxi:
            time.sleep(1)
            global straat
            global stad
            global telefnum2
            global prog
            r = stad[i]
            if not r:
                telefnum2.insert(i,"")
                prog = prog+1
                progress['value']=prog
                i = i+1
                lk.config(text = str(prog)+"/"+str(o))
            else:
                t = straat[i]
                w = WebDriverWait(driver, 10)
                w.until(expected_conditions.presence_of_element_located((By.NAME,"q")))
                ggl2 = driver.find_element_by_name('q')
                ggl2.send_keys("a")
                ggl2.clear()
                ggl2.send_keys(t + " "+ r )
                ggl2.send_keys(Keys.ENTER)
                time.sleep(1)
                try:
                    w = WebDriverWait(driver, 6)
                    w.until(expected_conditions.presence_of_element_located((By.XPATH,'//h5')))
                    driver.find_element_by_tag_name("h5").click()
                    time.sleep(1)
                    w.until(expected_conditions.presence_of_element_located((By.XPATH,'.//span[@class = "LrzXr zdqRlf kno-fv"]')))
                    teks = driver.find_element_by_xpath('.//span[@class = "LrzXr zdqRlf kno-fv"]').text
                    telefnum2.insert(i,teks)
                    prog = prog+1
                    progress['value']=prog
                    i = i+1
                    lk.config(text = str(prog)+"/"+str(o))
                except TimeoutException as e:
                    telefnum2.insert(i,"")
                    prog = prog+1
                    progress['value']=prog
                    i = i+1
                    lk.config(text = str(prog)+"/"+str(o))
        global acontr2
        global bcontr2
        global ccontr2
        if i<501:
            acontr2 = True
        elif i<1001:
            bcontr2 = True
        else:
            ccontr2 = True
        driver.quit()
        check()
    except:
        messagebox.showerror("Error", "app gecrashed, probeer app te sluiten en opnieuw op te starten door alle windows te sluiten")    
    
def hoofd():
    global telefnum
    global telefnum2
    global stad
    global p
    telefnum2 = []
    telefnum = []
    if p<501:
        a = threading.Thread(target=telefoongids, name='a', daemon=True, args=(0,p))
        a.start()
        d = threading.Thread(target=ggl, name='d', daemon=True, args=(0,p))
        d.start()
    else:
        a = threading.Thread(target=telefoongids, name='a', daemon=True, args=(0,500))
        a.start()
        d = threading.Thread(target=ggl, name='d', daemon=True, args=(0,500))
        d.start()
    if p<1001:
        if p>500:
            b = threading.Thread(target=telefoongids, name='b', daemon=True, args=(500,p))
            b.start()
            e = threading.Thread(target=ggl, name='e', daemon=True, args=(500,p))
            e.start()
    else:
        b = threading.Thread(target=telefoongids, name='b', daemon=True, args=(500,1000))
        b.start()
        e = threading.Thread(target=ggl, name='e', daemon=True, args=(500,1000))
        e.start()
    if p<1501:
        if p>1000:
            c = threading.Thread(target=telefoongids, name='c', daemon=True, args=(1000,p))
            c.start()
            f = threading.Thread(target=ggl, name='e', daemon=True, args=(1000,p))
            f.start()
    else:
        c = threading.Thread(target=telefoongids, name='c', daemon=True, args=(1000,1500))
        c.start()
        f = threading.Thread(target=ggl, name='e', daemon=True, args=(1000,1500))
        f.start()
    #e = threading.Thread(target=telefoongids, name='e', daemon=True, args=(0,40))
    #f = threading.Thread(target=telefoongids, name='f', daemon=True, args=(0,40))
    #a.start()
    #b.start()
    #c.start()
    #d.start()
    #e.start()
    #f.start()
    
hoofd()
window2.mainloop()
    


