# Mars Rover Photo Fetcher 

![Photo by Curiosity](https://mars.nasa.gov/msl-raw-images/msss/00974/mhli/0974MH0004800050304356C00_DXXX.jpg)

This Python program allows you to fetch and display photos taken by NASA's Mars rovers (Curiosity, Opportunity, and Spirit) on a specified Earth date. The data is obtained from the [Mars Rover Photos API](https://api.nasa.gov/mars-photos/api/v1/rovers) maintained by Chris Cerami.

## Table of Contents

- [Features](#features)
- [How to Use](#how-to-use)
- [API Documentation](#api-documentation)
- [Credits](#credits)

## Features

- **Rover Selection:** Choose between Curiosity, Opportunity, and Spirit.
- **Date Selection:** Enter a specific Earth date to view photos taken on that day.
- **API Integration:** Utilizes the [Mars Rover Photos API](https://api.nasa.gov/mars-photos/api/v1/rovers) to retrieve data.

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone [https://github.com/your-username/mars-rover-photo-fetcher.git](https://github.com/stfn333/Mars-Rover-Photos-Fetching.git)
    ```

2. Navigate to the project directory:

    ```bash
    cd Mars-Rover-Photos-Fetchingr
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

## API Documentation

Refer to the [Mars Rover Photos API documentation](https://api.nasa.gov/mars-photos/api/v1/rovers) for detailed information on available queries, parameters, and camera abbreviations.

## Credits

- [Chris Cerami](https://github.com/corincerami) - Maintainer of the Mars Rover Photos API.

Feel free to contribute, report issues, or suggest improvements! 🚀
