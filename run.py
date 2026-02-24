from annotation_tab import (
    switch_to_annotation_tab,
    download_image,
    take_ss,
    drag_download,
    close_download_popup,
    submit_data,
    dismiss_filler,
    submit_form
)
from checks import load_annotation,login_if_loggedout, load_chatgpt, annotation_image_loaded, chatgpt_tab_in_position, annotation_tab_in_position, gpt_attachment_in_position 
from sounds import AudioManager
from gpt_tab import submit_prompt, is_gpt_completed, tabs_reload
import asyncio
import time
import random
from sc import pilot
from relogging import login_chatgpt, logout_chatgpt

audio = AudioManager()


failed_attempts=0
max_failed_attempts=5
audio.start_bgm("aud/wait.mp3")
time.sleep(5)
switch_to_annotation_tab()
tabs_reload()
# Login if logged out
auth=login_if_loggedout()
if auth==False:
    audio.play_once("aud/error_short.mp3")
    time.sleep(100)

annotaion_in_correct_position=annotation_tab_in_position()
print("Annotation Loaded")
chatgpt_tab_in_position_in_correct_position=chatgpt_tab_in_position()
print("ChatGPT Loaded")
audio.stop_bgm()



checks=False
if annotaion_in_correct_position and chatgpt_tab_in_position:
  checks=True
  print("All tabs in correct position")

c=0
curr_acc=1
for i in range(500):
  audio.start_bgm("aud/wait.mp3")
  annotation_loaded=load_annotation()
  if annotation_loaded==False:
    audio.play_once("aud/error_short.mp3")
    time.sleep(1)
    tabs_reload()
    continue

  if chatgpt_tab_in_position()==False:
    audio.play_once("aud/error.mp3")
    time.sleep(60)
    break

  print("Annotation Loaded")
  print(f"Checks : {checks} Annotation Loaded : {annotation_loaded}")
  if checks and annotation_loaded:
    audio.stop_bgm()
    
    audio.play_once("aud/wonder.mp3")
    time.sleep(0.8)
    options = ["1", "2", "3", "4", "5"]
    rando = random.choice(options)
    audio.start_bgm("aud/process.mp3")
    time.sleep(0.8)    
    if c==0:
      switch_to_annotation_tab()
    annotation_image_stat=annotation_image_loaded()
    time.sleep(0.8)  
    if annotation_image_stat==False:
      print("Failed to load annotation")
      audio.play_once("aud/error_short.mp3")
      tabs_reload()
      time.sleep(3)
      continue

    chatgpt_loaded=load_chatgpt()
    if chatgpt_loaded==False:
      audio.play_once("aud/error.mp3")
      time.sleep(30)
      continue

    download_image()
    drag_download()
    gpt_stat=gpt_attachment_in_position()
    while(gpt_stat==False):
        print("GPT Attachment not found")
        audio.play_once("aud/error_short.mp3")
        time.sleep(2)
        logout_chatgpt()
        login_chatgpt(curr_acc)
        curr_acc=curr_acc+1
        if curr_acc>3:
            curr_acc=1
        # Redo 
        close_download_popup()
        switch_to_annotation_tab()
        download_image()
        drag_download()
        gpt_stat=gpt_attachment_in_position()
        #audio.play_once("aud/error.mp3")
        #time.sleep(30000)
        #break
        # Exit the loop
    result = submit_prompt()  
    if result==False:
        if failed_attempts>=max_failed_attempts:
            print("Max failed attempts reached. Switching account.")
            logout_chatgpt()
            login_chatgpt(curr_acc)
            curr_acc=curr_acc+1
            if curr_acc>3:
                curr_acc=1
            # Redo 
            close_download_popup()
            switch_to_annotation_tab()
            download_image()
            drag_download()
            gpt_stat=gpt_attachment_in_position()
        else:
            audio.play_once(f"aud/error_short.mp3")
            time.sleep(5)
            tabs_reload()
            close_download_popup()
            failed_attempts=failed_attempts+1
            continue

    close_download_popup()
    res=submit_data()
    if res==False:
      #audio.play_once(f"aud/error.mp3")
      #time.sleep(60)
      audio.play_once(f"aud/error_short.mp3")
      time.sleep(5)
      tabs_reload()
      close_download_popup()
      continue
      # Exit the loop
      #break
    pilot.moveTo(dismiss_filler,duration=0.5)
    pilot.click()
    #pilot.press("enter")
    submit_form()
    audio.stop_bgm()
    #audio.play_once(f"aud/success/{rando}.mp3")
    time.sleep(1)
    c=c+1
    print(c)



