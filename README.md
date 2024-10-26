# Real-Time Weather Monitoring System

## Overview

The **Real-Time Weather Monitoring System** is a web application designed to fetch and display real-time weather data for a specified location. It utilizes weather APIs to gather information on temperature, humidity, wind speed, and other weather conditions, providing users with up-to-date information about the weather in their area or any other selected location.

## Features

- Fetches real-time weather data from a weather API.
- Displays current temperature, humidity, wind speed, and other weather-related information.
- Allows users to search for weather conditions in different locations.
- User-friendly interface with a responsive design.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (if required for user preferences or logs)
- **APIs**: OpenWeatherMap (or any other weather API of your choice)

## Prerequisites

1. **Python 3.x** - Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
2. **Flask** - A lightweight WSGI web application framework in Python.
3. **Weather API Key** - Sign up at [OpenWeatherMap](https://openweathermap.org/) (or another weather service) to get an API key.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/real-time-weather-monitoring-system.git
   cd real-time-weather-monitoring-system
   ```

2. **Create a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the API Key**

   - Create a `.env` file in the project root directory and add your API key.
   
     ```env
     WEATHER_API_KEY=your_api_key_here
     ```

5. **Initialize the Database** (if the app uses a database for logging or user preferences)

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the application**

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. Open the application in your browser at `http://127.0.0.1:5000/`.
2. Enter a city name in the search bar and click **Get Weather**.
3. The app will display current weather information for the entered location, including temperature, humidity, wind speed, etc.

## Project Structure

```plaintext
├── app.py                 # Main Flask application file
├── templates/             # HTML templates for the app
│   ├── index.html         # Home page template
│   └── layout.html        # Layout template for consistent styling
├── static/                # Static files (CSS, JavaScript, images)
│   ├── css/
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## API Details

This application fetches data from the OpenWeatherMap API. The API provides the following details:

- **Temperature**: Current temperature in the specified location.
- **Humidity**: Current humidity level.
- **Wind Speed**: Wind speed at the location.
- **Conditions**: Weather conditions such as rain, snow, or clear sky.

## Example API Response (OpenWeatherMap)

```json
{
  "weather": [
    {
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "main": {
    "temp": 298.55,
    "feels_like": 301.86,
    "pressure": 1013,
    "humidity": 44
  },
  "wind": {
    "speed": 5.1
  },
  "name": "London"
}
```

## Future Enhancements

- Allow users to save their favorite locations.
- Display weekly or hourly forecasts.
- Add notifications for severe weather alerts.
- Implement user authentication for a personalized experience.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

---

### Note:
Remember to update the API key and any necessary environment variables before running the application.

