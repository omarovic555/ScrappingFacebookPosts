from fastapi import APIRouter     
from services.scraper import FacebookScraper


router = APIRouter()


@router.get('/savedata')
async def savedata(pageId: str) :
    """
    Saves scraped data from the specified URL to a file.

    Args:
        pageId (str): The pageId to scrape data from.

    Returns:
        A Json containing information about the scraping operation, including the status
        and any error messages or details.

    Example:
        To save scraped data from the URL https://facebook.com/pageAlpha, make a GET request to the endpoint:
        /savedata?url=pageAlpha
    """
    scraper = FacebookScraper()
    result = await scraper.create_table_and_insert_data(pageId)
    return result