import pyautogui
pilot=pyautogui
size=pilot.size()
from cursor_positions import annotation_title_bar

position=pilot.position()

print(f"Position : {position}")
print(f"Screen Size : {size.height}x{size.width}")




#pilot.moveTo(annotation_title_bar, duration=0.5)
#pilot.click()
"""
region=1065,295,25,25
sc=pilot.screenshot(region=region)
sc.save("trainings/google_login_waiting.jpg")
"""

"""
region=899,225,370,100
sc=pilot.screenshot(region=region)
sc.save("trainings/chatgpt_loging_new.jpg")
"""
"""
region=1087,86,70,40
sc=pilot.screenshot(region=region)
sc.save("trainings/chatgpt_loging_button.jpg")
"""
"""
region=835,658,200,50
sc=pilot.screenshot(region=region)
sc.save("trainings/claim_offer.jpg")


while True:
    position=pilot.position()
    print(f"Position : {position}")
"""






