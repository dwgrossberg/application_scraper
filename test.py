import requests
import json


def test():
    url = 'http://127.0.0.1:5000/splitter'
    with open('data.json') as f:
        data = json.load(f)
    res = requests.post(url, json=data)
    print(res.json())
    with open("data.json", "w") as json_file:
        json.dump(res.json(), json_file, indent=4)


if __name__ == "__main__":
    test()
