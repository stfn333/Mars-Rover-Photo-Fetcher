# Mars Rover Photo Fetcher

![Mars Rover](link-to-your-image.png)

This Python program allows you to fetch and display photos taken by NASA's Mars rovers (Curiosity, Opportunity, and Spirit) on a specified Earth date. The data is obtained from the [Mars Rover Photos API](https://api.nasa.gov/mars-photos/api/v1/rovers) maintained by Chris Cerami.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [Example Queries](#example-queries)
- [API Documentation](#api-documentation)
- [Credits](#credits)

## Features

- **Rover Selection:** Choose between Curiosity, Opportunity, and Spirit.
- **Date Selection:** Enter a specific Earth date to view photos taken on that day.
- **API Integration:** Utilizes the [Mars Rover Photos API](https://api.nasa.gov/mars-photos/api/v1/rovers) to retrieve data.

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/mars-rover-photo-fetcher.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mars-rover-photo-fetcher
    ```

3. Install dependencies (ensure you have Python and `requests` installed):

    ```bash
    pip install requests
    ```

4. Run the program:

    ```bash
    python fetch_photos.py
    ```

5. Follow the prompts to select the rover and enter the Earth date.

## Example Queries

- Fetch photos on a specific Martian sol:

    ```bash
    https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY
    ```

- Fetch photos on a specific Earth date:

    ```bash
    https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY
    ```

## API Documentation

Refer to the [Mars Rover Photos API documentation](https://api.nasa.gov/mars-photos/api/v1/rovers) for detailed information on available queries, parameters, and camera abbreviations.

## Credits

- [Chris Cerami](https://github.com/corincerami) - Maintainer of the Mars Rover Photos API.

Feel free to contribute, report issues, or suggest improvements! 🚀
