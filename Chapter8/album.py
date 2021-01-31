print("------------------Chapter 8, Exercise 8-7 & 8-8---------------------------")
def make_album(artist, title, tracks=None):
    """Build a Dictionary containing information about an album."""
    album_dict = {'Artist': artist,'Title': title}
    if tracks:
        album_dict['Tracks'] = tracks
    return album_dict

album = make_album('Seether', 'Holding Onto Strings Better Left To Fray', tracks= 7)
print(album)
album = make_album('MDFMK', 'MDFMK')
print(album)
album = make_album('Ryan Shupe & The Rubberband', 'Simplify', tracks=4)
print(album)

