# usage

feel free to use this however you want with no need to reference me.

this was purely a project I made for fun in my free time


# Documentation

this library reads .chart files from a function .parse()

## Functions

### pygh.parse(*filename*) -> *Song*:
| Parameters | Description                              |
| :--------  | :---------                            |
| `filename` | the file path used to read, MUST be a .chart    |
| Return     |                               |
| `Song`     | a song model that gets returned representing the song.chart |


## pygh.models

### models.Song
 - `name` is a `string` containing the name of the song
 - `artist` is a `string` containing artist name
 - `year` is a `int` containing the year the song was created
 - `offset` is a `float` containing the offset amount for the chart
 - `difficulty` is a `int` containing the integer difficulty for the chart
 - `previewstart` is a `float` for the start time of the menu preview audio
 - `previewend` is a `float` for the end time of the menu preview audio
 - `musicstream` is a `string` containing the filepath of the main audio for the song
 - streams
  - `guitarstream`
  - `bassstream`
 - `player 2` is a `string` containing the co op player for the song
 - `genre` is a `string` of the genre of the song
 - `mediatype` is a `string` of the mediatype of the song
 - `tracks[]` is a `list[track]` of the instruments in the song
 - `globalEvents[]` is a `list[SyncTrackEvent]` of all the global events in the song
 - `resolution` is a `int` of the amount of ticks in a quater note

### models.track
 - `name` is a `string` containing the value of the track (see https://github.com/TheNathannator/GuitarGame_ChartFormats/blob/main/doc/FileFormats/.chart/5-Fret%20Guitar.md for track types)
 - `difficultyTracks` is a `list[difficultyTrack]` of the different difficulty charts

### models.difficultyTrack
 - `difficulty` is a `string` of the name of the difficulty
  - `Easy`
  - `Medium`
  - `Hard`
  - `Expert`
 - `notes` is a `list[note]` of notes in that chart
 - `localEvents` is the `list[event]` of events in a chart such as starpower and solos

### models.note
 - `type` is a `int` of the type of the note
  - `0` is no effect
  - `5` is a hopo
  - `6` is a tap
 - `lane` is a `int` containing the lane its in
  - `0` lane 1 (green)
  - `1` lane 2 (red)
  - `2` lane 3 (yellow)
  - `3` lane 4 (blue)
  - `4` lane 5 (orange)
  - `7` open note (purple)
 - `length` is a `int` containing the length of the note in ticks, if 0 then its a single note (no sustain)
 - `position` is the song position of the note in ticks

### models.event
 - `type` is a `int` containing the type of local event
  - `0` is no event
  - `1` is a star power phrase
  - `2` is other local events
 - `name` is a `string` containing the name of the type of event
 - `position` is the `int` start of the event in ticks
 - `length` is a `int` of the lenth of the event in ticks (for star power)

### models.SyncTrackEvent
 - `position` is a `int` of the position in ticks
 - `name` is the type of event
  - `TimeSignature`
  - `TempoMarker`
  - `TempoAnchor`
  - `section`
  - `lyric`
  - `phrase_start`
  - `phrase_end`
 - `value` is a `any` of the metadata of the event
  - time signatures `(A, B)` for signature A/B
  - tempo marker `float` for BPM
  - tempo anchor `float`
  - lyric `string` for the words of the lyric
  - section `string` for the name of the section
  
