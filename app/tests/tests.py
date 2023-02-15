import unittest
from fastapi.testclient import TestClient
import uvicorn
import sys
sys.path.append("..")  # Add path to root directory
from app import app  # Import app from root directory

client = TestClient(app)

class TestScraping(unittest.TestCase):
    """
    Test class for the scraping endpoints in the FastAPI app.
    """

    def test_scraper(self):
        """
        Tests the /scraper endpoint.

        Verifies that the endpoint returns a 200 status code, a list in the response, and that the
        list contains at least one item.
        """
        response = client.get("/scaper?pageId=GuinnessWorldRecords")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
    unittest.main()
    