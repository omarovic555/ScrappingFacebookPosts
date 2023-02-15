"""
This module defines a FastAPI application that includes two routers: one for web scraping Facebook posts,
and another one for saving the scraped data into a SQLAlchemy database. It also defines a simple index route.

The application can be launched by running the module directly with Python.

Functions:
- index: A simple route that returns a dictionary message.
- main: The entry point of the application, that launches the FastAPI application using the Uvicorn server.
"""

import uvicorn
from fastapi import FastAPI
from apis import file_fb_posts_scraping, file_save_scraping_data

app = FastAPI()

app.include_router(file_fb_posts_scraping.router)
app.include_router(file_save_scraping_data.router)

@app.get('/')
def index() -> dict:
    """
    A simple route that returns a dictionary message.

    Returns:
    dict: A dictionary with a message.
    """
    return {'Message': 'This is a simple API!'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    