from fastapi import APIRouter
from services.file_facebook_scraper_class import *


router = APIRouter()


@router.get('/scrape-posts/{pageId}')
async def scrape_posts(pageId: str):
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
    scraper = FacebookScraper()
    # Appeler la méthode get_scraped_posts sur l'instance scraper de FacebookScraper
    scraped_posts = await scraper.get_scraped_posts(pageId)
    return scraped_posts

