from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
import json

# Create your tests here.
class SeleniumTests():

   @classmethod
   def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

   def testCRUDOperation(self):
     try:
       driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))        #This automatically install and loads the chrome driver
       driver.get('http://localhost:8000/login/')           #This redirects the chrome driver to this URL
       driver.execute_script("document.title = 'Hello, world!'")



       #This auto fiils the login page's text fields with the given username and password
       username_field = driver.find_element(By.ID, "id_username")
       password_field = driver.find_element(By.ID, "id_password")

       username_field.send_keys('ssahu')
       password_field.send_keys('123')


       #The submit button is clicked in the login form
       submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Log in']")

       submit_button.click()

       # Capture the redirect URL
       redirect_url = driver.current_url


       #This auto fills the form for adding the task details with the given values in the build-in function called send-keys and submits it
       driver.find_element(By.ID, "name1").send_keys('Morning Run')
       driver.find_element(By.ID, "date1").send_keys('30/05/2024')
       driver.find_element(By.ID, "startTime1").send_keys("12:30")
       driver.find_element(By.ID, "amountOfTime1").send_keys("04:00")
       driver.find_element(By.ID, "descriptionOfTheTask1").send_keys("Early morning run in the streets")
       driver.find_element(By.ID, "image").send_keys(os.path.abspath(
                                                             os.path.join(os.path.dirname(__file__), "..", "1000_F_601654907_FgISykN0GQp39MfRAlgg3IBmLDVIZYYk.jpg")))

       submit_button_to_add = driver.find_element(By.CSS_SELECTOR, "button[data-v-389b3d8a][type='submit']")

       driver.execute_script("arguments[0].click();", submit_button_to_add)



       #The update button on the added task is clicked, which redirects to the update form
       update_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Update']"))
       )

       driver.execute_script("arguments[0].click();", update_button)



       #The chrome driver auto-fills the update task form with the given values in the send_keys built-in function and submit it.
       driver.find_element(By.ID, "name1").send_keys("Swimming")

       driver.find_element(By.ID, "date1").send_keys("01/06/2024")

       driver.find_element(By.ID, "startTime1").send_keys("16:30")

       driver.find_element(By.ID, "amountOfTime1").send_keys("03:00")

       driver.find_element(By.ID, "descriptionOfTheTask1").send_keys("3 hours swimming at the sport centre")

       driver.find_element(By.ID, "image").send_keys(os.path.abspath(
                                                             os.path.join(os.path.dirname(__file__), "..", "photo-1622629797619-c100e3e67e2e.avif")))

       submit_button_to_update = driver.find_element(By.CSS_SELECTOR, "button[data-v-3ee9e199][type='submit']")

       driver.execute_script("arguments[0].click();", submit_button_to_update)



       #The delete button is clicked on the updated task
       delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Delete']"))
       )

       driver.execute_script("arguments[0].click();", delete_button)


       #The chrome driver redirects to the given URL path to access the Calorie tracker web page
       driver.get('http://localhost:5173/CalorieTracker')



       #The diet plan form gets auto-filled by the given values in the build-in function called send_keys.
       #Once that is done it submits it, by clicking the submit button called Fetch the amount of calories intaken.
       driver.find_element(By.ID, "query").send_keys('pasta')

       driver.find_element(By.ID, "amountOfCalories").send_keys("12000")

       driver.find_element(By.ID, "dietType").send_keys("high-fiber")

       driver.find_element(By.ID, "mealType").send_keys("lunch")

       submit_button_for_the_diet_plan = driver.find_element(By.CSS_SELECTOR, "button[data-v-023bece8][type='submit']")

       driver.execute_script("arguments[0].click();", submit_button_for_the_diet_plan)

       driver.find_element(By.ID, "listOfFoodItems").send_keys("1 packet of cookies")

       retrieve_button = driver.find_element(By.XPATH, '//button[normalize-space()="Fetch the amount of calories intaken"]')

       driver.execute_script("arguments[0].click();", retrieve_button)



       #The chrome driver clicks the button called See your Calorie History to redirect to the Calorie History web page.
       calorie_history_button = driver.find_element(By.XPATH, '//button[normalize-space()="See your Calorie Histroy"]')

       driver.execute_script("arguments[0].click();", calorie_history_button)



       #The chrome driver clicks the button called Fetch all the calorie consumption details at all the dates to display the table that contains the amount of calories at which dates.
       fetch_calorie_history = driver.find_element(By.XPATH, '//button[normalize-space()="Fetch all the calorie consumption details at all the dates"]')

       driver.execute_script("arguments[0].click();", fetch_calorie_history)



       #The chrome driver then redirects to the different given URL to access the web page where the user can fetch Youtube exercising videos.
       driver.get('http://localhost:5173/FetchingExercisingVideos')



       #The form for fetching the exercising videos is auto-filled with the given values in the build-in function called send_keys and click the submit button.
       driver.find_element(By.ID, "queryForVideos").send_keys("30 minutes run")

       submit_button_exercising_videos = driver.find_element(By.CSS_SELECTOR, "button[data-v-4463101b][type='submit']")

       driver.execute_script("arguments[0].click();", submit_button_exercising_videos)


       #The chrome driver is turned off
       driver.quit()


       #A message is returned stating that tests of all the functionalities in the prototype have passed
       return "The tests of all the functionalities have passed"

     except Exception as e:

       #From the try and catch block, if there is an error during the automated testing execution the error message is returned
       return str(e)