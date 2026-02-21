from sc import pilot
import time
from PIL import Image
from utils.screens import screenshots_different, screenshots_color_different
import pyperclip
import json

from cursor_positions import dismiss_submit_alert,annotation_image,dismiss_filler, submit_button, annotation_image_download_option, annotation_title_bar, annotation_barcode, popup_save_button, brave_download_button, first_download_item, annotation_first_field, chatgpt_screen_center, annotation_country_one_option, close_download, extension_position, form_filler_input, form_filler_submit

def switch_to_annotation_tab():
    pilot.moveTo(annotation_title_bar,duration=0.05)
    pilot.click()
    time.sleep(0.05)
    return True

def download_image():
    pilot.moveTo(annotation_image,duration=0.1)
    pilot.rightClick()
    time.sleep(0.5)
    pilot.moveTo(annotation_image_download_option,duration=0.2)
    time.sleep(0.3)
    pilot.click()
    time.sleep(0.5)
    # Check if download popup opened
    region=467,427,100,25
    sc=pilot.screenshot(region=region)
    saved=Image.open("trainings/download_popup_save_btn.jpg")
    diff=screenshots_different(saved,sc)
    while diff<=80:
        print(f"Download popup not yet visible: {diff}")
        time.sleep(0.2)
        sc=pilot.screenshot(region=region)
        diff=screenshots_different(saved,sc)

    pilot.moveTo(popup_save_button, duration=0.2)
    pilot.click()
    time.sleep(1)
    return True

def take_ss():
    time.sleep(1)
    region=342,80,313,60
    pilot.screenshot(region=region).save("sam.png")
    return True

def close_download_popup():
    time.sleep(0.5)
    pilot.moveTo(close_download,duration=0.08)
    pilot.click()
    pilot.click()    

def drag_download():
    time.sleep(0.3)
    pilot.click()
    # Open download popup
    #  , first_download_item, chatgpt_screen_center
    pilot.moveTo(brave_download_button,duration=0.2)
    pilot.click()
    time.sleep(0.2)
    pilot.moveTo(first_download_item,duration=0.1)
    time.sleep(0.2)
    pilot.dragTo(chatgpt_screen_center,duration=0.5, button="left")
    return True


def submit_form():
    time.sleep(1)
    pilot.moveTo(submit_button)
    pilot.click()
    time.sleep(2)
    pilot.moveTo(dismiss_submit_alert,duration=0.05)
    pilot.click()
    return True


def submit_data():
    pilot.moveTo(extension_position, duration=0.05)
    pilot.click()
    time.sleep(0.5)
    pilot.moveTo(form_filler_input,duration=0.05)
    pilot.click()
    time.sleep(0.5)
    copied_text = pyperclip.paste()
    if "You are a taxonomist" in copied_text:
        return False
    pilot.hotkey("ctrl", "v")
    #pilot.write(copied_text, interval=0.001)
    time.sleep(1)
    pyperclip.copy("")
    pilot.moveTo(form_filler_submit,duration=0.05)
    pilot.click()
    return True


