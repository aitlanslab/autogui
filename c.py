import pyautogui
pilot=pyautogui
size=pilot.size()
from cursor_positions import annotation_title_bar

position=pilot.position()

print(f"Position : {position}")
print(f"Screen Size : {size.height}x{size.width}")



"""
region=34,214,337,120
sc=pilot.screenshot(region=region)
sc.save("trainings/pending_img_loading.jpg")
"""
while True:
    position=pilot.position()
    print(f"Position : {position}")

