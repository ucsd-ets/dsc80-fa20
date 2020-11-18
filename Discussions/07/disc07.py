import requests


def url_list():
    """
    A list of urls to scrape.

    :Example:
    >>> isinstance(url_list(), list)
    True
    >>> len(url_list()) > 1
    True
    """

    return ...


def request_until_successful(url, N):
    """
    Makes a request to url 'N' times and returns a successful
    response, or None if the response is still not successful.

    :Example:
    >>> resp = request_until_successful('http://quotes.toscrape.com', N=1)
    >>> resp.ok
    True
    >>> resp = request_until_successful('http://example.webscraping.com/', N=1)
    >>> isinstance(resp, requests.models.Response) or (resp is None)
    True
    """

    return ...
