#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id
variable found in the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        X_Request_Id = response.info().get("X-Request-Id")
        print(X_Request_Id)