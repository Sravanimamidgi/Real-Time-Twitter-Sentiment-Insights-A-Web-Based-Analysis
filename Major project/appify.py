from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_pYQYI2DWpXy3ttrTUBP1ICbZsIuLlH0BVIBb")

# Prepare the Actor input
run_input = {
    "startUrls": [
        
    ],
    "searchTerms": [
        "ipl"
    ],
    "twitterHandles": [
    ],
    "conversationIds": [
    ],
    "maxItems": 10,
    "sort": "Top",
    "tweetLanguage": "en",
    "author": "",
    "inReplyTo": "",
    "mentioning": "",
    "geotaggedNear": "",
    "withinRadius": "",
    "geocode": "",
    "placeObjectId": "",
    "minimumRetweets": 0,
    "minimumFavorites": 0,
    "minimumReplies": 0,
    "start": "2024-03-01",
    "end": "2024-04-01",
    "customMapFunction": "(object) => { return {...object} }",
}

# Run the Actor and wait for it to finish
run = client.actor("61RPP7dywgiy0JPD0").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)