from sc import pilot
from cursor_positions import (
    chatgpt_menubar,
    chatgpt_account,
    chatgpt_logout,
    chatgpt_logout_confirm,
    chatgpt_login_button,
    chatgpt_google_login,
    chatgpt_google_acc1,
    chatgpt_google_acc2,
    chatgpt_google_acc3,
    chatgpt_google_login_pending,
    chatgpt_temp_chat
)
from PIL import Image
from utils.screens import screenshots_different, screenshots_color_different, screenshot_change_percent
import time

def logout_chatgpt():
    time.sleep(1)
    region=1087,86,70,40
    sc=pilot.screenshot(region=region)
    saved=Image.open("trainings/chatgpt_loging_button.jpg")
    img_diff=screenshot_change_percent(saved,sc)
    if img_diff>85:
        print(f"Logout Button Diff: {img_diff}")
        time.sleep(5)

        pilot.moveTo(chatgpt_menubar, duration=0.5)
        pilot.click()
        time.sleep(0.5)
        chatgpt_account_pos, chatgpt_logout_pos = get_logout_position()
        print(f"Account Position: {chatgpt_account_pos}, Logout Position: {chatgpt_logout_pos}")
        pilot.moveTo(chatgpt_account_pos, duration=0.5)
        pilot.click()
        time.sleep(0.5)
        pilot.moveTo(chatgpt_logout_pos, duration=0.5)
        pilot.click()
        time.sleep(0.5)
        pilot.moveTo(chatgpt_logout_confirm, duration=0.5)
        pilot.click()
        time.sleep(0.5)
        duration=30
        for i in range(duration):
            logout_btn=Image.open("trainings/chatgpt_loging_button.jpg")
            area=1087,86,70,40
            sc=pilot.screenshot(region=area)
            img_diff=screenshots_different(logout_btn,sc)
            if img_diff<=85:
                print("Logged out successfully")
                return True
            time.sleep(1)
        return False
    return True


def login_chatgpt(target_account=1):
    time.sleep(1)
    pilot.moveTo(chatgpt_login_button, duration=0.5)
    pilot.click()
    time.sleep(0.5)
    new_login=Image.open("trainings/chatgpt_loging_new.jpg")
    old_login=Image.open("trainings/chatgpt_loging_back.jpg")
    area=899,225,370,100
    sc=pilot.screenshot(region=area)
    new_login_diff=screenshots_different(new_login,sc)
    old_login_diff=screenshots_different(old_login,sc)
    #if new_login_diff<old_login_diff:        
    if True:
        print("New Logging")
        pilot.moveTo(chatgpt_google_login, duration=0.5)
        pilot.click()
        time.sleep(0.5)
        pending_area=1065,295,25,25
        pending_image=Image.open("trainings/google_login_waiting.jpg")
        for i in range(30):
            sc=pilot.screenshot(region=pending_area)
            pending_diff=screenshots_different(pending_image,sc)
            if pending_diff>=100:
                if target_account==1:
                    pilot.moveTo(chatgpt_google_acc1, duration=0.5)
                    pilot.click()
                elif target_account==2:
                    pilot.moveTo(chatgpt_google_acc2, duration=0.5)
                    pilot.click()
                elif target_account==3:
                    pilot.moveTo(chatgpt_google_acc3, duration=0.5)
                    pilot.click()
                
                # check the loading of chatgpt login
                random_source_area=1065,295,25,25
                source_area_image=pilot.screenshot(region=random_source_area)
                for j in range(30):
                    new_source_image=pilot.screenshot(region=random_source_area)
                    source_diff=screenshots_different(source_area_image,new_source_image)
                    if source_diff>=100:
                        print("Logged in successfully")
                        time.sleep(0.5)
                        pilot.moveTo(chatgpt_temp_chat, duration=0.5)
                        pilot.click()
                        time.sleep(0.5)
                        return True
                    time.sleep(1)
                time.sleep(1)
                break
            time.sleep(1)
        print("Error Occured")
        return False
    else:
        print("Old Logging")
        return False


def get_logout_position():
    region=835,658,200,50
    current_pos=pilot.screenshot(region=region)
    target_pos=Image.open("trainings/claim_offer.jpg")
    diff=screenshots_different(current_pos,target_pos)
    print(diff)
    if diff>=70:
        return chatgpt_account,chatgpt_logout
    else:
        acc=933,630
        logout=926,571
        return acc,logout





