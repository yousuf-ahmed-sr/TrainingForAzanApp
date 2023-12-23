from selenium import webdriver
from selenium.webdriver.common.by import By

all_headphones = []

# Start a new instance of Chrome
driver = webdriver.Chrome()

# Navigate to Amazon's search results page
driver.get('https://www.amazon.com/')
search_id = driver.find_element(By.ID, 'twotabsearchtextbox')
search_id.send_keys('noise canceling headphones')
search_id.submit()
elements = driver.find_elements(By.CLASS_NAME, 's-image')

for element in elements:
    name = element.get_attribute('alt')
    if name:
        all_headphones.append(name)

jbl_headphones = []  # Create a list to store JBL headphones

for item in all_headphones:
    if 'jbl' in item.lower():  # Use item.lower() to make it case-insensitive
        jbl_headphones.append(item)
print(f"{jbl_headphones}")



# Create an instance of the 'a-price-whole' class or object
# Use Selenium to find and extract the element with the 'a-price-whole' class
price_element = driver.find_element(By.CLASS_NAME, 'a-price-whole')

# Extract the text content from the element
price = price_element.text

# Print the extracted price
print(f'Price: {price}')
