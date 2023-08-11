import requests
import os
api_key = os.environ.get('API_KEY')


def main():
    parse_reddit_json()

def parse_reddit_json():
    request_url = "https://tradestie.com/api/v1/apps/reddit" 
    json_arr = get_api(request_url) 

    first_stock = json_arr[0]

    sentiment = first_stock['sentiment']
    ticker = first_stock['ticker']
    n_comments = first_stock['no_of_comments']

    print(f"The boys at /r/WallstreetBets are {sentiment} about {ticker}")
    parse_polygon_json(ticker)

def parse_polygon_json(ticker):
    request_url = f"https://api.polygon.io/v2/reference/news?ticker={ticker}&apiKey={api_key}"
    json_obj = get_api(request_url)
    first_title = json_obj["results"][0]["title"]
    print(first_title)

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
