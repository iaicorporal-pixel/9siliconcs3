# SG4 - Understanding Classes and Objects
## Class Name
Playlist

## Class Description
This class represents a custom collection of songs within a music streaming application. It tracks details such as total playtime, track count, and visibility to other users.

## Properties
| Property | Data Type | Description |
|---|---|---|
| name | string | The title of the playlist created by the user. |
| songCount | int | The total number of songs currently in the playlist. |
| isPublic | boolean | Indicates whether the playlist is visible to everyone or private. |
| totalDuration | double | The total playback time of all songs in minutes. |

## Methods
| Method | Description |
|---|---|
| addSong(songId: string) | Adds a new song to the playlist using its unique identifier. |
| removeSong(songId: string) | Removes a specific song from the playlist based on its identifier. |
| togglePrivacy() | Toggles the playlist visibility between public and private. |

## Class Diagram
![Class Diagram](images/classDiagram.png)

## Design Explanation
### Why did you choose this class?
I chose the Playlist class from the Music context because digital music streaming is a common daily activity. A playlist is a dynamic concept that translates well into an object-oriented system because it maintains state properties and provides interactive behaviors.

### Which property is the most important? Why?
The `name` property is the most important because users and systems identify and organize custom collections primarily by title. Without a name, users cannot easily search for or distinguish between different playlists.

### Which method is the most useful? Why?
The `addSong(songId: string)` method is the most useful because the core purpose of a playlist is to aggregate songs. Passing a `songId` parameter allows the playlist to dynamically grow and store new tracks.
