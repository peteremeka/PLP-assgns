import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get URL from user
    url = input("Please enter the image URL: ").strip()

    if not url:
        print("✗ No URL provided. Exiting.")
        return

    if not url.startswith("https://"):
        print("✗ Insecure URL. Only HTTPS links are allowed.")
        return

    try:
        # Create directory if it doesn't exist
        save_dir = "Fetched_Images"
        os.makedirs(save_dir, exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes

        # Check if the response is actually an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ URL did not return an image. Content-Type: {content_type}")
            return

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename or '.' not in filename:
            # Try to infer extension from content-type
            ext = content_type.split("/")[-1]
            filename = f"downloaded_image.{ext}"

        # Save the image
        filepath = os.path.join(save_dir, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
