import instaloader
import sys
import os

def download_profile(username):
    try:
        # Create an instance of Instaloader
        L = instaloader.Instaloader()
        
        # Create a directory for downloads
        download_dir = f"downloads_{username}"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        # Get profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        print(f"\nDownloading content from {username}'s profile...")
        
        # Download posts
        print("\nDownloading posts...")
        for post in profile.get_posts():
            L.download_post(post, target=download_dir)
        
        # Download stories
        print("\nDownloading stories...")
        try:
            L.download_stories(userids=[profile.userid], filename_target=download_dir)
        except Exception as e:
            print(f"Note: Could not download stories - {str(e)}")
        
        print(f"\nDownload complete! Content saved in '{download_dir}' folder")
        
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile '{username}' does not exist")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python instagram_downloader.py username")
        sys.exit(1)
    
    username = sys.argv[1]
    download_profile(username) 