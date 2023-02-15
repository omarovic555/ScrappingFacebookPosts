from facebook_scraper import get_posts
from loguru import logger

async def get_scraped_posts(pageId: str):

    """
    Scrape posts from a given Facebook page URL.

    Args:
        url (str): The URL of the Facebook page to scrape.

    Returns:
        dict: A dictionary containing a message indicating the end of the scraping process, and a
              list of post objects, where each object contains the post ID, time, truncated text,
              likes count, shares count, and comments count.

    Raises:
        HTTPException: If the Facebook page cannot be reached or if the page does not exist.
    """
    # Initialize an empty list to store the posts
    posts: list = []

    # Get the first 3 sections from a Facebook page 'GuinnessWorldRecords'
    for post in get_posts(pageId, pages=3):
        post_data = {
            "post_id": post['post_id'],
            "time": post['time'],
            "text": post['text'][:199],
            "likes": post['likes'],
            "shares": post['shares'],
            "comments": post['comments']
        }
        posts.append(post_data)
        logger.info("PostId:"+post['post_id'])
     
    return {"message": "End of scraping", "posts": posts }

