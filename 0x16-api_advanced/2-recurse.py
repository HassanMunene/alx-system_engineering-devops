#!/usr/bin/python3
"""
recurse it.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    # Initializes the hot_list
    if hot_list is None:
        hot_list = []

    # Define the URL for subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'

    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        # Making HTTP GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Checks if the data contains posts
        if 'data' in data and 'children' in data['data']:
            # Extract titles of the current page of posts
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            # Checks if there are more pages
            after_key = data['data']['after']
            if after_key:
                # recursive call to fetch the next page
                return recurse(subreddit, hot_list, after_key)
            else:

                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:

        return None


if __name__ == '__main__':

    subreddit = "hacking"
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
