playlist = input().split()
n = int(input())

for _ in range(n):
    command = input()
    parts = command.split(" * ")
    action = parts[0]

    if action == "Add Song":
        song = parts[1]
        if song not in playlist:
            playlist.append(song)
            print(f"{song} successfully added")

    elif action == "Delete Song":
        song_number = int(parts[1])

        if song_number <= len(playlist):
            deleted = []

            for i in range(song_number):
                deleted.append(playlist[i])

            for i in range(song_number):
                playlist.pop(0)

            for i in range(len(deleted)):
                if i == len(deleted) - 1:
                    print(deleted[i], end="")
                else:
                    print(deleted[i], end=", ")

            print(" deleted")

    elif action == "Shuffle Songs":
        index1 = int(parts[1])
        index2 = int(parts[2])

        if 0 <= index1 < len(playlist) and 0 <= index2 < len(playlist):
            playlist[index1], playlist[index2] = playlist[index2], playlist[index1]
            print(f"{playlist[index1]} is swapped with {playlist[index2]}")

    elif action == "Insert":
        song = parts[1]
        index = int(parts[2])

        if index < 0 or index > len(playlist):
            print("Index out of range")
        else:
            if song in playlist:
                print("Song is already in the playlist")
            else:
                playlist.insert(index, song)
                print(f"{song} successfully inserted")

    elif action == "Sort":
        playlist.sort(reverse=True)

    elif action == "Play":
        print("Songs to Play:")
        for song in playlist:
            print(song)