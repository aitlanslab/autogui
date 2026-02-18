from sc import pilot
import time
import json
import pyperclip
from cursor_positions import chatgpt_prompt_input, chatpgt_close, chatgpt_reload, annotation_reload
from utils.screens import screenshots_different
def submit_prompt():
    time.sleep(2)
    pilot.click()
    pilot.moveTo(chatgpt_prompt_input,duration=0.05)
    pilot.click()
    prompt="""You are a taxonomist who extract the informations in json format analysing the herbarium sheet. The attached herbarium sheet contains collection data and notes. Analyse the attached sheet and replace the json values:{"family":"Fabaceae","genus":"Crotalaria","species":"juncea","current_name":"Crotalaria juncea","infraspecific_rank":"","infraspecific_taxon":"","author_infra":"","collector_name":"J.D. Hooker","collection_date":"1892-07-14","country_name":"India","state":"Bihar","district":"Jalpaiguri","city":"","village":"","locality":"Tea garden margins","altitude":"150 m","latitude":"N 24° 53' 15.20\"","longitude":"E 91° 52' 10.50\""}. Follow the same format of value as in the sample json for latitude and longitude. Only fill the values those are available in the attached herbarium sheet, else leave blank, also raise flag if the confidence of predicted value is low. Your response should only contain the copiable json in code format without any instruction or description text."""
    pyperclip.copy(prompt)
    #pilot.write(prompt, interval=0.01)
    pilot.hotkey("ctrl", "v")

    time.sleep(3)
    pilot.press("enter")
    time.sleep(2)
    pilot.press("enter")
    time.sleep(0.5)
    pilot.press("enter")
    time.sleep(0.5)
    pilot.press("enter")
    return is_gpt_completed()



from PIL import ImageChops
import numpy as np

def screenshot_change_percent(img1, img2):
    """
    Returns percentage of pixels that changed between two images
    """
    # Ensure same mode & size
    if img1.size != img2.size:
        raise ValueError("Images must be same size")

    diff = ImageChops.difference(img1, img2)

    diff_np = np.array(diff)

    # If RGB, reduce to grayscale-like magnitude
    if diff_np.ndim == 3:
        diff_np = diff_np.max(axis=2)

    changed_pixels = np.count_nonzero(diff_np)
    total_pixels = diff_np.size

    percent_changed = (changed_pixels / total_pixels) * 100
    return percent_changed


def refresh_gpt():
    pilot.moveTo(chatpgt_close, duration=0.1)
    pilot.click()
    time.sleep(1)
    pilot.click()
    return True


def is_gpt_completed():
    region = (951, 84, 200, 40)
    sc1=pilot.screenshot(region=region)
    max_waiting=1500
    # wait for 60s to detect any changes
    for i in range(max_waiting):
        sc2=pilot.screenshot(region=region)
        change=screenshot_change_percent(sc1, sc2)
        if change>=100:
            print("GPT response detected")
            refresh_gpt()
            time.sleep(0.5)
            time.sleep(1)  # give clipboard time
            copied_text = pyperclip.paste()
            data={}
            try:
                data = json.loads(copied_text)
                print("Parsed new response:", data)
                
            except json.JSONDecodeError:
                print("Clipboard does not contain valid JSON")
                return False
            refresh_gpt()
            return data
        if i%100==0:
            print(f"Waiting for GPT response... {max_waiting-i} ms left")
            pilot.scroll(-200)
        time.sleep(0.01)
    print("Waiting time up")
    return False


def tabs_reload():
    pilot.moveTo(chatgpt_reload, duration=0.3)
    pilot.click()
    time.sleep(1)
    pilot.moveTo(annotation_reload, duration=0.3)
    pilot.click()
    time.sleep(1)
    return True



"""
{
  "family": "Fabaceae",
  "genus": "Crotalaria",
  "species": "juncea",
  "scientific_name": "Crotalaria juncea L.",
  "current_name": "Crotalaria juncea",
  "synonyms": "",
  "author_name": "L.",
  "infraspecific_rank": "",
  "infraspecific_taxon": "",
  "author_infra": "",
  "collector_name": "J.D. Hooker",
  "collection_number": "",
  "collection_date": "1892-07-14",
  "acc_number": "",
  "country_name": "Japan",
  "state_name": "West Bengal",
  "district": "Sylhet",
  "city": "",
  "village": "",
  "locality": "Tea garden margins",
  "altitude": "150 m",
  "latitude": "N 24° 53' 15.20\"",
  "longitude": "E 91° 52' 10.50\"",
  "notes": "Common near cultivated areas",
  "flag_family": 0,
  "flag_genus": 0,
  "flag_species": 1,
  "flag_latitude": 0,
  "flag_longitude": 1}


{
  "family": "Fabaceae",
  "genus": "Crotalaria",
  "species": "juncea",
  "scientific_name": "Crotalaria juncea L.",
  "current_name": "Crotalaria juncea",
  "synonyms": "",
  "author_name": "L.",
  "infraspecific_rank": "",
  "infraspecific_taxon": "",
  "author_infra": "",
  "collector_name": "J.D. Hooker",
  "collection_number": "",
  "collection_date": "1892-07-14",
  "acc_number": "",
  "country_id": "18",
  "state_id": "377",
  "district": "Sylhet",
  "city": "",
  "village": "",
  "locality": "Tea garden margins",
  "altitude": "150 m",
  "latitude": "N 24° 53' 15.20\"",
  "longitude": "E 91° 52' 10.50\"",
  "notes": "Common near cultivated areas",
  "flag_family": 0,
  "flag_genus": 0,
  "flag_species": 1,
  "flag_latitude": 0,
  "flag_longitude": 1
}
"""