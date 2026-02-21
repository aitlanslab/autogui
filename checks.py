from sc import pilot
from utils.screens import screenshots_color_different,screenshots_different, screenshot_change_percent
from cursor_positions import image_starting, reload_btn, annotation_reload, annotation_menu_btn, menu_btn
import time
from gpt_tab import tabs_reload
from utils.log import create_log
from PIL import Image
from PIL import ImageChops
import numpy as np

def img_different(img1, img2, thresh=10):
    if img1.size != img2.size:
        raise ValueError("Images must be same size")

    img1 = img1.convert("RGB")
    img2 = img2.convert("RGB")

    diff = ImageChops.difference(img1, img2)
    diff_np = np.array(diff).max(axis=2)  # 0..255 per pixel

    changed_pixels = np.count_nonzero(diff_np > thresh)
    total_pixels = diff_np.size

    return (changed_pixels / total_pixels) * 100




def reload_tab():
    time.sleep(1)
    pilot.moveTo(reload_btn,duration=1)
    pilot.click()
    return True

def gpt_attachment_in_position():
    region=838, 507, 70,70
    saved_img=Image.open("trainings/gpt_attachment.jpg")
    for i in range(5):
        new_img=pilot.screenshot(region=region)
        res=img_different(new_img,saved_img)
        if float(res)>10:
            create_log({"function":"gpt_attachment_in_position","success":True,"diff":res})
            return True
        create_log({"function":"gpt_attachment_in_position","success":False,"diff":res})
        time.sleep(1)
    return False

def annotation_loaded():
    region=28,176,100,50
    sc1=pilot.screenshot(region=region)
    for i in range(300):
        sc2=pilot.screenshot(region=region)
        diff=screenshots_different(sc1,sc2)
        if diff>=50 and diff<=100:
            print("Changes Loaded")
            create_log({"function":"annotation_loaded","success":True})
            return True
        if diff==100:
            print("Wait")
        create_log({"function":"annotation_loaded","success":False}) 
        time.sleep(1)
    return True

def is_loggedin():
    region=223,114,300,300
    current_sc=pilot.screenshot(region=region)
    logic_sc=Image.open("trainings/login_screen.jpg")
    diff=screenshots_different(logic_sc,current_sc)
    is_login=False
    if diff>=60:
        is_login=True

def load_annotation():
    #region=45,493,25,25
    region=29,181,200,200
    saved_btn=Image.open("trainings/blank.jpg")
    for i in range(30):
        plus_btn=pilot.screenshot(region=region)
        
        res=img_different(plus_btn,saved_btn)
        print("Blank image diff")
        print(res)
        
        if float(res)>=10:
            create_log({"function":"load_annotation","success":True,"diff":res})
            return True

        create_log({"function":"load_annotation","success":False,"diff":res})
        time.sleep(1)
    return False

error_count=0
def load_chatgpt():
    #region=45,493,25,25
    region=1060,283,60,90
    saved=Image.open("trainings/chatgpt_error.jpg")
    for i in range(3):
        sc=pilot.screenshot(region=region)
        diff=screenshots_color_different(saved,sc)
        if diff>=30:
            return True
        tabs_reload()
        time.sleep(2)
    return False




def annotation_tab_in_position():
    region=17,4,150,20
    sc=None
    diff=0
    saved=Image.open("trainings/annotation_tab.jpg")
    for i in range(50):
        sc=pilot.screenshot(region=region)
        diff=screenshots_different(saved,sc)
        if diff<100:
            create_log({"function":"annotation_tab_in_position","success":True,"diff":diff})
            return True
        create_log({"function":"annotation_tab_in_position","success":False,"diff":diff})
        time.sleep(1)
    print(f"Failed to find annotation tab, difference of diff {diff}")
    sc.save("failed annotation.jpg")
    return False
    

def chatgpt_tab_in_position():
    region=835,7,50,20
    saved=Image.open("trainings/chatgpt_tab.jpg")
    sc=None
    diff=0
    for i in range(50):
        sc=pilot.screenshot(region=region)
        diff=screenshots_different(saved,sc)
        if diff<100:
            create_log({"function":"chatgpt_tab_in_position","success":True,"diff":diff})
            return True
        create_log({"function":"chatgpt_tab_in_position","success":False,"diff":diff})
        time.sleep(1)
    print(f"Failed to find gpt tab, difference of diff {diff}")
    sc.save("failed_gpt.jpg")
    return True

def annotation_image_loaded():
    region=87,227,244,120
    saved=Image.open("trainings/failed_img_loading.jpg")
    sc=pilot.screenshot(region=region)
    diff=screenshots_different(saved,sc)
    print("Error diff:")
    print(diff)
    if diff<35:
        return False
        print("Image not loaded")
    # check if image is not loaded
    region=34,214,337,120
    saved=Image.open("trainings/pending_img_loading.jpg")
    sc=pilot.screenshot(region=region)
    diff=screenshots_color_different(saved,sc)
    if diff<=8:
        print("Image is not loaded")
        return False
    
    # check if different loading screen
    region=120,231,160,100
    sc=pilot.screenshot(region=region)
    saved=Image.open("trainings/still_img_loading.jpg")
    diff=screenshots_color_different(saved,sc)
    if diff<=8:
        print("Image not loaded yet")
        return False

    # check if annotation page is loaded
    region=5,136,160,60
    sc2=pilot.screenshot(region=region)
    saved2=Image.open("trainings/review_page.jpg")
    diff=screenshot_change_percent(saved2,sc2)
    print("Annotation page not opened")
    print(diff)
    if diff<=93.70:        
        print("Annotation page not opened")
        print(diff)
        time.sleep(0.8)
        pilot.moveTo(menu_btn,duration=0.5)
        pilot.click()
        time.sleep(0.5)
        pilot.moveTo(annotation_menu_btn,duration=0.5)
        pilot.click()
        return False
    return True

def login_if_loggedout():
    region=11,7,100,20
    sc=pilot.screenshot(region=region)
    saved=Image.open("trainings/login_tab.jpg")
    diff=screenshots_color_different(saved,sc)
    if diff<37:
        pilot.moveTo(annotation_reload, duration=0.3)
        pilot.click()
        time.sleep(3)
        import random
        from accounts import accounts
        acc=random.choice(accounts)
        email=acc["email"]
        password=acc["password"]
        pilot.moveTo(277,402)
        pilot.click()
        time.sleep(0.5)
        pilot.typewrite(email, interval=0.05)

        pilot.moveTo(276,462)
        pilot.click()
        time.sleep(0.5)
        pilot.typewrite(password, interval=0.05)

        pilot.moveTo(395,557)
        pilot.click()
        time.sleep(3)

        region=5,136,160,60
        annotation_url="http://68.178.172.222/bsi/admin/annotations.php"
        pilot.moveTo(280,62,duration=0.5)
        pilot.click()
        time.sleep(0.5)
        pilot.typewrite(annotation_url, interval=0.05)
        pilot.press("enter")
        time.sleep(4)
    return True
