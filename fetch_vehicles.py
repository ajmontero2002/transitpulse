import requests
from google.transit import gtfs_realtime_pb2

FEED_URL = "https://cdn.mbta.com/realtime/VehiclePositions.pb"

def fetch_feed(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response.content)
    return feed

def main():
    feed = fetch_feed(FEED_URL)
    print(f"Vehicles in feed: {len(feed.entity)}")


if __name__ == "__main__":
    main()
