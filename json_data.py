import requests
import json


headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                     "image/avif,image/webp,image/apng,*/*;q=0.8,application/"
                     "signed-exchange;v=b3;q=0.9",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
           "bx-ajax": "true"}


def get_data(url="https://logbook.itstep.org/auth/get-marks-selects"):
    s = requests.Session()
    response = s.get(url="https://logbook.itstep.org/students/get-stud-vizit", headers=headers)
    print(response.text)

    with open('result.json', "w") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)
