import requests
import json


def test():
    url = 'https://location-splitter-6a8b6f1a4160.herokuapp.com/splitter'
    with open('data.json') as f:
        data = json.load(f)
    res = requests.post(url, json=data)
    print(res.json())
    with open("data.json", "w") as json_file:
        json.dump(res.json(), json_file, indent=4)


if __name__ == "__main__":
    test()
