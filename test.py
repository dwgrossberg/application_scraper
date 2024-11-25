import requests
import json


def test():
    url = 'http://127.0.0.1:5000/splitter'
    with open('test_data.json') as f:
        data = json.load(f)
    res = requests.post(url, json=data)
    print(res.json())


if __name__ == "__main__":
    test()
