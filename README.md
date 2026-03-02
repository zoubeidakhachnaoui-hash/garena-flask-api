# Flask API for Garena Login

#H4RDIXXXXX IS HERE?

This project provides a Flask API wrapper for the Garena login process, based on the provided Python script. It exposes a single endpoint to handle user authentication and retrieve relevant tokens.

## Features

*   **Garena Login:** Authenticates users against the Garena platform.
*   **Token Retrieval:** Returns `access_token`, `open_id`, `jwt`, and `decoded_jwt`.
*   **AES Encryption:** Utilizes AES encryption for secure communication.

## Setup

### Prerequisites

Before running the API, ensure you have the following installed:

*   Python 3.x
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Install dependencies:**

    ```bash
    pip install Flask requests pycryptodome
    ```

## Usage

### Running the API

To start the Flask API server, run the `app.py` file:

```bash
python app.py
```

The API will be accessible at `http://0.0.0.0:5000`.

### API Endpoint

*   **Endpoint:** `/login`
*   **Method:** `POST`
*   **Content-Type:** `application/json`

#### Request Body

The request body should be a JSON object containing the `uid` and `password`:

```json
{
    "uid": "YOUR_UID",
    "password": "YOUR_PASSWORD"
}
```

#### Example Request (using `curl`)

```bash
curl -X POST -H "Content-Type: application/json" -d '{"uid": "4562891100", "password": "H4XRKBYYBY2F-S1X_TEAM"}' http://127.0.0.1:5000/login
```

#### Example Response

```json
{
    "access_token": "<your_access_token>",
    "open_id": "<your_open_id>",
    "jwt": "<your_jwt>",
    "decoded_jwt": {
        // Decoded JWT payload
    }
}
```

## Test Credentials

You can use the following credentials for testing purposes:

*   **UID:** `4562891100`
*   **PASSWORD:** `H4XRKBYYBY2F-S1X_TEAM`

## Disclaimer

This project is provided for educational and informational purposes only. Use at your own discretion.

#H4RDIXXXXX IS HERE?
