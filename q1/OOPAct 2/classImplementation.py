class Playlist:
    """
    Represents a custom collection of songs within a music streaming
    application. Tracks details such as total playtime, track count,
    and visibility to other users.
    """

    def __init__(self, name, is_public=False):
        self.name = name            
        self.isPublic = is_public   

        self.__songs = {}           
        self.__songCount = 0
        self.__totalDuration = 0.0

    def addSong(self, songId, duration):
        """Adds a new song to the playlist using its unique identifier and duration (minutes)."""
        if songId in self.__songs:
            print(f"  [skip] '{songId}' is already in '{self.name}'.")
            return

        self.__songs[songId] = duration
        self.__songCount += 1
        self.__totalDuration += duration
        print(f"  [add] '{songId}' ({duration} min) -> '{self.name}'")

    def removeSong(self, songId):
        """Removes a specific song from the playlist based on its identifier."""
        if songId not in self.__songs:
            print(f"  [skip] '{songId}' was not found in '{self.name}'.")
            return

        duration = self.__songs.pop(songId)
        self.__songCount -= 1
        self.__totalDuration -= duration
        print(f"  [remove] '{songId}' <- '{self.name}'")

    def togglePrivacy(self):
        """Toggles the playlist visibility between public and private."""
        self.isPublic = not self.isPublic

    def getSongCount(self):
        """Safely returns the current number of songs in the playlist (reads a private attribute)."""
        return self.__songCount

    def getTotalDuration(self):
        """Safely returns the total playback time in minutes (reads a private attribute)."""
        return round(self.__totalDuration, 2)

    def display_info(self):
        """Returns a readable one-line summary of the playlist's current state."""
        visibility = "Public" if self.isPublic else "Private"
        return (f"{self.name} | Visibility: {visibility} | "
                f"Songs: {self.getSongCount()} | Duration: {self.getTotalDuration()} min")


if __name__ == "__main__":
    playlist1 = Playlist("relapse", is_public=True)
    playlist2 = Playlist("hamilton", is_public=False)

    playlist1.addSong("song_001", 3.5)
    playlist1.addSong("song_002", 4.2)
    playlist1.addSong("song_003", 2.9)

    playlist2.addSong("song_101", 5.0)
    playlist2.addSong("song_102", 6.1)

    print("--- BEFORE ---")
    print("Object 1:", playlist1.display_info())
    print("Object 2:", playlist2.display_info())

    print("\nPerforming action on Object 1: removeSong('song_002') + togglePrivacy() ...")
    playlist1.removeSong("song_002")
    playlist1.togglePrivacy()

    print("\n--- AFTER ---")
    print("Object 1:", playlist1.display_info())
    print("Object 2:", playlist2.display_info())
