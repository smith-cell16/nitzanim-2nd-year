

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
    }
    "beleiver": {
        "artist": "amagine dragons",
        "duration": (3, 50),
        "genre": "pop",
    }
    "hatikva": {
        "artist": "amami",
        "duration": (3, 15),
        "genre": "Israeli",
    }
}
def delete_song (my_dict):
    song = input("what song would you to delete").lower()
    if song in my_dict:
        my_dict.pop(song)
    elif song == "finish":
        print("here is the edited playlist: ", my_dict)
        return
    else:
        print("song does not exist")

    return my_dict

def search_song (my_dict):
    song = input("what song would you to search for").lower()
    if song in my_dict:
        print("song exists")
        my_dict = delete_song(my_dict)
    elif song == "finish":
        print("here is  playlist: ", liked_songs)
    else:
        print("song does not exist")

    return my_dict


def delete_artist (my_dict):
    artist = input("what artist would you to delete").lower()
    for song in my_dict:

        if my_dict[song]["artist"]== artist:
            my_dict.pop(song)

    else:
        print("artist does not exist")
    return my_dict


def main():
    my_dict = search_song(liked_songs)
    my_dict = delete_song(my_dict)
    print(my_dict)



    chice = input("what would you like to do?: add song, search song, delete song")


