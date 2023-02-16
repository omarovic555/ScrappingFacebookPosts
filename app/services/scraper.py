from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, DateTime, select, text
from facebook_scraper import get_posts
from loguru import logger
import pandas as pd
import os


class FacebookScraper:

    def __init__(self):
        self.database_url = os.environ.get("DATABASE_URL")
        if not self.database_url:
         self.database_url = "sqlite:///mydatabase.db"
        
    async def get_scraped_posts(self, pageId: str):
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
            logger.info("PostId:" + post['post_id'])

        return {"message": "End of scraping", "posts": posts}

    async def create_table_and_insert_data(self, pageId: str):
        """
        This module contains an asynchronous function for scraping Facebook posts from a given URL,
        and then saving the scraped data into a SQLAlchemy database.

        The function uses the get_posts method from the facebook_scraper library to scrape posts from the
        specified Facebook page, and then creates a new table in the SQLAlchemy database to store the post data.
        The function also inserts the scraped data into the newly created table, and then performs a SELECT
        query to retrieve and log the inserted data.

        The function takes a single argument:
        - pageId (str): A string representing the pageId of the Facebook page to scrape.

        The function returns a list of dictionaries representing scraped Facebook posts. Each dictionary contains
        information about a single post, such as the post's text, author, and timestamp.
        """

        table_name: str = "posts_" + pageId + "_table"
        # Initialize an empty list to store the posts
        posts: list = []

        # Get the first posts from a Facebook page
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
        metadata = MetaData()
        engine = create_engine(self.database_url)
        table = Table(table_name, metadata,
                      Column('post_id', String, primary_key=True),
                      Column('time', DateTime),
              Column('text', String),
              Column('likes', Integer),
              Column('shares', Integer),
              Column('comments', Integer)
              )
        metadata.create_all(bind=engine)
        with engine.connect() as conn:

            for post in posts:
            
             insert_query=table.insert().values(post_id=post['post_id'],
                                              time=post['time'],
                                              text=post['text'],
                                              likes=post['likes'],
                                              shares=post['shares'],
                                              comments=post['comments'])
            
             conn.execute(insert_query)
            select_stmt = select(table)
            conn.execute(select_stmt)
            query = text(f"SELECT post_id,time,likes,comments,shares FROM {table_name}")
            result = conn.execute(query)
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            logger.success("data inserted successfully")
            logger.info(df)
            return(posts)

