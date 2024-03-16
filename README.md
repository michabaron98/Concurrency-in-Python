# Concurrency-in-Python

This project demonstrates how to implement concurrency in Python using asyncio and aiohttp libraries for asynchronous HTTP requests.



## Structure
- `main.py`: Contains the main script demonstrating concurrency using asyncio and aiohttp.
- `common.py`: Contains common constants and functions used in the project.
- `async_http_request.py`: Contains functions for asynchronous HTTP requests.
- `http_request.py`: Contains functions for synchronous HTTP requests.
- `timer.py`: Contains decorators to calculate execution time for functions.

### Prerequisites

Make sure you have Python 3.12 installed on your system.

## Local setup

### Installing requirements

Create and activate a virtual environment:

```commandline
python3 -m venv .venv
source .venv/bin/activate
```

Assuming that the `virtualenv` is activated, install the dependencies in the following way:

```commandline
pip install -r requirements.txt
```

### Running manually

```commandline
python main.py
```