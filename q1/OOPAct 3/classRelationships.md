# Class Relationships: Association and Multiplicity

## Existing Class
Class: **Playlist** — a custom collection of songs (name, visibility, song count, total duration).

## New Related Class
Class: **Song** — a single track (songId, title, artist, duration). A playlist needs songs to actually be useful, which is why the two are connected.

## Association
Relationship: **Playlist contains Song**
Explanation: Playlist stores a list of real Song object references; `addSong()` is how that connection is made.

## Multiplicity
Multiplicity: **1 : 0..\***
Explanation: A playlist can start empty and grow to hold many songs, while each song here belongs to only one playlist.

## Analysis

### What is the association between your two classes?

My Playlist class has a HAS-A relationship with my Song class: a Playlist contains Song objects, where each Song represents one individual track with its own title, artist, and duration. Playlist doesn't store any song information directly — instead it keeps a list of Song objects and reads their data whenever it needs to, through getSongCount(), getTotalDuration(), and get_songs(). This means the relationship isn't just conceptual; it's a real connection in the code, where one object (Playlist) manages a collection of other objects (Song).

### What multiplicity did you choose and why?

I chose a 1 : 0..* multiplicity, because a Playlist can exist with zero songs right after it's created and then grow to hold as many songs as the user adds — there's no fixed upper limit in my design. On the Song side, each Song in my test run is only ever added to the one Playlist it was created for, so the relationship is one Playlist to many Songs rather than the other way around. This fits how playlists actually work in a real music app: you start with an empty list and build it up over time.

### How did you implement the relationship in Python?

I implemented the relationship with a private attribute, self.__songs, which is a Python list. The addSong(song) method is what builds the relationship — it simply appends the Song object that's passed in onto that list. Everything else, like getSongCount() and getTotalDuration(), reads from that same list with len() and sum() rather than keeping separate numbers that could get out of sync.

### Why did you store an object reference instead of copying its data?

I store the actual Song object inside self.__songs instead of copying its title or duration into new variables, because a reference keeps the Playlist connected to the song's full, current information. For example, get_songs() returns the real Song objects, so when the test script calls song.get_summary() on each one, it has access to the title, artist, and duration all at once. If I had only copied song.title as a plain string when adding it, the Playlist would have no way to also report the artist or duration later, and the two classes would effectively be disconnected.

### If your relationship uses many, why is a list appropriate?

My relationship is one-to-many — one Playlist can be linked to many Song objects — so a Python list is the natural fit, since it can hold zero, one, or many items and keeps them in the order they were added. In my implementation, self.__songs doesn't hold plain text or IDs; it holds actual Song objects, which is why looping over it with for song in self.__songs gives full access to each song's complete data. A list also made it simple to compute getSongCount() and getTotalDuration() just by looking at how many items are in the list and summing an attribute across all of them.