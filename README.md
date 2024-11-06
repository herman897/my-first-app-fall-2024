# my-first-app-fall-2024

## Setup

Create and activate a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever revisiting):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
ALPHAVANTAGE_API_KEY="..."
```

## Usage 

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
python app/unemployment.py
```

Run the stocks report:

```sh
python app/stocks.py
```

Run the email sender:

```sh
python app/email_service.py
```

Run the rps game:
```sh
python app/rps.py
```