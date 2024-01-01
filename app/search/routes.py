from fastapi import APIRouter
from metaphor_python import Metaphor
import datetime
import os
from config import config

metaphor = Metaphor(api_key=config.metaphor_key)
router = APIRouter()

@router.get("/search/{topic}")
def search(topic: str):
    # Prepare the search options
    one_week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    search_options = {
        'start_published_date': one_week_ago,
        'num_results': 5,  # Adjust as needed
        'use_autoprompt': True,
        'type': 'neural'
    }

    # Crafted Metaphor-style query
    query = f"Here's what's new and noteworthy in {topic}, including recent studies, expert opinions, articles, and discussions."
    # Perform the search
    response = metaphor.search(query, **search_options)

    # Process and display the results
    return [{"title": result.title, "url": result.url} for result in response.results]