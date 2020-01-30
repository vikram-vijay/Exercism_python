def recite(start_verse, end_verse):
    verse_template = "On the {} day of Christmas my true love gave to me: "
    verse_day_and_gift  = [['first', "a Partridge in a Pear Tree."],
          ['second', "two Turtle Doves"],
          ['third', "three French Hens"],
          ['fourth', "four Calling Birds"],
          ['fifth', "five Gold Rings"],
          ['sixth', "six Geese-a-Laying"],
          ['seventh', "seven Swans-a-Swimming"],
          ['eighth', "eight Maids-a-Milking"],
          ['ninth', "nine Ladies Dancing"],
          ['tenth', "ten Lords-a-Leaping"],
          ['eleventh', "eleven Pipers Piping"],
          ['twelfth', "twelve Drummers Drumming"]]

    if start_verse * end_verse <= 0 or start_verse > 12 or end_verse > 12 or start_verse > end_verse:
        raise ValueError("Start day and end day should be between 0 and 13")
    elif start_verse == end_verse:
        verse_template = verse_template.format(verse_day_and_gift[start_verse-1][0])
        listVerse = [verse_day_and_gift[i][1] for i in range(start_verse-1,-1,-1)]
        return [verse_template + ", ".join(listVerse[:-1]) + ", and " + listVerse[-1]] if start_verse != 1 else [verse_template + listVerse[0]]
    else:
        return [recite(i,i)[0] for i in range(start_verse,end_verse+1)]