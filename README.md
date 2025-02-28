# Weather API

This is a simple Weather API built with FastAPI that fetches weather data from an external API.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Weather_Api.git
    cd Weather_Api
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `settings.py` file in the root directory with your API key:
    ```python
    # settings.py
    class Settings:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        api_key = "your_api_key_here"

    settings = Settings()
    ```

## Running the API

### Run in dev mode
```bash
fastapi dev app.py```

### Run in prod mode
```bash
fastapi run app.py
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

### Get Weather

- **URL:** `/weather/{city}`
- **Method:** `GET`
- **Response:**
    ```json
    {
        "city": "City Name",
        "temperature": 20.5,
        "description": "clear sky",
        "humidity": 60,
        "wind_speed": 5.1
    }
    ```

## Example

To get the weather for London, you can make a GET request to:
```
http://127.0.0.1:8000/weather/London
```

## License

This project is licensed under the MIT License.
