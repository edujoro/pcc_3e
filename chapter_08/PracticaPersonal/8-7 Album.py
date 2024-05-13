def make_album(title, artist,number_songs = None):
    album = {}
    album['title'] = title
    album['artist'] = artist
    if number_songs:
        album['number_songs'] = number_songs

    return album

print(make_album('Master of Puppets', 'Metallica',15))

print(make_album('Afraid to shot strangers', 'Iron Maiden',9))