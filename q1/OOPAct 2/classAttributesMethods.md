# Class Attributes and Methods

## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)

## Design Revision
Changes from my previous design:
- `addSong` now takes a second parameter, `duration : double`, alongside `songId`, so that `totalDuration` can be updated accurately every time a song is added (the original signature only had `songId`).
- `songCount` and `totalDuration` are now **private**. In the original design they were plain public properties, but they are really values that should only ever change as a side effect of `addSong()`/`removeSong()`, not be set directly from outside the class.
- Added two small getter methods, `getSongCount()` and `getTotalDuration()`, so other code can still safely *read* those private values without being able to overwrite them.
- The class name, context (a music-streaming Playlist), and the three original methods (`addSong`, `removeSong`, `togglePrivacy`) all stayed the same.

## Visibility Decisions

| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| name | string | Public | Other parts of the app (search, display, sharing) need to read the playlist's title directly, and there's no risk in exposing it. |
| isPublic | boolean | Public | The UI and other features need to check a playlist's visibility directly (e.g. to decide whether to show it in a public feed); `togglePrivacy()` is still the intended way to *change* it. |
| songCount | int | Private | This must always equal the number of songs actually stored in the playlist. If outside code could set it directly, it could easily go out of sync with the real contents. |
| totalDuration | double | Private | Same reasoning as songCount — it's a calculated value that depends on which songs are actually in the playlist, so it should only change through `addSong()`/`removeSong()`. |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)

## Test Run
![Test Run](images/classTestRun.png)

## Object Diagram
![Object Diagram](images/objectDiagram.png)

## Analysis

### Why did you make your chosen attribute private?
I made `songCount` and `totalDuration` private because both values are supposed to be a direct reflection of the songs that are actually stored in the playlist, not numbers anyone can set randomly. If they were public, another part of the program could accidentally set `playlist.songCount = 50` without ever adding 50 songs, or set `totalDuration` to a number that no longer matches the real songs in the list. That would break the whole point of the class, since anything that trusts these numbers — like a screen showing "12 songs, 45 minutes" — could end up displaying completely wrong information. Keeping them private and only changing them inside `addSong()` and `removeSong()` guarantees they always stay in sync with the actual song data.

### Which method changes the state of your object?
`addSong()` changes an object's state by adding the new `songId`/duration pair into the internal song storage, then increasing `songCount` by one and adding the song's duration to `totalDuration`. `removeSong()` does the reverse — it deletes the song entry and decreases both `songCount` and `totalDuration`. `togglePrivacy()` also changes state, flipping `isPublic` between `True` and `False`. In my test run, calling `playlist1.removeSong("song_002")` dropped Object 1's song count from 3 to 2 and lowered its duration from 10.6 to 6.4 minutes, and `togglePrivacy()` switched its visibility from Public to Private.

### How did your two objects demonstrate that instances are independent?
`playlist1` ("relapse") and `playlist2` ("hamilton") were both created from the same `Playlist` class but started with different songs, song counts, and durations. After I called `removeSong()` and `togglePrivacy()` on `playlist1` only, the BEFORE/AFTER output showed playlist1's song count drop from 3 to 2, its duration drop from 10.6 to 6.4 minutes, and its visibility flip to Private — while playlist2 still showed the exact same song count (2), duration (11.1), and visibility (Private) as before. That proves each object keeps its own separate copy of the attributes in memory, so changing one Playlist object has no effect on any other Playlist object.

### What is the difference between your class diagram and your object diagram?
My class diagram shows the `Playlist` blueprint in general terms — attribute names, their data types, and method signatures — but no actual values, because a class describes what *every* playlist could look like. My object diagram shows two specific playlists, `playlist1` and `playlist2`, with their real final values after Step 7 (e.g. `playlist1`'s `songCount = 2` and `totalDuration = 6.4`, versus `playlist2`'s `songCount = 2` and `totalDuration = 11.1`). In short, the class diagram describes the template, and the object diagram describes real instances created from that template at one specific moment in the program.
