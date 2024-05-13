def make_album(title, artist,number_songs = None):
    album = {}
    album['title'] = title
    album['artist'] = artist
    if number_songs:
        album['number_songs'] = number_songs

    return album



while True:
    title = input('Ingrese el nombre del titulo del album, sino q para salir: ')
    if title == 'q':
        break
    artist = input('Ingrese el artist del album, sino q para salir: ')
    if artist == 'q':
        break
    cadena_mostrar = make_album(title, artist)
    print(cadena_mostrar)
