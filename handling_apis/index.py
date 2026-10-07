import requests


def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)

    data = response.json()

    if data["statusCode"] == 200 and data["success"]:
        user_data = data["data"]
        return user_data
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        user_data = fetch_random_user()
        print(user_data)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()