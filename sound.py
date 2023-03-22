import arcade
from arcade import Sound
from random import choice
from os import listdir

class SoundManager:
    """A class representing a Sound Manager"""

    def __init__(self):
        """Initializes the data"""
        self.base = "./Assets/Audio/"
        self.sounds = {}

    def get_valid_sounds(self, subfolder:str, sound_name:str) -> list:
        """Returns a list of all valid sounds
        
        Gets a list of sounds matching a given sound name from a given subfolder name
        
        Args:
            subfolder (str): The subfolder of the `self.base` folder where the audio is located
            sound_name (str): The name of the sound to search for.
            
        Returns:
            A list containing all sounds in the given directory containing the word `sound_name`"""
        
        res = [sound for sound in listdir(self.base + subfolder) if sound_name.lower() in sound]
        self.sounds[subfolder].setdefault(sound_name, res)
        return res

    def load(self, name_or_class: str | object, sound_name:str) -> Sound:
        """Loads a sound of type `sound_name` into memory.
        
        Selects a sound from the subfolder `name_or_class` containing the word `sound_name` and returns the loaded file.
        
        Args:
            name_or_class (str | object): The name of the subfolder, or instance of a class, that shares a foldername
            sound_name (str): The name of the sound to select.
            
        Returns:
            A Sound object to be played with arcade.play_sound(`Sound`)"""
        folder_name = name_or_class if isinstance(name_or_class, str) else name_or_class.__class__.__name__
        self.sounds.setdefault(folder_name, {})
        return arcade.load_sound(self.base + folder_name + "/" + choice(self.sounds.get(sound_name, self.get_valid_sounds(folder_name, sound_name))))
    
    def play(self, name_or_class: str | object, sound_name:str) -> None:
        """Plays a given sound
        
        Plays a random sound with the name `sound_name` from the folder `name_or_class`
        
        Args:
            name_or_class (str | object): The name of the subfolder, or an instance of a class that shares the same name as a subfolder.
            sound_name (str): The name of the sound to play."""
        arcade.play_sound(self.load(name_or_class, sound_name))

