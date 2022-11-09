# MusicSort
Sorts music files by reading ID3 tags in accordance to plex's recommended file structure.


## Sorting File Structure
```
/Root
  /AlbumArtist
    /Album
      /File
```
   

## Requirements
* Python3
* Mutagen

```pip install mutagen```

## Usage

```python MusicSorter.py```

## Known Bugs
* Wav's are not supported by Mutagen. Wav files will be copied to their own folder called /Wav's, but not sorted furhter.

## Drawbacks
* This program is reliant on files having proper ID3 tags. If they are incorrect, the files will be sorted incorrectly.
* If the ID3 tags are missing from a file, the files will be sorted into their designated folders depending on which tags they are missing. The priority is Title,Artist,Album,AlbumArtist

```
/Root
  /No Title
  /No Artist
  /No Album
  /No Album Artist
```


