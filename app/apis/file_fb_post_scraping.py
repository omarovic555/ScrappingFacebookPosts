from fastapi import APIRouter
from services import file_fb_post_scraping_service

router = APIRouter()

@router.get('/scraper')
async def scraper(pageId: str) :
    """
    Scrapes Facebook posts from the specified URL and returns the results as a list of dictionaries.

    Args:
        pageId (str): The pageId to scrape Facebook posts from.

    Returns:
        A JSON data describes an array, and each element of that array is an object: representing scraped Facebook posts. Each array contains
        information about a single post, such as the post's text, author, and timestamp.

    Example:
        To scrape Facebook posts the URL https://facebook.com/pageAlpha, make a GET request to the endpoint:
        /scraper?url=pageAlpha
    """
    result = await file_fb_post_scraping_service.get_scraped_posts(pageId)
    return result
