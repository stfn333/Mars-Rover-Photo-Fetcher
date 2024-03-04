import requests
from datetime import datetime


def enter_rover_name():
    """Prompt the user to enter a rover name and validate the input."""
    input_name = input("Enter rover name ([C]uriosity, [O]pportunity, [S]pirit): ")
    rover_name = ""

    # Validate the entered rover name
    if input_name.lower() not in ["c", "o", "s"]:
        print("Please enter a valid rover name.")
        return None
    else:
        # Convert the input to the corresponding rover name
        if input_name == "c":
            rover_name = "curiosity"
        elif input_name == "o":
            rover_name = "opportunity"
        elif input_name == "s":
            rover_name = "spirit"
        return rover_name


def enter_earth_date():
    """Prompt the user to enter an Earth date in 'YYYY-MM-DD' format and validate the input."""
    while True:
        try:
            earth_date = input("Enter Earth date (YYYY-MM-DD): ")
            date_is_valid = datetime.strptime(earth_date, '%Y-%m-%d')
            return earth_date
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'yyyy-mm-dd'.")
            return None


def fetch_photo_information():
    """Fetching information from the NASA API (api.nasa.gov)"""
    rover_name = enter_rover_name()

    # If rover name is not entered properly, return None
    if rover_name is None:
        return None
    else:
        earth_date = enter_earth_date()

        # If Earth date is not entered properly, return None
        if earth_date is None:
            return None
        else:
            url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/photos"
            api_key = "DEMO_KEY"
            params = {"api_key": api_key, "earth_date": earth_date}
            response = requests.get(url, params=params)
            data = response.json()

            # If there are photos for the given date, return the data
            if data != {'photos': []}:
                return data
            else:
                # Print a message if there are no photos for the given date
                print(response)
                print("No photos on that day.")
                return None


def display_photo_information():
    """Display photo information, including rover name, Earth date, and image URLs."""
    data = fetch_photo_information()

    # If there is no valid data, return None
    if data is None:
        return None
    else:
        rover_name = data['photos'][0]['rover']['name']
        earth_date = data['photos'][0]['earth_date']

        # Display the header with rover name and Earth date
        print(f"===== Photos taken by {rover_name.capitalize()} on {earth_date} =====")

        # Extract image URLs from the data and print them
        image_urls = [photo['img_src'] for photo in data['photos']]
        for url in image_urls:
            print(url)


# Trigger the execution of the program
display_photo_information()





