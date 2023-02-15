from fastapi.testclient import TestClient
from loguru import logger
import uvicorn
import sys
sys.path.append("..")  # Add path to root directory
from app import app  # Import app from root directory
import pytest

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Message': 'This is a simple API!'}
    
def test_scraper():
    """
    Tests the /scraper endpoint.

    Verifies that the endpoint returns a 200 status code, a dictionary in the response, and that the
    dictionary contains at least one key-value pair.
    """
    response = client.get("/scraper?pageId=GuinnessWorldRecords")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) > 0
    logger.info("TestScraper Passed")

if __name__ == "__main__":
   
    pytest.main()