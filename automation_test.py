from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Constants
URL = "https://ecs-qa.kloudship.com"
USERNAME = "kloudship.qa.automation@mailinator.com"
PASSWORD = "Password1"

def login(driver):
    print("Navigating to login page...")
    driver.get(URL)
    
    try:
        print("Waiting for the username field...")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        print("Entering username and password...")
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "loginButton").click()
        
        # Wait to ensure the login process is successful
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logoutButton")))
        print("Login successful!")
    except Exception as e:
        print(f"Error during login: {e}")

def add_package(driver):
    try:
        # Navigate to Package Types
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Package Types"))).click()
        print("Navigated to Package Types.")
        
        # Click 'Add Manually'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Add Manually']"))).click()
        print("Clicked 'Add Manually' button.")
        
        # Fill in package details
        first_name = "John"
        last_name = "Doe"
        dimensions = random.randint(1, 19)
        
        driver.find_element(By.ID, "name").send_keys(f"{first_name}_{last_name}")
        driver.find_element(By.ID, "dimensions").send_keys(str(dimensions))
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print(f"Package added: {first_name}_{last_name}, Dimensions: {dimensions}")
    except Exception as e:
        print(f"Error during package addition: {e}")

def delete_package(driver, package_name):
    try:
        # Navigate to Package Types
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Package Types"))).click()
        print("Navigated to Package Types.")
        
        # Locate and delete the package
        packages = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for package in packages:
            if package_name in package.text:
                package.find_element(By.CSS_SELECTOR, "button[title='Delete']").click()
                driver.find_element(By.CSS_SELECTOR, "button[title='Confirm']").click()
                print(f"Package deleted: {package_name}")
                break
    except Exception as e:
        print(f"Error during package deletion: {e}")

def logout(driver):
    try:
        driver.find_element(By.ID, "logoutButton").click()
        print("Logged out successfully.")
    except Exception as e:
        print(f"Error during logout: {e}")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        # Test Case 1: Add Package
        login(driver)
        add_package(driver)
        
        # Test Case 2: Delete Package
        delete_package(driver, "John_Doe")
        
        print("All actions completed. Keeping the browser open...")
        input("Press Enter to quit the browser.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        print("Closing the browser...")
        driver.quit()
