from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
import os, pathlib, time

class preferAlbumArtist(BeetsPlugin):
    def __init__(self):
        super().__init__()
        self.register_listener('alternatives.item_updated', self.on_update)

    def on_update(self, collection, item, action, path):
        # Debug
        #self._log.error('update captured.\ncollection: {}\nitem: {}\naction: {}\ndestination: {}'.format(collection, item, action,item.destination))
        item.artist = item.albumartist 
        item.arist_sort = item.albumartist_sort
        item.write(path=path)
    
    def loaded(self):
        self._log.info('Plugin loaded!')
