import telebot
from facebook_scraper import get_posts
from loguru import logger
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('C:/Users/user/Desktop/ScrappingFacebookPosts/app/config.env')
load_dotenv(dotenv_path=dotenv_path)
TOKEN = os.getenv('TOKEN')

BOT_CHAT_ID = "6091946077"
CHAT_ID = "2123256274"

bot = telebot.TeleBot(TOKEN)
x = bot.get_me()

@bot.message_handler(func=lambda message: message.text)
def handle_number(message):
    """
    Handle messages containing a Facebook page name.
    Scrape the page for the first 3 sections and send the posts data back to the user.

    Args:
        message (telebot.types.Message): The message object containing the Facebook page name.

    Returns:
        None.
    """
    posts: list = []

    # Get the first 3 sections from a Facebook page
    for post in get_posts(message.text, pages=3):
        post_data = {
            "post_id": post['post_id'],
            "time": post['time'],
            "text": post['text'][:199],
            "likes": post['likes'],
            "shares": post['shares'],
            "comments": post['comments']
        }
        posts.append(post_data)
        logger.info("PostId:" + post['post_id'])

    # Send the result back to the user
    bot.send_message(CHAT_ID,str(posts))

# Start the bot
bot.polling(timeout=120)

