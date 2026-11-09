import os
from openai import OpenAI
from telegram import Bot

# توکن‌ها و آیدی‌ها
BOT_TOKEN = os.getenv("9128434188:AAGhTbMhQNYDhbcaO34ep31sPed42T9BAOc")
CHANNEL_ID = os.getenv("-1004409822301")
DEEPSEEK_API_KEY = os.getenv("ng-a346f3f0f550a7afe11a646154a97370")

# تنظیم اتصال به دیپ سیک
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

def generate_post():
    prompt = "یک پست کوتاه، جذاب و حرفه‌ای درباره امنیت سایبری، هک اخلاقی یا یک آسیب‌پذیری جدید به زبان فارسی بنویس. حتماً از ایموجی‌های مرتبط استفاده کن و متن رو برای کانال تلگرام آماده کن."
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a cyber security expert writing for a Telegram channel."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response.choices[0].message.content

def send_to_telegram(text):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='Markdown')

if __name__ == "__main__":
    print("در حال تولید پست با دیپ سیک...")
    post_content = generate_post()
    print("ارسال به تلگرام...")
    send_to_telegram(post_content)
    print("با موفقیت ارسال شد!")
