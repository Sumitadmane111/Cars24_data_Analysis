#Import the required libraries or modules.
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np  # For NaN values

# Initialize the webdriver
driver = webdriver.Firefox()

# List of cities to scrape data from
Cities = ['delhi-ncr', 'mumbai']

for city in Cities:
    url = f'https://www.cars24.com/buy-used-cars-{city}/'
    driver.get(url)

    # Scroll to load more cars
    for i in range(25):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract car links
    final_list = []
    for div in soup.find_all('a', class_='IIJDn'):
        link_tag = div
        if link_tag:
            final_list.append(link_tag['href'])

    # Initialize the dictionary to store data
    car_data = {
        "Brand": [],
        "Car Model": [],
        "Car Name": [],
        "Car Variant": [],
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

    # Loop through each link and extract data
    for link in final_list:
        driver.get(link)
        time.sleep(2)  # Wait for the page to load

        try:
            lis_elements = driver.find_element(By.CLASS_NAME, "_36EKv").find_elements(By.TAG_NAME, "strong")
            lis_texts = [lis.text for lis in lis_elements]

            # Insert 'Manual' if lis_texts has exactly 9 elements
            if len(lis_texts) == 9:
                lis_texts.insert(6, 'Manual')

            try:
                car_data["Car Model"].append(lis_texts[1])
            except IndexError:
                car_data["Car Model"].append(np.nan)

            try:
                car_data["Registration ID"].append(lis_texts[2])
            except IndexError:
                car_data["Registration ID"].append(np.nan)

            try:
                car_data["Car Transmission"].append(lis_texts[6])
            except IndexError:
                car_data["Car Transmission"].append(np.nan)

            try:
                car_data["KM driven"].append(lis_texts[7])
            except IndexError:
                car_data["KM driven"].append(np.nan)

            try:
                car_data["Owner Type"].append(lis_texts[8])
            except IndexError:
                car_data["Owner Type"].append(np.nan)

            try:
                car_data["Fuel Type"].append(lis_texts[9])
            except IndexError:
                car_data["Fuel Type"].append(np.nan)

            try:
                car_price = driver.find_element(By.CLASS_NAME, "_2j-eI").find_element(By.CLASS_NAME, "text-right").find_element(By.CLASS_NAME, "_3i9_p").text
                car_data["Car Price"].append(car_price)
            except Exception as e:
                print(f"Error getting Car Price for link: {link}, Error: {str(e)}")
                car_data["Car Price"].append(np.nan)

            try:
                location = driver.find_element(By.CLASS_NAME, "_1Rvdw").find_element(By.TAG_NAME, "strong").text
                car_data["Location"].append(location)
            except Exception as e:
                print(f"Error getting Location for link: {link}, Error: {str(e)}")
                car_data["Location"].append(np.nan)

            try:
                emi = driver.find_element(By.CLASS_NAME, "_2j-eI").find_element(By.TAG_NAME, "strong").text
                car_data["Monthly EMI"].append(emi)
            except Exception as e:
                print(f"Error getting Monthly EMI for link: {link}, Error: {str(e)}")
                car_data["Monthly EMI"].append(np.nan)

            try:
                downPayment = driver.find_element(By.CLASS_NAME, "_2j-eI").find_element(By.TAG_NAME, "label").text
                car_data["Downpayment Amount"].append(downPayment)
            except Exception as e:
                print(f"Error getting Downpayment Amount for link: {link}, Error: {str(e)}")
                car_data["Downpayment Amount"].append(np.nan)

            try:
                brand_element = driver.find_element(By.CLASS_NAME, "_1bqW4").find_element(By.CLASS_NAME, "_2Ximl").text
                brand = brand_element.split()[1]
                car_data["Brand"].append(brand)
            except Exception as e:
                print(f"Error getting Brand for link: {link}, Error: {str(e)}")
                car_data["Brand"].append(np.nan)

            try:
                car_name_variant = driver.find_element(By.CLASS_NAME, "_1bqW4").find_element(By.CLASS_NAME, "_2Ximl").text.split()
                car_name = ' '.join(car_name_variant[2:])  # Join first two elements for Car Name
                car_variant = ' '.join(car_name_variant[2:])  # Join remaining elements for Car Variant
                car_data["Car Name"].append(car_name)
                car_data["Car Variant"].append(car_variant)
            except Exception as e:
                print(f"Error getting Car Name and Car Variant for link: {link}, Error: {str(e)}")
                car_data["Car Name"].append(np.nan)
                car_data["Car Variant"].append(np.nan)

        except Exception as e:
            print(f"Error occurred for link: {link}, Error: {str(e)}")

    # Convert dictionary to DataFrame
    df = pd.DataFrame(car_data)

    # Print or save the DataFrame
    print(df)
    # Save the DataFrame to a CSV file
    df.to_csv(f'cars24_{city}.csv', index=False)

# Close the driver
driver.quit()
