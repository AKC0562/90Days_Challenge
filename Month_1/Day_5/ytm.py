
import argparse
from ytmusicapi import YTMusic

def main():
    parser = argparse.ArgumentParser(description="Get YT Music song preview")
    parser.add_argument("query", help="Song name, e.g. 'Blinding Lights'")
    args = parser.parse_args()

    ytm = YTMusic()
    results = ytm.search(args.query, filter="songs", limit=10)
    song = results[0]

    vid = song["videoId"]
    title = song["title"]
    artist = song["artists"][0]["name"]

    info = ytm.get_song(vid)
    streams = info["streamingData"]["adaptiveFormats"]
    audio = [s for s in streams if s["mimeType"].startswith("audio/")]
    audio.sort(key=lambda s: s["bitrate"], reverse=True)

    print(f"{title} – {artist}")

if __name__ == "__main__":
    main()