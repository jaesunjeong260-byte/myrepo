import requests

def check_github_status():
    response = requests.get("https://github.com")
    if response.status_code == 200:
        print(f"GitHub의 오늘의 명언: {response.text}")
    else:
        print("API 호출 실패!")

if __name__ == "__main__":
    check_github_status()
