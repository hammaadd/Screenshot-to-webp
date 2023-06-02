import streamlit as st
from selenium import webdriver
from time import sleep
from pathlib import Path
from PIL import Image

st.markdown(
        """
        ### This app let you take screenshot and automatically convert screenshot of any website to webp
    """
    )
#Input field to take url
url_ss = st.text_input("Add Url of site you want to take screenshot of.", key=None, type="default", placeholder="Url of the website eg: https://www.google.com", label_visibility="visible")
#Input Field to take name for screenshot
name_of_site = st.text_input("Add name of the screenshot *This is optional.", key=None, type="default", placeholder="Google", label_visibility="visible")
#Input Field to add wait time after link is opened *Max Value is 60
sleep_time = st.number_input("Add Wait Time in seconds After Link is opened how long It should wait to take screenshot",min_value=1, max_value=60, key=None, value=1 ,step=1, label_visibility="visible")

#Button to take screenshot
result = st.button("Take Screenshot")

#Function to declare headless chrome driver used to access website
def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--window-size=1920, 947")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

#Call to function to declare headless chrome
driver = web_driver()


#Function to convert screenshot to webp
def convert_to_webp(source, title):
    if(title == ""): #Check if title is not empty
        title = "Screenshot"
    destination = f"screenshots/{title}.webp"

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination #returning path to created image
if result and url_ss:
    url = url_ss
    driver.get(url) #accessing the given url
    title = driver.title
    
    sleep(1)
    driver.get_screenshot_as_file("screenshots/screenshot.png") #screenshot taken of the given url
    check = convert_to_webp(Path('screenshots/screenshot.png'), name_of_site)
    if check:
        image = Image.open(check)
        st.image(image, caption=f'Screenshot of website {title}')
else:
    st.markdown("""
                    ### Add Url to proceed
                    """)
    