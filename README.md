# Cars24_data_Analysis
Analyzed car listings from the Cars24 website across different cities to identify market trends and insights for strategic planning.
# Cars24
Level:1
To scrape the data from the Cars24 website we have used Beautifulsoups and Selenium library in Python.

Level 2: 
To clean the datasets after scraping according to the requirement we have used the Pandas library.

Level 3:
To Visualise the data with some insights we have used the matplotlib and seaborn libraries from Python. We have also used Tableau for better visualization.

Requirements: 

Table 1: `Cars24 Data` 
Attributes required in the table
1. **`Brand**:`
    - *Data Type*: String
    - *Description*: The brand or manufacturer of the used car.
2. **`Car Model**:`
    - *Data Type*: String
    - *Description*: The model of the used car.
3. **`Car Name**:`
    - *Data Type*: String
    - *Description*: The name or make of the used car.
4. **`Car Variant**:`
    - *Data Type*: String
    - *Description*: The specific variant or version of the used car.
5. **`Car Transmission**:`
    - *Data Type*: String
    - *Description*: The type of transmission system in the used car.
6. **`KM Driven**:`
    - *Data Type*: Integer
    - *Description*: The total distance the car has been driven.
7. **`Owner Type**:`
    - *Data Type*: String
    - *Description*: The type of car owner (e.g., first owner, second owner).
8. **`Fuel Type**:`
    - *Data Type*: String
    - *Description*: The type of fuel the used car operates on.
9. **`Registration ID**:`
    - *Data Type*: String
    - *Description*: The unique registration ID of the used car.
10. **`Monthly EMI**:`
    - *Data Type*: Float or String
    - *Description*: The monthly Equated Monthly Installment for the used car.
11. **`Car Price**:`
    - *Data Type*: Float or String
    - *Description*: The total price of the used car.
12. **`Downpayment Amount**:`
    - *Data Type*: Float or String
    - *Description*: The initial downpayment amount for the used car.
13. **`Location**:`
    - *Data Type*: String
    - *Description*: The location or city where the used car is listed.

Step-by-step scraping:

To scrape these as a table we first get a link of each car from the location.
This is under the Link.py file.

To scrape the data inside the link found in the above is under the Cars Details.py file.

To automate this we have used the for loop and looped over each link and scraped then, saved the data as a pd.dataframe and into csv file.
The code is under the Cars24_delhi_ncr_data.py and Cars_mumbai_data.py and the csv file are cars24_delhi-ncr.csv and cars24_mumbai.csv

After we have the main.py file which has automated all the processes of scraping the data from all cities required using multiple for loop.

The csv files will be the same.

After this, we can do the data-cleaning process. The code is inside the Data_cleaning.py file and we will get two cleaned csv files named cleaned_cars24_delhi-ncr.csv, and cleaned_cars24_mumbai.csv.

The visualization is done with different Python libraries like Matplotlib, seaborn, pandas, and numpy in Project_Cars24. The Tableau screenshots are attached here:

![WhatsApp Image 2024-06-17 at 10 35 39 PM](https://github.com/Sandhya-16-m-64/Cars24/assets/172419475/0fedbfaa-9455-4d79-a2e5-4d9a60628b0d)![WhatsApp Image 2024-06-17 at 10 36 40 PM](https://github.com/Sandhya-16-m-64/Cars24/assets/172419475/7283ea7a-2407-4834-a3da-ece7a12c9376)
![WhatsApp Image 2024-06-17 at 10 37 31 PM](https://github.com/Sandhya-16-m-64/Cars24/assets/172419475/c276f4d5-bab4-420d-9e3a-62f85cce0a74)
![WhatsApp Image 2024-06-17 at 10 39 49 PM](https://github.com/Sandhya-16-m-64/Cars24/assets/172419475/369f888c-6a27-4c8b-b400-f777f6b36550)
![WhatsApp Image 2024-06-17 at 10 44 09 PM](https://github.com/Sandhya-16-m-64/Cars24/assets/172419475/b64f42ad-33a0-4c90-bfe6-806dbcfa1bf4)
![WhatsApp Image 2024-06-17 at 10 45 22 PM](https://github.com/Sandhya-16-m-64/Cars24/assets/172419475/0499e9d6-c51d-4462-ba06-8a5627f12f27)




