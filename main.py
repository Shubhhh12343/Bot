import time
import os 
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# Initialize Chrome driver
driver = webdriver.Chrome()
time.sleep(2)
driver.get("http://theimperative.pythonanywhere.com")
driver.implicitly_wait(3)
driver.fullscreen_window()
driver.maximize_window()     

email_input = driver.find_element(By.ID,"id_email")
email_input.send_keys("bipin.tatkare@atmstech.in")
time.sleep(2)

password_input = driver.find_element(By.ID, "id_password")
password_input.send_keys("Bipin@123")
time.sleep(2)

login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(2)

home_url = driver.current_url

reconcile_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Reconcile']").click()
time.sleep(2)


bank_name = driver.find_element(By.ID, "id_bank_name")
bank_select = Select(bank_name)
bank_select.select_by_value("7c5f96bd-a150-443e-b854-92210b99e01f")

process_date = driver.find_element(By.ID, "id_process_date")
process_date.send_keys("05/06/2023")
time.sleep(2)

montrain_file = driver.find_element(By.ID,"id_montran_file")
downloads_path = os.path.expanduser("~") + "/Downloads"
file_name = "57500000247971_2023-06-05_1686013618743.txt"
file_path = os.path.join(downloads_path, file_name)
montrain_file.send_keys(file_path)
time.sleep(2)

bank_file = driver.find_element(By.ID,"id_bank_statement")
downloads_path1 = os.path.expanduser("~") + "/Downloads"
file_name1 = "HDFC-7971_5.06.csv"
file_path1 = os.path.join(downloads_path1, file_name1)
bank_file.send_keys(file_path1)
time.sleep(2)

submit_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Submit']")
submit_btn.click()
time.sleep(2)

approve_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()
time.sleep(2)

view_btn = driver.find_element(By.XPATH, "//tbody/tr[1]/td[3]/a[1]").click()
time.sleep(4)

download_link = driver.find_element(By.XPATH, "//a[contains(text(),'media/')]").get_attribute("href")
driver.get(download_link)
time.sleep(5)

driver.back()
time.sleep(2)


reconcile_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Reconcile']").click()
time.sleep(2)
bank_name = driver.find_element(By.ID, "id_bank_name")
bank_select = Select(bank_name)
bank_select.select_by_value("b794733f-a34e-44c1-ad05-a4dcb8ba927a")

process_date = driver.find_element(By.ID, "id_process_date")
process_date.send_keys("05/06/2023")
time.sleep(2)

montrain_file = driver.find_element(By.ID,"id_montran_file")
downloads_path = os.path.expanduser("~") + "/Downloads"
file_name = "15810200017569_2023-06-05_1686013559960.txt"
file_path = os.path.join(downloads_path, file_name)
montrain_file.send_keys(file_path)
time.sleep(2)

bank_file = driver.find_element(By.ID,"id_bank_statement")
downloads_path1 = os.path.expanduser("~") + "/Downloads"
file_name1 = "FEDLECOL7569_5.06.xlsx"
file_path1 = os.path.join(downloads_path1, file_name1)
bank_file.send_keys(file_path1)
time.sleep(2)

submit_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Submit']")
submit_btn.click()
time.sleep(2)

approve_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Approve']").click()
time.sleep(2)

view_btn = driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/a[1]").click()
time.sleep(2)
download_link = driver.find_element(By.XPATH, "//a[contains(text(),'media/')]").get_attribute("href")
driver.get(download_link)
time.sleep(15)

driver.close()


