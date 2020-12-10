from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import threading
import time
import sys
import os
import tkinter as tk


def main(input1,input2,input3,input4,input5):
    # input1 = int(sys.argv[1])   # number of whole fullscreen pages per post
    # input2 = float(sys.argv[2]) # sleep time per loop
    # input3 = int(sys.argv[3])   # jump pixels
    # input4 = sys.argv[4]        # URL
    # input5 = sys.argv[5]        # Video File Name
    
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome("./chromedriver.exe",options=options)

    driver.get(input4)

    driver.set_window_size(750, 1000)
    driver.set_window_position(0, 0)

    def thread_function():
        os.system(f"ffmpeg -f gdigrab -show_region 1 -framerate 40 -video_size 960x1000 -offset_x 0 -offset_y 0 -i desktop -t 00:00:15 {input5}.mp4")

    x = threading.Thread(target=thread_function, args=())
    x.start()
    
    for i in range(0,input1*880,input3+1):  
        time.sleep(input2)
        driver.execute_script(f"window.scrollTo({i},{i+input3})")
        
    time.sleep(3)
    driver.close()

page_w = 450
page_h = 350

root= tk.Tk() 
root.wm_iconbitmap('logo.ico')
root.wm_title('   فرامتن')
canvas1 = tk.Canvas(root, width = page_w, height = page_h,relief = 'raised') 
canvas1.pack()


first_input = page_w - 380


label1 = tk.Label(root, text='ضبط کننده فیلم تبلیغ')
label1.config(font=('helvetica', 14))
canvas1.create_window(page_w/2, 25, window=label1)

first_div_y = 90

label2 = tk.Label(root, text=':تنظیمات ریکوردر')
label2.config(font=('helvetica', 10))
canvas1.create_window(page_w/2, first_div_y, window=label2)




label2 = tk.Label(root, text='تعداد صفحات')
label2.config(font=('helvetica', 8))
canvas1.create_window(first_input, first_div_y + 30, window=label2)
entry1 = tk.Entry (root)
entry1.config(width=(8))
canvas1.create_window(first_input, first_div_y + 50, window=entry1)

label2 = tk.Label(root, text='سرعت')
label2.config(font=('helvetica', 8))
canvas1.create_window(first_input + 80, first_div_y + 30, window=label2)
entry2 = tk.Entry (root)
entry2.config(width=(8))
canvas1.create_window(first_input + 80, first_div_y + 50, window=entry2)

label2 = tk.Label(root, text='تعداد پیکسل')
label2.config(font=('helvetica', 8))
canvas1.create_window(first_input + 160, first_div_y + 30, window=label2)
entry3 = tk.Entry (root)
entry3.config(width=(8))
canvas1.create_window(first_input + 160, first_div_y + 50, window=entry3)

label2 = tk.Label(root, text='لینک')
label2.config(font=('helvetica', 8))
canvas1.create_window(first_input + 240, first_div_y + 30, window=label2)
entry4 = tk.Entry (root)
entry4.config(width=(8))
canvas1.create_window(first_input + 240, first_div_y + 50, window=entry4)

label2 = tk.Label(root, text='نام خروجی')
label2.config(font=('helvetica', 8))
canvas1.create_window(first_input + 320, first_div_y + 30, window=label2)
entry5 = tk.Entry (root)
entry5.config(width=(8))
canvas1.create_window(first_input + 320, first_div_y + 50, window=entry5)

# input1 = int(sys.argv[1])   # number of whole fullscreen pages per post
# input2 = float(sys.argv[2]) # sleep time per loop
# input3 = int(sys.argv[3])   # jump pixels
# input4 = entry4        # URL
# input5 = entry5        # Video File Name

button1 = tk.Button (root, text='شروع',command=lambda:main(int(entry1.get()),float(entry2.get()),int(entry3.get()),entry4.get(),entry5.get()),bg='green',fg='white')
button2 = tk.Button (root, text='توقف',command=main,bg='green',fg='white')
# button3 = tk.Button (root, text='Config',command=main,bg='green',fg='white')
button4 = tk.Button (root, text='خروج',command=exit,bg='green',fg='white')



canvas1.create_window(page_w/2, first_div_y + 100, window=button1)
canvas1.create_window(page_w/2, first_div_y + 140, window=button2)
# canvas1.create_window(170, 140, window=button3)
canvas1.create_window(page_w/2, first_div_y + 210, window=button4)

root.mainloop()




