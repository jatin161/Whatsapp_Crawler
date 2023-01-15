#%%

import pandas as pd
import numpy as np
import dataframe_image as dfi
df = pd.DataFrame(np.random.randn(6, 6), columns=list('ABCDEF'))
df_styled =df.style.set_properties(**{'background-color': 'black',
                           'color': 'white',
                            'border-color': 'gray'
                          })
dfi.export(df_styled.hide_index(),r"whatsapp_test.png")


#%%

def send_message(mobile,message,filepath,CHROME_DATA_PATH):

    print("Whatsapp Bot Starting")
    # import os
    # os.system("taskkill /im chromedriver.exe /t /f")
    
    from datetime import datetime
    from selenium import webdriver
    from selenium.webdriver.common import keys  
    import time
    import os

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service

    #from config import CHROME_DATA_PATH 

    from datetime import datetime
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location ="C:\Program Files\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument(CHROME_DATA_PATH)
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(r"D:\Whatsapp\chromedriver.exe"),options=chrome_options)
    driver.get('https://web.whatsapp.com/')
    from datetime import datetime
    if ((datetime.now().hour==9) or (datetime.now().hour==18)):
        time.sleep(105)
    else :
        time.sleep(10)
    search_box=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]")
    search_box.send_keys(mobile) 
    time.sleep(2)
    

    driver.find_element_by_xpath('//*[@title="{}"]'.format(mobile)).click()#
    
    message_box=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message_box.send_keys(message) 
    time.sleep(2)
    
    
    attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
    attachment_box.click()

    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)

    time.sleep(10)
    
    send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
    send_button.click()
    # filepath=r"C:\Users\Administrator\Desktop\Schedulers\Whatsapp Bot\whatsapp_test.png"
    # send_message("Whatsapp Testing","Hi Team - Testing From VDI",filepath)
    print("Message Sent Successfully through Whatsapp Bot at",datetime.now())

    time.sleep(50)
    driver.quit()




# %%
from config import CHROME_DATA_PATH
filepath=r"D:\Whatsapp\mytable.png"
send_message("Whatsapp Testing","*Automated Message is shared to your Friend*",filepath,CHROME_DATA_PATH)
    
