import os
import requests
from telegram import Bot

# توکن‌ها و آیدی‌ها از Secrets گیت‌هاب خونده میشن
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def generate_post():
    prompt = "یک پست کوتاه، جذاب و حرفه‌ای درباره امنیت سایبری، هک اخلاقی یا یک آسیب‌پذیری جدید به زبان فارسی بنویس. حتماً از ایموجی‌های مرتبط استفاده کن و متن رو برای کانال تلگرام آماده کن."
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "deepseek/deepseek-v4.1-flash",
        "messages": [
            {"role": "system", "content": "You are a cyber security expert writing for a Telegram channel."},
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post("https://api.hormouz.net/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"خطا: {response.status_code} - {response.text}")
        return None

def send_to_telegram(text):
    if not text:
        return
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='Markdown')

if __name__ == "__main__":
    print("در حال تولید پست...")
    post_content = generate_post()
    if post_content:
        print("ارسال به تلگرام...")
        send_to_telegram(post_content)
        print("با موفقیت ارسال شد!")
