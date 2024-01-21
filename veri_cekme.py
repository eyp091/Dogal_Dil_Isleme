from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

file = open("yeni_data_1", "w", encoding="utf-8")
file.close()

driver.get("https://www.trendyol.com/riccon/unisex-siyah-sneaker-0012072-p-37155275/yorumlar?boutiqueId=61&merchantId=180000")

time.sleep(3)

for i in range(1, 2):
    uni_path = f"/html/body/main/section/div/div/article/p" 

    try:
        uni_name = driver.find_element(By.XPATH, uni_path).text

        with open("yeni_data_1", "a", encoding="utf-8") as f:

         f.write(f"\n('{i} - {uni_name}  . ')")
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight-1500)")
        
        print(uni_name)
          
    except Exception as e:
        print(f"{i}. veri alınırken hata oluştu: {e}")

driver.quit()