from dataclasses import dataclass
import math
from typing import Dict, List


# 7.3 - Jukebox: Design a musical jukebox using object oriented principles.

@dataclass
class Song:
    artist: str
    title: str
    

class Jukebox:
    songs: Dict[int, Song]
    playlist: List[Song]
    playing: bool
    credits: int
    credit_cost: int
    
    def __init__(self, songs: Dict[int, Song]) -> None:
        self.songs = songs
        self.playlist = []
        self.playing = False
        self.credit = 0
        self.credit_cost = 200
        
    def purchase_credit(self, money: int) -> None:
        self.credits += math.floor(money / self.credit_cost)
        
    def select_song(self, song_number: int) -> None:
        if self.credits == 0:
            print('Please purchase credits')
            
        song = self.songs.get(song_number)
        if song:
            self.playlist.append(song)
            self.credits -= 1
            print(f'Song {song.title} added to playlist')
            if not self.playing:
                self.play()
        else:
            print(f'Song number {song_number} not found')
            
    def play(self) -> None:
        while self.playlist:
            self.playing = True
            song = self.playlist.pop(0)
            print(f'Playing {song.title}')
            
        self.playing = False
        