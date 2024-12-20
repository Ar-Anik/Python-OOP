"""
Imagine we're working on a project that uses an external library to fetch data from an API. The API method occasionally fails, and we need a
quick fix to retry the request. Instead of modifying the library, we can monkey patch the method to add retry logic.
"""

import requests
from time import sleep

original_get = requests.get

def get_with_retry(url, max_retries=3, delay=2, backoff=2, **kwargs):
    retries = 0
    while retries < max_retries:
        try:
            response = original_get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            """ requests.exceptions.RequestException is the base exception class for all exceptions raised by the requests library """
            retries += 1
            print(f"Attempt {retries} failed: {e}")
            if retries < max_retries:
                sleep_time = delay * (backoff ** (retries - 1))
                print(f"Retrying in {sleep_time} seconds...")
                sleep(sleep_time)
            else:
                print("Max retries reached. Raising the exception.")
                """
                    The raise keyword re-raised exception exits the get_with_retry function. The calling code (the part where requests.get(url) is called) 
                    has an except Exception as e block to catch any exceptions raised during the execution.
                """
                raise

requests.get = get_with_retry

try:
    response = requests.get("https://jsonplaceholder.typi1code.com/posts/?_limit=2")
    print(response)
except Exception as e:
    print(f"Failed to fetch data: {e}")
