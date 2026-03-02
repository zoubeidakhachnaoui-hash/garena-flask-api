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

*   **Endpoint:** `/xg`
*   **Method:** `GET`

#### Query Parameters

The `uid` and `Pw` parameters should be passed as query parameters in the URL.

#### Example Request (using `curl`)

```bash
curl "http://127.0.0.1:5000/xg?uid=4562891100&Pw=H4XRKBYYBY2F-S1X_TEAM"
```

#### Example Response

```json
{
    "access_token": "86cbe7f6aa662083b4c0e70016bfe6777f72eeb95fffb35b36f3415887416a1f",
    "decoded_jwt": {
        "account_id": 14860324772,
        "client_type": 1,
        "client_version": "1.120.3",
        "country_code": "BR",
        "emulator_score": 0,
        "exp": 1772450909,
        "external_id": "e3b9787cac0e27df2625a633091fd30f",
        "external_type": 4,
        "external_uid": 4562891100,
        "is_emulator": false,
        "lock_region": "ME",
        "lock_region_time": 1772036631,
        "nickname": "H4XPCX9FQRI",
        "noti_region": "ME",
        "plat_id": 0,
        "reg_avatar": 102000007,
        "release_channel": "ios",
        "release_version": "OB52",
        "signature_md5": "",
        "source": 2,
        "using_version": 1
    },
    "jwt": "eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxNDg2MDMyNDc3Miwibmlja25hbWUiOiJINFhQQ1g5RlFSSSIsIm5vdGxfcmVnaW9uIjoiTUUiLCJsb2NrX3JlZ2lvbiI6Ik1FIiwiZXh0ZXJuYWxfaWQiOiJlM2I5Nzg3Y2FjMGUyN2RmMjYyNWE2MzMwOTFmZDMwZiIsImV4dGVybmFsX3R5cGUiOjQsInBsYXRfaWQiOjAsImNsaWVudF92ZXJzaW9uIjoiMS4xMjAuMyIsImVtdWxhdG9yX3Njb3JlIjowLCJpc19lbXVsYXRvciI6ZmFsc2UsImNvdW50cnlfY29kZSI6IkJSIiwiZXh0ZXJuYWxfdWlkIjo0NTYyODkxMTAwLCJyZWdfYXZhdGFyIjoxMDIwMDAwMDcsInNvdXJjZSI6MiwibG9ja19yZWdpb24fdGltZSI6MTc3MjAzNjYzMSwiY2xpZW50X3R5cGUiOjEsInNpZ25hdHVyZV9tZDUiOiIiLCJ1c2luZ192ZXJzaW9uIjoxLCJyZWxlYXNlX2NoYW5uZWwiOiJpb3MiLCJyZWxlYXNlX3ZlcnNpb24iOiJPQjUyIiwiZXhwIjoxNzcyNDUwOTA5fQ.ExV9CCCYRzgSrrdBAy9MZIOhfDJrOi6NFTZJKfs7lzkH",
    "open_id": "e3b9787cac0e27df2625a633091fd30f"
}
```

## Test Credentials

You can use the following credentials for testing purposes:

*   **UID:** `4562891100`
*   **PASSWORD:** `H4XRKBYYBY2F-S1X_TEAM`

## Disclaimer

This project is provided for educational and informational purposes only. Use at your own discretion.

#H4RDIXXXXX IS HERE?
