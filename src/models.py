
from enum import Enum, IntEnum


#====== Enumerators =========

#====== class models ==========

class SyncTrackEvent:
  def __init__(self, pos : int, name : str, value : any = None):
    self.position = pos
    self.name = name
    self.value = value

class event:
  def __init__(self, typeE : int, name : str, pos : int, leng : int = 0):
    self.type = typeE #0 : none, 1 : starpower, 2: other
    self.name = name #star, Solo, Soloend...
    self.position = pos
    self.length = leng #length for starpower

class note:
  def __init__(self, typeE : int, lane : int, length : int, pos : int):
    self.type = typeE
    self.lane = lane
    self.length = length
    self.position = pos

class difficultyTrack:
  def __init__(self, difficulty : str, notes: list[note], lEvents : list[event]):
    self.difficulty = difficulty
    self.notes = notes
    self.localEvents = lEvents
  def __str__(self) -> str:
      return self.difficulty
  def __eq__(self, __value: object) -> bool:
    if type(__value) == str:
      if self.difficulty == __value:
        return True
      else:
        return False

class track:
  def __init__(self, name : str, difficultyTracks: list[difficultyTrack]):
    self.name = name
    self.difficultyTracks = difficultyTracks
  def __str__(self) -> str:
    return self.name
  def __eq__(self, __value: object) -> bool:
    if type(__value) == str:
      if self.name == __value:
        return True
      else:
        return False

class Song:
  def __init__(self : str, name : str, artist : str, year : int, offset : float, difficulty : int, previewstart: float, previewend: float, musicstream: str,guitarstream: str,bassstream: str,player2: str, genre: str, mediatype: str, tracks: list[track], gevents : list[event], resolution : int = 192):
    self.name = name
    self.artist = artist
    self.year = year
    self.offset = offset
    self.resolution = resolution
    self.player2 = player2
    self.difficultyValue = difficulty
    self.previewstart = previewstart
    self.previewend = previewend
    self.genre = genre
    self.mediatype = mediatype
    self.musicstream = musicstream
    self.guitarstream = guitarstream
    self.bassstream = bassstream
    self.tracks = tracks
    self.globalEvents = gevents
