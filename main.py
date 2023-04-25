# Steg 1: Öppna cmd och skriv in cd C:\Program Files (x86)\Google\Chrome\Application
# Steg 2: skriv in detta: chrome.exe --remote-debugging-port=8989 --user-data-dir="C:\Selenium\Chrome_Test_Profile
# Steg 3: gå till https://rumble.com och logga in

# Setup
from selenium.webdriver.chrome import webdriver
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="C:\Selenium\chromedriver.exe",chrome_options=opt)

print(driver.title)

time.sleep(3)
driver.get("https://rumble.com/")

greenUpload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/button[1]")))
greenUpload_button.click()

time.sleep(15)
uploadVideoButton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/nav/div/div[3]/a[1]")))
uploadVideoButton.click()

videoTitle = "Motivational Speeches"
videoDescription = "Transform your life today by clicking here: https://linktr.ee/empowered_elevation ! Discover powerful tools and resources to help you reach your goals and achieve your dreams.  https://linktr.ee/empowered_elevation"
videoTags = "motivation, inspire, determination, success, achievement, goals, positivity, self-improvement, growth, progress, mindset, focus, discipline, persistence, perseverance, hard work, effort, dedication, passion, ambition"


def getFirstFile():
    # Set the path to the folder you want to get the first item from
    folder_path = "" # where your movies are at

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Get the first file in the folder
    first_file = files[0]

    # Get the name of the first file
    first_file_name = os.path.basename(first_file)

    first_file_path = os.path.join(folder_path, first_file)

    print("First file in folder:", first_file)
    print("Name of first file:", first_file_name)
    return first_file_path

def deleteTheFile(nameOfFileAndPath):
    # delete the film from folder
    time.sleep(2)
    print("Deleting the movie from folder")
    os.remove(nameOfFileAndPath)


uploads = 0
# The worker
while(True):
    print("New upload started!")
    driver.get("https://rumble.com/upload.php")

    time.sleep(5)
    while(True):

        file_path = getFirstFile()

        try:
            # Find the file input element and upload the first file
            file_input = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'Filedata')))
            file_input.send_keys(file_path)

            time.sleep(5)
        except:
            print("Unable to uploadfile")
            break

        try:
            videoTitle_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/section/form[1]/div/div[2]/input[1]')))
            videoTitle_input.send_keys(videoTitle)
            time.sleep(5)
        except:
            print("Unable to add Video Title")
            break

        try:
            video_description_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/section/form[1]/div/div[2]/textarea')))
            video_description_input.send_keys(videoDescription)
            time.sleep(5)
        except:
            print("Unable to add Video Description")
            break

        try:
            videoTag_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/section/form[1]/div/div[2]/input[2]')))
            videoTag_input.send_keys(videoTags)
            time.sleep(5)
        except:
            print("Unable to add Video Tag")
            break

        try:
            # Upload button
            upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/section/form[1]/div/div[2]/div[7]/input')))
            upload_button.click()
            time.sleep(5)
        except:
            print("Unable to click on upload button")
            break
        """
        try:
            #Rumble Only
            rumbleOnly = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/section/form[2]/div/div[2]/div[3]/div/a')))
            rumbleOnly.click()
            time.sleep(5)
        except:
            print("Unable to click on Rumble Only")
            break
        """
        try:
            #Open For all youtube rumble and more
            rumbleOnly = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/section/form[2]/div/div[2]/div[1]/div/a')))
            rumbleOnly.click()
            time.sleep(5)
        except:
            print("Unable to click on Video management (Exclusive)")
            try:
                # Rumble Only
                rumbleOnly = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '/html/body/main/div/div/div[2]/section/form[2]/div/div[2]/div[3]/div/a')))
                rumbleOnly.click()
                time.sleep(5)
            except:
                print("Unable to click on Rumble Only")
                break


        try:
            # Terms and conditions
            # You have not signed an exclusive agreement with any other parties.
            termsandcoditions1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/section/form[2]/div/div[7]/div[1]')))
            termsandcoditions1.click()
            time.sleep(5)
        except:
            print("Unable to click on Terms and conditions step 1")
            break

        try:
            # Check here if you agree to our terms of service.
            termsandcoditions2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/section/form[2]/div/div[7]/div[2]')))
            termsandcoditions2.click()
            time.sleep(5)
        except:
            print("Unable to click on Terms and conditions step 2")
            break

        try:
            # Submit
            submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/section/form[2]/div/div[11]/input[1]')))
            submit_button.click()
            time.sleep(5)

            print("Upload complete!")
            time.sleep(5)

            # Delete the file that was used
            deleteTheFile(file_path)
            time.sleep(5)
            # back to start
            driver.get("https://rumble.com/upload.php")
            uploads += 1
            print(f"Their have been {uploads} uploads so far")
        except:
            print("Unable to click on Submit button")
            break


