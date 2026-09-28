from beets.plugins import BeetsPlugin


class PreferAlbumArtist(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.register_listener('alternatives.item_updated', self.on_update)

    def on_update(self, collection, item, action, path):
        if not item.albumartist:
            return
        tmp = item.copy()  # never touch the library's own item
        tmp.artist = tmp.albumartist
        tmp.artist_sort = tmp.albumartist_sort
        tmp.write(path=path)
