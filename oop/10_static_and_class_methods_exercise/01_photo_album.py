import math


class PhotoAlbum:

    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return (f"{label} photo added successfully on page "
                        f"{i + 1} slot {len(page)}")
        return "No more free slots"

    def display(self):
        separator = "-" * 11
        if self.photos:
            text = separator + "\n"
        else:
            return ""
        for page in self.photos:
            text += " ".join(["[]" for _ in page]) + "\n"
            text += separator + "\n"

        return text.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

