import json

file_name = "youtube.txt"


def load_data():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file, indent=4)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)


    for vid in videos:
        print(vid)

    # if not videos:
    #     print("No videos found.")
    # else:
    #     for index, video in enumerate(videos, start=1):
    #         print(f"{index}. Name: {video['name']} | Time: {video['time']}")

    print("*" * 70)


def add_videos(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")

    videos.append({
        "name": name,
        "time": time
    })

    save_data_helper(videos)

    print("Video added successfully!")


def main():

    videos = load_data()

    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)

            case "2":
                add_videos(videos)

            case "3":
                pass

            case "4":
                pass

            case "5":
                print("Goodbye!")
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
