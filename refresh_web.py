from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#填寫課程上限＆課程代碼
Upper_limit= str(40)
code_in_school= "BA1935701"

#webdriver新版本設定，視窗最大化以關閉個人列表
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = 'https://querycourse.ntust.edu.tw/querycourse/#/'

#網站刷新行為
def web_refresh():
    driver.get(url)
    #代碼輸入
    course_code =driver.find_element(By.XPATH,'//*[@id="app"]/div[12]/main/div/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/input')
    course_code.click()
    course_code.send_keys(code_in_school)
    #搜尋按鈕
    search_buttom = driver.find_element(By.XPATH,'//button[@class="v-btn v-btn--block v-btn--round theme--light"]')
    search_buttom.click()
    #等待搜尋結果
    condition = WebDriverWait(driver, 1,0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[13]/main/div/div/div/div/div[5]/div[1]/table/tbody/tr/td[8]/span[1]'))
        )
    condition =  (condition.text[0]+condition.text[1])
    return(condition)
    

cond1= web_refresh()
#迴圈確認有無同學退選
while cond1 ==Upper_limit:
    print("無法加選")   
    cond1= web_refresh()
    
    if cond1 <Upper_limit:
        break   

print("趕快加簽")
        
    

