import threading
import subprocess
import time
import requests
import os

from flask import Flask

# --- دالة للحصول على رابط ngrok ---
def get_ngrok_url():
    try:
        resp = requests.get("http://127.0.0.1:4040/api/tunnels")
        resp.raise_for_status()
        data = resp.json()
        for tunnel in data.get("tunnels", []):
            if tunnel.get("proto") == "https":
                return tunnel.get("public_url")
    except Exception as e:
        print("Error getting ngrok URL:", e)
    return None

# --- تشغيل Flask ---
def run_flask():
    os.environ["FLASK_APP"] = "app"
    os.environ["FLASK_ENV"] = "development"
    subprocess.run(["flask", "run", "--port", "5000"])

# --- تشغيل ngrok ---
def run_ngrok():
    subprocess.run(["ngrok", "http", "5000"])

# --- طباعة رابط ngrok بمجرد جاهزيته ---
def print_ngrok_url():
    url = None
    while not url:
        url = get_ngrok_url()
        if url:
            print(f"Ngrok URL: {url}")
            # هنا يمكن حفظه في متغير بيئة ليتم استخدامه داخل Flask
            os.environ["NGROK_URL"] = url
        else:
            time.sleep(1)

if __name__ == "__main__":
    # تشغيل Flask و ngrok في خيوط منفصلة
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_ngrok).start()
    print_ngrok_url()
