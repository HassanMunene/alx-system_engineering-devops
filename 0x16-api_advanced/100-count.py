#!/usr/bin/python3
"""
Count it script.
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, keyword_count=None):
    if keyword_count is None:
        keyword_count = Counter()

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'

    # Sets a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        # Makes HTTP GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Checks if the data contains posts.
        if 'data' in data and 'children' in data['data']:
            # Extract and process the titles
            for post in data['data']['children']:
                title = post['data']['title'].lower()

                # Counts the occurrence of each word in a title
                for keyword in word_list:
                    keyword_count[keyword] += title.count(keyword.lower())

            # Checks if there are more pages.
            after_key = data['data']['after']
            if after_key:
                # Makes a recursive call.
                return count_words(subreddit, word_list, after_key, keyword_count)
            else:
                sorted_counts = sorted(
                    keyword_count.items(), key=lambda x: (-x[1], x[0].lower()))
                for keyword, count in sorted_counts:
                    print(f'{keyword}: {count}')
        else:
            print("No posts found")
    except requests.exceptions.RequestException:
        print("No posts found")


if __name__ == '__main__':
    subreddit = "programming"
    word_list = ["java", "python", "javascript",
                 "scala", "no_results_for_this_one"]
    count_words(subreddit, word_list)
