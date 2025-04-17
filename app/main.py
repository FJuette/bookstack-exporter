import os
import logging
import sys
import asyncio
from typing import List, Optional
from datetime import datetime

import httpx
from dotenv import load_dotenv
from httpx import AsyncClient
from pydantic import BaseModel, HttpUrl

# Load environment variables from .env file
load_dotenv(override=True, verbose=True)


def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        print(f"Error: The environment variable '{var_name}' is not set.")
        sys.exit(1)
    return value


# Get global variables from environment
bookstack_token = get_env_variable('BOOKSTACK_TOKEN')
bookstack_url = get_env_variable('BOOKSTACK_URL')
export_dir = get_env_variable('EXPORT_DIR')
export_format = get_env_variable('EXPORT_FORMAT')

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Authorization: Token <token_id>:<token_secret>
headers = {'Authorization': f'Token {bookstack_token}'}


class Cover(BaseModel):
    id: int
    name: str
    url: HttpUrl


class DataItem(BaseModel):
    id: int
    name: str
    slug: str
    description: str
    created_at: datetime
    updated_at: datetime
    created_by: int
    updated_by: int
    owned_by: int
    cover: Optional[Cover]  # Cover can be None, so it's Optional


class BooksModel(BaseModel):
    data: List[DataItem]
    total: int


async def store_book(client: AsyncClient, book: DataItem):
    url = f'{bookstack_url}/api/books/{book.id}/export/'
    file_ending: str = ''
    if export_format == 'pdf':
        url = url + 'pdf'
        file_ending = 'pdf'
    elif export_format == 'markdown':
        url = url + 'markdown'
        file_ending = 'md'
    elif export_format == 'html':
        url = url + 'html'
        file_ending = 'html'

    logger.debug(f'Try to download book {book.name} as {file_ending}...')
    blob_r = await client.get(url, headers=headers)
    if blob_r.status_code == 200:
        with open(f'{export_dir}/{book.name}.{file_ending}', 'wb') as f:
            f.write(blob_r.content)
        logger.debug(f"Book {book.name} downloaded successfully.")
    else:
        logger.error(f"Failed to download book {book.id}: {blob_r.status_code}")


async def store_books():
    r = httpx.get(f'{bookstack_url}/api/books', headers=headers)
    books = BooksModel(**r.json())
    async with httpx.AsyncClient() as client:
        tasks = [store_book(client, book) for book in books.data]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(store_books())
