import requests

def main():
    parse_json()

def parse_json():
    json_arr = get_api() 
    # for obj in json_arr:
    #     sentiment = {obj['sentiment']}
    #     ticker = {obj['ticker']}
    #     n_comments = {obj['no_of_comments']}
    #     print(f"The boys are {sentiment} about {ticker}")
    print(json_arr)



def get_api():
    url = "https://tradestie.com/api/v1/apps/reddit" 
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    main()
