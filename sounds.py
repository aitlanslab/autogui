import pygame
import time
import random
import sys

# ---------- AUDIO MANAGER ----------
class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        self.bgm_loaded = False

    # ---- Background Music ----
    def start_bgm(self, path: str):
        if not self.bgm_loaded:
            pygame.mixer.music.load(path)
            self.bgm_loaded = True
        pygame.mixer.music.play(-1)  # loop forever

    def stop_bgm(self):
        pygame.mixer.music.stop()
        self.bgm_loaded=False

    def pause_bgm(self):
        pygame.mixer.music.pause()


    def resume_bgm(self):
        pygame.mixer.music.unpause()

    # ---- One-shot Sounds ----
    def play_once(self, path: str, volume: float = 0.5):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(volume)
        sound.play()

    # ---- Shutdown ----
    def shutdown(self):
        pygame.mixer.music.stop()
        pygame.quit()


