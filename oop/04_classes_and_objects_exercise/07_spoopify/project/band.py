from project.album import Album

class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums: list[Album] = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        current_album = next((a for a in self.albums if a.name == album_name), None)
        if not current_album:
            return f"Album {album_name} is not found."
        if current_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(current_album)
        return f"Album {album_name} has been removed."

    def details(self) -> str:
        albums_details = "\n".join([a.details() for a in self.albums])
        return (f"Band {self.name}\n"
                f"{albums_details}")

