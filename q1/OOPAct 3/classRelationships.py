class Song:
    """A single track with some basic info."""

    def __init__(self, song_id, title, artist, duration):
        self.songId = song_id
        self.title = title
        self.artist = artist
        self.duration = duration  # minutes

    def get_summary(self):
        return f"{self.title} by {self.artist} ({self.duration} min)"


class Playlist:
    """A playlist that contains many Song objects (1 Playlist : 0..* Songs)."""

    def __init__(self, name, is_public=False):
        self.name = name
        self.isPublic = is_public
        self.__songs = []  # stores actual Song objects, not just names

    def addSong(self, song):
        """Adds a Song object to this playlist -- this builds the relationship."""
        self.__songs.append(song)

    def togglePrivacy(self):
        self.isPublic = not self.isPublic

    def getSongCount(self):
        return len(self.__songs)

    def getTotalDuration(self):
        return sum(song.duration for song in self.__songs)

    def get_songs(self):
        """Lets other code access the related Song objects."""
        return self.__songs

    def display_info(self):
        visibility = "Public" if self.isPublic else "Private"
        return (f"{self.name} | {visibility} | "
                f"Songs: {self.getSongCount()} | Duration: {self.getTotalDuration()} min")


if __name__ == "__main__":
    playlist1 = Playlist("Morning Coffee Mix", is_public=True)

    song1 = Song("song_001", "Sunrise Drive", "The Amber Hour", 3.5)
    song2 = Song("song_002", "Slow Roast", "Nadia Cole", 4.2)
    song3 = Song("song_003", "Steam & Sugar", "The Amber Hour", 2.9)

    print("--- BEFORE RELATIONSHIP ---")
    print(playlist1.display_info())

    print("\n--- BUILDING RELATIONSHIP ---")
    for song in (song1, song2, song3):
        playlist1.addSong(song)
        print("Added:", song.get_summary())

    print("\n--- AFTER RELATIONSHIP ---")
    print(playlist1.display_info())
    print("Related object(s):")
    for song in playlist1.get_songs():
        print(" -", song.get_summary())
