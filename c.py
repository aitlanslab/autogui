import pyautogui
pilot=pyautogui
size=pilot.size()
from cursor_positions import annotation_title_bar

position=pilot.position()

print(f"Position : {position}")
print(f"Screen Size : {size.height}x{size.width}")



"""
region=120,231,160,100
sc=pilot.screenshot(region=region)
sc.save("trainings/still_img_loading.jpg")

region=120,231,160,100
sc=pilot.screenshot(region=region)
sc.save("trainings/still_img_loading.jpg")
"""
"""
region=5,136,160,60
sc=pilot.screenshot(region=region)
sc.save("trainings/annotation_page.jpg")
"""
"""
region=1060,283,60,90
sc=pilot.screenshot(region=region)
sc.save("trainings/chatgpt_error.jpg")
"""
import time
time.sleep(3)


while True:
    position=pilot.position()
    print(f"Position : {position}")

