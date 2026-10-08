from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    ""
)

db = client["ytmanager"]
video_collection = db["videos"]


def list_videos():
    for video in video_collection.find({}):
        print(
            f"ID: {video['_id']} | "
            f"Name: {video['name']} | "
            f"Time: {video['time']}"
        )


def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_videos(videoId, name, time):
    video_collection.update_one(
        {"_id": ObjectId(videoId)}, {"$set": {"name": name, "time": time}}
    )


def delete_videos(videoId):
    video_collection.delete_one({"_id": ObjectId(videoId)})


def main():
    while True:
        print("\nYoutube Manager App")
        print("1) List all videos")
        print("2) Add video")
        print("3) Update video")
        print("4) Delete video")
        print("7) Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()

            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_videos(name, time)

            case "3":
                videoId = input("Enter the video id: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")

                update_videos(videoId, name, time)

            case "4":
                videoId = input("Enter the video id: ")
                delete_videos(videoId)

            case "7":
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
