
import models

diffs = [ #difficulties
  "Expert",
  "Hard",
  "Medium",
  "Easy"
]
tracknames = [
  "Single", #lead guitar
  "DoubleGuitar", #Co-op Guitar
  "DoubleBass", #bass guitar
  "DoubleRhythm", #rhythm guitar
  "Keyboard" #5-lane keys
]

#create song class from .chart file
def parse(filename):
  if filename.endswith(".chart") != True:
    raise Exception("File must be a .chart file")
  lines = open(filename, "r").read().split("\n")

  song = models.Song("Name", "artist", 0, 0, 0, 0, 0, "", "", "", "", "", "", [], [])
  spot = 0
  spot2 = ""
  for line in lines:
    if line.find("}") != -1:
      spot = 0
      continue
    if line == "[Song]":
      spot = 1
      continue
    elif line=="[SyncTrack]":
      spot = 2
      continue
    elif line=="[Events]":
      spot = 3
      continue
    elif line.find("{") != -1:
      continue
    for name in tracknames:
      for diff in diffs:
        if line == "[" + diff + name + "]":
          spot = name
          spot2 = diff
          if spot not in song.tracks:
            song.tracks.append(models.track(spot, []))
            if spot2 not in song.tracks[song.tracks.index(spot)].difficultyTracks:
              song.tracks[song.tracks.index(spot)].difficultyTracks.append(models.difficultyTrack(spot2, [], []))
          break
        break
      continue
    
    if line == "[" + spot2 + str(spot) + "]":
      continue
    elif spot == 1:
      datapoint = line.replace(" ", "").replace("\t", "").replace("\"" , "").replace(",", "").split("=")
      if datapoint[0] == "Name":
        song.name = datapoint[1]
      elif datapoint[0] == "Artist":
        song.artist = datapoint[1]
      elif datapoint[0] == "Year":
        song.year = int(datapoint[1])
      elif datapoint[0] == "Offset":
        song.offset = int(datapoint[1])
      elif datapoint[0] == "Resolution":
        song.resolution = int(datapoint[1])
      elif datapoint[0] == "Player2":
        song.player2 = datapoint[1]
      elif datapoint[0] == "Difficulty":
        song.difficulty = int(datapoint[1])
      elif datapoint[0] == "PreviewStart":
        song.previewstart = float(datapoint[1])
      elif datapoint[0] == "PreviewEnd":
        song.previewend = float(datapoint[1])
      elif datapoint[0] == "Genre":
        song.genre = datapoint[1]
      elif datapoint[0] == "MediaType":
        song.mediatype = datapoint[1]
      elif datapoint[0] == "MusicStream":
        song.musicstream = datapoint[1]
      elif datapoint[0] == "GuitarStream":
        song.guitarstream = datapoint[1]
      elif datapoint[0] == "BassStream":
        song.bassstream = datapoint[1]
    elif spot == 2: #synctrack
      DATA = line.split(" ")
      tick = DATA[2]
      if DATA[4] == "TS": #time signature
        denom = 4
        if len(DATA) >= 7:
          denom = 2**int(DATA[6])
        signature = (DATA[5], denom)
        event = models.SyncTrackEvent(tick, "TimeSignature", signature)
        song.globalEvents.append(event)
      elif DATA[4] == "B": #tempo
        BPM = float(DATA[5]) / 1000
        event = models.SyncTrackEvent(tick, "TempoMarker", BPM)
        song.globalEvents.append(event)
      elif DATA[4] == "A": #tempo anchor
        Time = float(DATA[5]) / 1000000
        event = models.SyncTrackEvent(tick, "TempoAnchor", Time)
        song.globalEvents.append(event)
    elif spot == 3: #Events
      
      DATA = line.split(" ")
      tick = DATA[2]
      if DATA[4] == "E":
        EventValue = DATA[5].replace('\"', "").split(" ")
        if EventValue[0] == "section":
          name = ""
          for i in range(6, len(DATA)):
            name += DATA[i] + " "
          name = name.replace('\"', "")
          Event = models.SyncTrackEvent(tick, EventValue[0], name)
          song.globalEvents.append(Event)
        elif EventValue[0] == "lyric":
          name = DATA[6].replace('\"', "")
          Event = models.SyncTrackEvent(tick, EventValue[0], name)
          song.globalEvents.append(Event)
        elif EventValue[0] == "phrase_start":
          Event = models.SyncTrackEvent(tick, EventValue[0])
          song.globalEvents.append(Event)
        elif EventValue[0] == "phrase_end":
          Event = models.SyncTrackEvent(tick, EventValue[0])
          song.globalEvents.append(Event)
    elif spot in tracknames: #track data
      if spot2 in diffs:
        
        DATA = line.split(" ")
        tick = DATA[2]
        if DATA[4] == "E": #Local Event
          name = DATA[5]
          evnt = models.event(2, name, tick) # sets it as an "Other" event
          song.tracks[song.tracks.index(spot)].difficultyTracks[song.tracks[song.tracks.index(spot)].difficultyTracks.index(spot2)].localEvents.append(evnt)
        elif DATA[4] == "N": #Note
          if int(DATA[5]) in [5, 6]:
            if lastNote.position == tick:
              lastNote.type = int(DATA[5])
          elif int(DATA[5]) in [0, 1, 2, 3, 4, 7]:
            lane = int(DATA[5])
            length = int(DATA[6])
            noteType = 0
            note = models.note(noteType, lane, length, tick)
            song.tracks[song.tracks.index(spot)].difficultyTracks[song.tracks[song.tracks.index(spot)].difficultyTracks.index(spot2)].notes.append(note)
            lastNote = note
        elif DATA[4] == "S": #Special
          if lastNote.position == tick:
            if DATA[5] == 2:
              evnt = models.event(1, "starpower", tick, length)
              song.tracks[song.tracks.index(spot)].difficultyTracks[song.tracks[song.tracks.index(spot)].difficultyTracks.index(spot2)].localEvents.append(evnt)
  return song
