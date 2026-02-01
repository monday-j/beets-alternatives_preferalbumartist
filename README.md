# beets-alternatives_preferalbumartist
Shamelessly ripped from [this issue](https://github.com/geigerzaehler/beets-alternatives/issues/147#issuecomment-3283707097).

## What does this do?
Automatically overwrite the `Artist` metadata tag with the `Album Artist` when using [beets-alternatives](https://github.com/geigerzaehler/beets-alternatives).

## Why would I want to use this?
Many older (or poorly supported) Digital Audio Players tend to read the Artist tag in their internal database, ignoring the Album Artist tag entirely. This results in poorly-sorted music that would otherwise work fine in more modern music players.

This script aims to fix that issue by simply overwriting the `Artist` and `Sort Artist` tags with the `Album Artist` and `Sort Album Artist` tags respectively. It's a fairly destructive method to resolve this issue, but used responsibly in tandem with `beets-alternatives`, will result in a better experience on many older DAPs.

## How do I use this?

Make sure you have the `pluginpath:` defined in your beets `config.yaml` (I use `~/.config/beets/plugins`). Place `preferalbumartist.py` in the folder you've defined. Then, in the `config.yaml`, ensure `preferalbumartist` is listed in the `plugins:` key, like so:

```
plugins:
  - ...
  - alternatives
  - preferalbumartist
```

To ensure it's been loaded, type `beet version` into your console. You should see `preferalbumartist` in your list of plugins.

## Recommended plugins

I also use the [beets FtInTitle](https://beets.readthedocs.io/en/stable/plugins/ftintitle.html) plugin to add featured artists to the title of the track.

## Is there a better way to do this?

Probably, but that's likely outside the scope of this README.

Just kidding, I'll write some thoughts on that. `beets-alternatives` is a sweet plugin and super useful for these kinds of use cases, though in its current state I do believe it assumes the target device is capable of reading metadata in the same way as the primary reader of your "main" library.

I use Jellyfin to read my music library directly and primarily interface with my music library that way. The motivation for finding a solution like this was purchasing a Snowsky/Fiio Echo Mini, which is pretty bad at reading tags. I could set up the bulk of my library to write tags in a way that's readable for the Echo Mini but that comes at the cost of compromising on Jellyfin's abilities.

What I'd do, if given the time and ability, is create a new configuration tag for `beets-alternatives` that simply remaps tags onto each other, like so:
```
alternatives:
  external-player:
    ---
    remap:
      artist: albumartist
      sort-artist: sort-albumartist
      some-other-tag: a-different-tag
      etc: etcetc
```
But until I get the time and ability, this is what I've got for now.

## Credits
- [beets-alternatives plugin authors](https://github.com/geigerzaehler/beets-alternatives) for their tool
- [waterlubber](https://github.com/waterlubber) for [their script](https://github.com/geigerzaehler/beets-alternatives/issues/147#issuecomment-3283707097)
