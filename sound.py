import arcade
from random import choice
from os import listdir

class Player(arcade.Sprite):
    def __init__(self):
        # I'm pretty sure I need something here but IDK... I'll read the docs later
        
        # COMPOSITION!
        self.sounds = SoundManager()

    def attack(self):
        # Do fancy lil attack thing. And then somewhere go:
        self.sounds.play(self, "attack")

class SoundManager:
    """
    init function.
    Args:
        base_path (str): The base path for the audio
    """
    def __init__(self):
        self.base = "./Assets/Audio/"
        self.sounds = {}

    def get_valid_sounds(self, cls_name:str, sound_name:str):
        res = [sound for sound in listdir(self.base + cls_name) if sound_name.lower() in sound]
        self.sounds[cls_name].setdefault(sound_name, res)
        return res

    def load(self, cls, sound_name:str):
        cls_name = cls.__class__.__name__
        self.sounds.setdefault(cls_name, {})
        return arcade.load_sound(self.base + cls.__class__.__name__ + "/" + choice(self.sounds.get(sound_name, self.get_valid_sounds(cls_name, sound_name))))
    
    def play(self, cls, sound_name:str):
        arcade.play_sound(self.load(cls, sound_name))

if __name__ == "__main__":
    from time import sleep
    p = Player()

    for i in range(5):
        p.attack()
        sleep(0.3)