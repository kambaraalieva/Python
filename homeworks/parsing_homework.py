import requests
from bs4 import BeautifulSoup

URL = "https://www.mashina.kg/search/all/"

def parse_cars():
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    cars = []

    # find all car cards (change selector if needed)
    car_cards = soup.find_all("div", class_="list-item")

    for car in car_cards:
        car_data = {
            "title": None,
            "price": None,
            "year": None,
            "city": None,
            "link": None
        }

        title_tag = car.find("div", class_="block title")
        price_tag = car.find("div", class_="block price")
        year_tag = car.find("span", class_="year")
        city_tag = car.find("span", class_="city")
        link_tag = car.find("a")

        if not title_tag or not price_tag or not link_tag:
            continue

        if title_tag:
            car_data["title"] = title_tag.text.strip()

        if price_tag:
            car_data["price"] = price_tag.text.strip()

        if year_tag:
            car_data["year"] = year_tag.text.strip()

        if city_tag:
            car_data["city"] = city_tag.text.strip()

        if link_tag:
            car_data["link"] = "https://www.mashina.kg" + link_tag.get("href")

        cars.append(car_data)

    return cars


if __name__ == "__main__":
    result = parse_cars()

    for i, car in enumerate(result, start=1):
        print(f"{i}. {car}")
