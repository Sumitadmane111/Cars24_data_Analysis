#Import the required libraries or modules.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Step 1: Driver ready to scrape the URL.
driver = webdriver.Firefox()
url = 'https://www.cars24.com/buy-used-tata-punch-2022-cars-new-delhi-10007934792/'
driver.get(url)
time.sleep(5)

#Step 2: Create a Directionary to store the data.
car_data = {
    "Brand": [],
    "Car Model": [],
    "Car Name": [],
    "Car Varient": [],
    "Car Transmission": [],
    "KM driven": [],
    "Owner Type": [],
    "Fuel Type": [],
    "Registration ID": [],
    "Monthly EMI": [],
    "Car Price": [],
    "Downpayment Amount": [],
    "Location": []
}

#Step 2: Use Selenium to scrape the data from the URL and add those data to the specified key of the dictionary.
lis_texts = [lis.text for lis in driver.find_element(By.CLASS_NAME, "_36EKv").find_elements(By.TAG_NAME, "strong")]
car_data["Car Model"].append(lis_texts[1])
car_data["Registration ID"].append(lis_texts[2])
car_data["Car Transmission"].append(lis_texts[6])
car_data["KM driven"].append(lis_texts[7])
car_data["Owner Type"].append(lis_texts[8])
car_data["Fuel Type"].append(lis_texts[9])

car_price = driver.find_element(By.CLASS_NAME, "_2j-eI").find_element(By.CLASS_NAME, "text-right").find_element(By.CLASS_NAME, "_3i9_p").text
car_data["Car Price"].append(car_price)

location = driver.find_element(By.CLASS_NAME, "_1Rvdw").find_element(By.TAG_NAME, "strong").text
car_data["Location"].append(location)

emi = driver.find_element(By.CLASS_NAME, "_2j-eI").find_element(By.TAG_NAME, "strong").text
car_data["Monthly EMI"].append(emi)

downPayment = driver.find_element(By.CLASS_NAME, "_2j-eI").find_element(By.TAG_NAME, "label").text
car_data["Downpayment Amount"].append(downPayment)

brand_element = driver.find_element(By.CLASS_NAME, "_1bqW4").find_element(By.CLASS_NAME, "_2Ximl").text
brand = brand_element.split()[1]
car_data["Brand"].append(brand)

driver.quit()

#Print to see the dictionary
print(car_data)
