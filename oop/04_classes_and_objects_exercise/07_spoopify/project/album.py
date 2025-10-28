from project.song import Song

class Album:

    def __init__(self, name: str, *args: Song):
        self.name = name
        self.published = False
        self.songs = list(args)

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        current_song = next((song for song in self.songs
                             if song.name == song_name), None)
        if not current_song:
            return "Song is not in the album."

        self.songs.remove(current_song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self) -> str:
        songs_details = "\n".join([f"== {song.get_info()}" for song in self.songs])
        return (f"Album {self.name}\n"
                f"{songs_details}")


