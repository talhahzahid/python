import sqlite3

conn = sqlite3.connect("youtube.db")

cursor = conn.cursor()

cursor.execute("""
     CREATE TABLE IF NOT EXISTS  videos (
                id INTEGER PRIMART KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
        )
     """)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("*" * 70)
        print("no video found")
        print("*" * 70)
    else:
        print("-" * 30)
        for row in rows:
            print(row)
        print("-" * 30)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_video(videoId, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ? , time = ? WHERE id = ?",
        (new_name, new_time, videoId),
    )
    conn.commit()


def delete_video(videoId):
    cursor.execute("DELETE FROM videos where id = ?", (videoId,))
    conn.commit()


def main():
    while True:
        print("youtube manager app || chose your choise")
        print("1: list all video")
        print("2: add video")
        print("3: update video")
        print("4: delete video")
        print("7: exit")
        choise = input("Enter your choise: ")

        if choise == "1":
            list_videos()
        elif choise == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choise == "3":
            videoId = int(input("Enter video id: "))
            new_name = input("Enter the video name: ")
            new_time = input("Enter the video time: ")
            update_video(videoId, new_name, new_time)
        elif choise == "4":
            videoId = int(input("Enter the video id: "))
            delete_video(videoId)
        elif choise == "7":
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
