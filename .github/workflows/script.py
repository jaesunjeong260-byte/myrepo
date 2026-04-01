import requests
import datetime

def save_github_zen():
    response = requests.get("https://github.com")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if response.status_code == 200:
        content = f"[{now}] GitHub Zen: {response.text}\n"
        # 파일에 추가 기록 (append 모드)
        with open("result.txt", "a", encoding="utf-8") as f:
            f.write(content)
        print(f"저장 완료: {content}")
    else:
        print("API 호출 실패!")

if __name__ == "__main__":
    save_github_zen()
