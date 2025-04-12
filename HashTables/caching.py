"""
Caching with hash tables

Store results so we don't recompute/refetch
"""

cache = {}


def get_page(url):
    if url in cache:
        print(f"Returning cached: {url}")
        return cache[url]

    print(f"Fetching: {url}")
    # pretend we're fetching
    data = f"<html>{url}</html>"
    cache[url] = data
    return data


get_page("google.com")
get_page("facebook.com")
get_page("google.com")  # cached!
get_page("google.com")  # still cached
