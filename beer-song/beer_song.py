def recite(start, take=1):
    song = []
    song_verse_1 = "{} {} of beer on the wall, {} {} of beer."
    song_verse_2 = "Take one down and pass it around, {} {} of beer on the wall."
    song_verse_3 = "Take it down and pass it around, no more bottles of beer on the wall."
    song_verse_4 = "No more bottles of beer on the wall, no more bottles of beer."
    song_verse_5 = "Go to the store and buy some more, 99 bottles of beer on the wall."
    while take:
        if len(song) >= 2:
            song.append("")
        if start == 1:
            song.append(song_verse_1.format(start, 'bottle', start, 'bottle'))
            song.append(song_verse_3)
        if start == 0:
            song.append(song_verse_4)
            song.append(song_verse_5)
        if start >= 2:
            song.append(song_verse_1.format(start, "bottles", start, "bottles"))
            if start == 2:
                song.append(song_verse_2.format(start - 1, 'bottle'))
            else:
                song.append(song_verse_2.format(start-1, "bottles"))
        take -= 1
        start -= 1
    return song



