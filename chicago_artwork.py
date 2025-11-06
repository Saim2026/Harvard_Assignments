# This script allows users to search for artworks by a specific artist
# from the Art Institute of Chicago's public API and displays the results
# in the terminal.

import requests

API_URL = "https://api.artic.edu/api/v1/artworks/search"


def fetch_artworks(artist, limit=10):
    """Fetch artworks for a given artist."""
    try:
        response = requests.get(API_URL, params={"q": artist, "limit": limit})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    return response.json().get("data", [])


def display_artworks(artworks, artist):
    """Display all artworks info in the terminal."""
    if not artworks:
        print(f"No artworks found for '{artist}'.")
        return

    print(f"\nFound {len(artworks)} artworks for '{artist}':\n")
    for i, art in enumerate(artworks, start=1):
        title = art.get("title", "Untitled")
        date = art.get("date_start", "Unknown Year")
        art_id = art.get("id", "N/A")
        print(f"{i}. {title} ({date}) [ID: {art_id}]")
    print()


def main():
    print("\n🎨 WELCOME TO THE ART INSTITUTE OF CHICAGO ARTWORK SEARCH")
    print("******************************************************\n")

    artist = input("Enter an artist's name: ").strip()
    limit = input("How many artworks to fetch? (default 10): ").strip()
    limit = int(limit) if limit.isdigit() else 10

    artworks = fetch_artworks(artist, limit)
    display_artworks(artworks, artist)


print("\nExiting Gallery. Goodbye! 🎨\n")

if __name__ == "__main__":
    main()
