# Impledge_QA_DivyaGupta
Assignment - 2 (Impledge_QA)
## Exercise - 1 Automation
### Overview
This Python script automates the management of package types on a web-based platform using the Selenium WebDriver. It includes functionalities for logging into the system, adding a new package, deleting a package, and logging out.
### Approach
1. Login - Used `WebDriverWait` to ensure the page elements are fully loaded before interacting with them.
2. Adding a Package - Used CSS selectors and dynamic input generation for unique entries.
3. Deleting a Package - Used table traversal to locate a specific package by name and delete it.
4. Logout - Ensures a clean exit from the session to maintain application state integrity.
### Pre-requisites
1. Python - Ensure you have Python 3.6 or later installed.
2. WebDriver - Install the appropriate WebDriver for your browser. For example, chromedriver for Chrome.
3. Selenium Library: Install the Selenium library by running:
   
   ``` properties
   pip install selenium
   ```

4. Browser: Chrome is recommended for this script. Make sure you have the latest version.
5. System Access: Ensure the target web application (`https://ecs-qa.kloudship.com`) is accessible.
### Execution Steps
1. Run the Script
   - Execute the script from the command line:
     
     ``` properties
     python script_name.py
     ```
2. Perform Automated Tasks
   - The script will log into the platform.
   - Add a new package with a randomized name and dimensions.
   - Delete the package based on its name.
3. Close the Browser
   - The script will keep the browser open for inspection after the actions are completed. Press `Enter` in the console to close the browser.
## Exercise 2 Postman

### Overview
This Postman collection contains test cases for verifying and interacting with EasyPost's API. It includes two primary requests: verifying an address and retrieving shipment details. The tests ensure data accuracy and API response reliability while validating the expected business logic.

### Requests
1. Address - Verify
   - Method - POST
   - Endpoint - `https://api.easypost.com/v2/addresses?verify_strict[]=delivery`
   - Purpose - Validates address accuracy and ensures no errors in the response.
   - Tests Included - Response has no `error`. Status code is one of `200`, `201`, or `422`.
2. Get Shipment Details
   - Method - GET
   - Endpoint - `https://api.easypost.com/v2/shipments/shp_e0b570fd1d7d4b62bd206917eae5881a`
   - Purpose - Fetches details of a specific shipment.
   - Tests Included - The `retail_rate` matches expected values (`12`). `retail_rate` is greater than `list_rate`.

### Steps to Execute
1. Import - Load the JSON file into Postman using the Import button.
2. Set API Key - Add your EasyPost API key in the collection’s Authorization settings.
3. Run Requests:
   - Execute Address - Verify to validate the address.
   - Execute Get Shipment Details to fetch shipment data.
4. Review Tests - Check the Test Results tab to confirm all tests passed.

## Exercise 3 SQL

### Overview
This script updates and queries a healthcare database to manage and validate relationships between doctors, patients, and admissions. It ensures data consistency and extracts actionable insights such as identifying unlinked doctors or incomplete admissions.

### Approach
1. Modify data to align with business rules (e.g., reassign `attending_doctor_id`).
2. Use `JOIN` operations to analyze relationships between tables and identify discrepancies.
3. Ensure logical consistency across tables through updates and validation queries.

### Steps to Execute
1. Update Admissions Table:
   - Update the `attending_doctor_id` and `patient_id `values in the `Admissions` table using the provided `UPDATE` statements.
2. Validate Updates:
   - Run the `SELECT COUNT(*)` query to confirm that no admissions remain with `attending_doctor_id = 3`.
3. Run Queries:
   - Query 1: Fetch details of doctors with admissions by joining `doctors` and `admissions`.
   - Query 2: Fetch doctors with no admissions using a `LEFT JOIN` and filtering `NULL` records.
   - Query 3: Identify patients with incomplete admissions due to missing doctor details using a `JOIN`.
