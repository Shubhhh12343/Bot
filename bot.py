import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# Define a list of banks to process


# Initialize Chrome driver
driver = webdriver.Chrome()
time.sleep(2)
driver.get("http://theimperative.pythonanywhere.com")
driver.implicitly_wait(3)
driver.fullscreen_window()
driver.maximize_window()

email_input = driver.find_element(By.ID, "id_email")
email_input.send_keys("bipin.tatkare@atmstech.in")
time.sleep(2)

password_input = driver.find_element(By.ID, "id_password")
password_input.send_keys("Bipin@123")
time.sleep(2)

login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
time.sleep(2)

# home_url = driver.current_url

time.sleep(2)

banks = [
    {
        "name": "HDFC Bank",
        "value": "7c5f96bd-a150-443e-b854-92210b99e01f",
        "process_date": "05/06/2023",
        "montran_file": "57500000247971_2023-06-05_1686013618743.txt",
        "bank_file": "HDFC-7971_5.06.csv"
    },
    {
        "name": "Federal Bank",
        "value": "b794733f-a34e-44c1-ad05-a4dcb8ba927a",
        "process_date": "05/06/2023",
        "montran_file": "15810200017569_2023-06-05_1686013559960.txt",
        "bank_file": "FEDLECOL7569_5.06.xlsx"
    }
]

reconcile_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Reconcile']").click()
for bank in banks:
    # Select the bank
    bank_name = driver.find_element(By.ID, "id_bank_name")
    bank_select = Select(bank_name)
    bank_select.select_by_value(bank["value"])

    # Provide process date
    process_date = driver.find_element(By.ID, "id_process_date")
    process_date.clear()
    process_date.send_keys(bank["process_date"])
    time.sleep(2)

    # Upload Montran file
    montran_file = driver.find_element(By.ID, "id_montran_file")
    downloads_path = os.path.expanduser("~") + "/Downloads"
    montran_file_path = os.path.join(downloads_path, bank["montran_file"])
    montran_file.send_keys(montran_file_path)
    time.sleep(2)

    # Upload Bank statement file
    bank_file = driver.find_element(By.ID, "id_bank_statement")
    bank_file_path = os.path.join(downloads_path, bank["bank_file"])
    bank_file.send_keys(bank_file_path)
    time.sleep(2)

    # Submit the form
    submit_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submit_btn.click()
    time.sleep(2)

    # Approve the form
    approve_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Approve']")
    approve_btn.click()
    time.sleep(2)

    
