import os
import requests
from rich import print

from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("API_KEY")


def main():
    parse_reddit_json()


def parse_reddit_json():
    request_url = "https://apewisdom.io/api/v1.0/filter/wallstreetbets/page/1"
    json_obj = get_api(request_url)

    first_stock = json_obj["results"][0]

    ticker = first_stock["ticker"]
    name = first_stock["name"]
    mentions = first_stock["mentions"]
    upvotes = first_stock["upvotes"]

    print(
        f"{ticker} AKA {name} is ranked #1 on /r/WallstreetBets with {mentions} mentions and {upvotes} upvotes!"
    )
    parse_polygon_json(ticker)


def parse_polygon_json(ticker):
    request_url = (
        f"https://api.polygon.io/v2/reference/news?ticker={ticker}&apiKey={api_key}"
    )
    json_obj = get_api(request_url)
    first_title = json_obj["results"][0]["title"]
    first_author = json_obj["results"][0]["author"]
    first_article_url = json_obj["results"][0]["article_url"]

    print(f"Acording to {first_author}\n{first_title}")
    print(f"Check it out here {first_article_url}")


def get_api(request_url):
    url = request_url
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    main()
