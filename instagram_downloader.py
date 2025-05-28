import instaloader
import os
import sys

def download_instagram_content():
    print("Instagram Content Downloader")
    print("---------------------------")
    
    # Get username input
    username = input("Enter Instagram username: ").strip()
    
    if not username:
        print("Error: Please enter a username")
        return

    try:
        # Create directory for downloads
        download_dir = f"downloads_{username}"
        os.makedirs(download_dir, exist_ok=True)
        
        print(f"\nDownloading content for @{username}...")
        
        # Initialize Instaloader with custom directory
        L = instaloader.Instaloader(dirname_pattern=download_dir)
        
        # Download posts and profile picture
        print("Downloading posts and photos...")
        L.download_profile(username, profile_pic_only=False)
        
        # Try to download stories (will require login for private profiles)
        try:
            print("Attempting to download stories...")
            profile = instaloader.Profile.from_username(L.context, username)
            L.download_stories(userids=[profile.userid], filename_target=download_dir)
        except Exception as e:
            print("Note: Could not download stories (this is normal for public profiles)")
        
        print(f"\nSuccess! Content downloaded to folder: {download_dir}")
        print("\nDownloaded content includes:")
        print("- All photos and videos from posts")
        print("- Profile picture")
        print("- Post captions and metadata")
        
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"\nError: Profile @{username} does not exist")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"\nError: Cannot access private profile @{username}")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    try:
        download_instagram_content()
    except KeyboardInterrupt:
        print("\nDownload cancelled by user")
        sys.exit(0) 