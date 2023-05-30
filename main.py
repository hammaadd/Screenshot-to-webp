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
url_ss = st.text_input("Add Url of site you want to take screenshot of.", key=None, type="default", placeholder="Url of the website eg: https://www.google.com", label_visibility="visible")
name_of_site = st.text_input("Add name of the screenshot *This is optional.", key=None, type="default", placeholder="Google", label_visibility="visible")
result = st.button("Take Screenshot")

def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 947")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

driver = web_driver()

def convert_to_webp(source, title):
    if(title == ""):
        title = "Screenshot"
    #destination = source.with_suffix(".webp")
    destination = f"screenshots/{title}.webp"

    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp

    return destination
if result and url_ss:
    url = url_ss
    driver.get(url)
    title = driver.title
    
    sleep(1)
    driver.get_screenshot_as_file("screenshots/screenshot.png")
    check = convert_to_webp(Path('screenshots/screenshot.png'), name_of_site)
    if check:
        image = Image.open(check)
        st.image(image, caption=f'Screenshot of website {title}')
    