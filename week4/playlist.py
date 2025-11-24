

liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    },
    "attention" : {
        "artist": "charlie puth",
        "duration": (4, 25),
        "genre": "hiphop",
    },
    "beleiver": {
        "artist": "imagine dragons",
        "duration": (3, 50),
        "genre": "pop",
    },
    "hatikva": {
        "artist": "amami",
        "duration": (3, 15),
        "genre": "Israeli",
    }
}
def delete_song (my_dict):
    song = input("what song would you to delete")
    if song in my_dict:
        my_dict.pop(song)
    elif song == "finish":
        print("here is the edited playlist: ", my_dict)
        return
    else:
        print("song does not exist")

    return my_dict

def search_song (my_dict):
    song = input("what song would you to search for?")
    if song in my_dict:
        delete_Q = input("this song exists, would you like to delete it?")
        if delete_Q == "yes":
            my_dict.pop(song)
            print(f"{song} was deleted")
    elif song == "finish":
        print("here is  playlist: ", liked_songs)
    else:
        print("song does not exist")

    return my_dict


def delete_artist (my_dict):
    artist = input("what artist would you to delete")
    for song in list(my_dict.keys()):
        if my_dict[song]["artist"] == artist:
            my_dict.pop(song)

    return my_dict


def main():
    my_dict = search_song(liked_songs)
    my_dict = delete_artist(my_dict)
    print(my_dict)

    # action = input("what do want to do? search song, search artist, end, print liked songs").lower()
    # if action == "search song":
    #     search_song(liked_songs)
    # elif action == "search artist":
    #     delete_artist(my_dict)


main()







