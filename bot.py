import os
from telegram import Bot
from datetime import datetime

# ===== ENV VARIABLES =====
BOT_TOKEN = os.environ.get("BOT_TOKEN")          # GitHub Secret
CHANNEL_ID = os.environ.get("CHANNEL_ID")        # GitHub Secret, ex: @smartdealsindia5
AFFILIATE_TAG = os.environ.get("AFFILIATE_TAG")  # GitHub Secret, ex: smartdeals063-21

bot = Bot(token=BOT_TOKEN)

# ===== AMAZON PRODUCT LONG LINK =====
PRODUCT_LONG_LINK = "https://www.amazon.in/SWORNOF-Womens-Kanjivaram-Patola-Blouse/dp/B0C5CPYGYV?_encoding=UTF8&pd_rd_w=zhanZ&content-id=amzn1.sym.fa294cf3-99e4-435e-8284-16ec3b3e2443%3Aamzn1.symc.752cde0b-d2ce-4cce-9121-769ea438869e&pf_rd_p=fa294cf3-99e4-435e-8284-16ec3b3e2443&pf_rd_r=A1KKHTJ7W2H2ZZV3A8Y7&pd_rd_wg=BRoOG&pd_rd_r=aee07f8c-a15d-40c1-8d98-bf0f3c1ed7d7&th=1&linkCode=ll2&tag=smartdeals063-21&linkId=6c8e9a281135e9d5ba2522c1d99e3048&ref_=as_li_ss_tl"

# ===== HELPER FUNCTION =====
def clean_amazon_link(long_url, tag):
    try:
        asin = long_url.split("/dp/")[1].split("/")[0]
        return f"https://www.amazon.in/dp/{asin}/?tag={tag}"
    except IndexError:
        return long_url

def create_post_message(product_name, product_url):
    affiliate_link = clean_amazon_link(product_url, AFFILIATE_TAG)
    message = f"""
🔥 *Amazon Deal Alert* 🔥

🛍️ {product_name}

👉 Buy Now:
{affiliate_link}

⏰ Limited Time Offer!
"""
    return message

# ===== MAIN FUNCTION =====
def main():
    product_name = "SWORNOF Womens Kanjivaram Patola Blouse"
    message = create_post_message(product_name, PRODUCT_LONG_LINK)
    bot.send_message(chat_id=CHANNEL_ID, text=message)
    print(f"Posted to {CHANNEL_ID} at {datetime.now()}")

# ===== ENTRY POINT =====
if __name__ == "__main__":
    main()
