# #!/usr/bin/python3
# # get subs
# from requests import get
# from sys import argv


# def number_of_subscribers(subreddit):
#     """subs"""
#     head = {'User-Agent': 'Dan Kazam'}
#     count = get('https://www.reddit.com/r/{}/about.json'.format(
#         subreddit), headers=head).json()
#     try:
#         return count.get('data').get('subscribers')
#     except:
#         return 0

# if __name__ == "__main__":
#     number_of_subscribers(argv[1])

#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
