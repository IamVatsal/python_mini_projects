import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url: str) -> None:
    try:
        response: Response = requests.get(url)

        #info

        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get("Content-Type", "Unknown")
        server: str = headers.get("Server", "Unknown")
        response_time: float = response.elapsed.total_seconds()


        print(f"\nURL: {url}")
        print(f"Status Code: {status_code}")
        print(f"Content Type: {content_type}")
        print(f"Server: {server}")
        print(f"Response Time: {response_time:.2f} seconds")

    except RequestException as e:
        print(f"Error: {e}")


def main() -> None:
    url: str = input("\nEnter the URL to check status: ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        print(f"\ndefaulting to https://{url}")
        url = "https://" + url
        print(f"if you want to use http://, please enter it manually")
    check_status(url)

if __name__ == "__main__":
    main()