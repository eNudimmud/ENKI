#!/home/deck/.openclaw/workspace/skills/twitter-post/venv/bin/python3
"""
E*NKI Twitter Posting Script
Posts tweets to @HelvetiVault following strict content guidelines
"""

import sys
import json
import tweepy
from pathlib import Path
from datetime import datetime

# Load credentials from openclaw.json
CONFIG_PATH = Path.home() / ".openclaw" / "openclaw.json"

def load_credentials():
    """Load Twitter API credentials from OpenClaw config"""
    try:
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        
        twitter_config = config.get("social", {}).get("twitter", {})
        creds = twitter_config.get("credentials", {})
        
        if not creds:
            return None, "Twitter credentials not found in openclaw.json"
        
        return creds, None
    except Exception as e:
        return None, f"Failed to load config: {str(e)}"

def check_daily_limit():
    """Check if daily posting limit has been reached"""
    # TODO: Implement daily counter (store in ~/.openclaw/workspace/.twitter-post-count.json)
    # For now, just return True
    return True, 0  # (allowed, count_today)

def post_tweet(text, media_path=None, dry_run=False):
    """Post a tweet to @HelvetiVault"""
    
    # Load credentials
    creds, error = load_credentials()
    if error:
        return {"error": "CREDENTIALS_ERROR", "message": error}
    
    # Check daily limit
    allowed, count = check_daily_limit()
    if not allowed:
        return {
            "error": "DAILY_LIMIT_REACHED",
            "message": f"Daily limit of 3 posts reached. Current count: {count}"
        }
    
    # Dry run: just preview
    if dry_run:
        return {
            "status": "preview",
            "text": text,
            "length": len(text),
            "media": media_path if media_path else None,
            "message": "Dry run — tweet not posted"
        }
    
    try:
        # Authenticate with Twitter API v1.1
        auth = tweepy.OAuth1UserHandler(
            creds["apiKey"],
            creds["apiSecret"],
            creds["accessToken"],
            creds["accessTokenSecret"]
        )
        
        api = tweepy.API(auth)
        
        # Post tweet
        if media_path:
            # Upload media first
            media = api.media_upload(media_path)
            tweet = api.update_status(status=text, media_ids=[media.media_id])
        else:
            tweet = api.update_status(status=text)
        
        # Build response
        tweet_url = f"https://twitter.com/HelvetiVault/status/{tweet.id}"
        
        result = {
            "status": "success",
            "tweet_id": str(tweet.id),
            "url": tweet_url,
            "text": tweet.text,
            "posted_at": tweet.created_at.isoformat(),
            "account": "@HelvetiVault"
        }
        
        # TODO: Increment daily counter
        
        return result
        
    except tweepy.errors.Forbidden as e:
        return {
            "error": "API_FORBIDDEN",
            "message": f"Twitter API forbidden (check permissions): {str(e)}"
        }
    except tweepy.errors.TooManyRequests as e:
        return {
            "error": "RATE_LIMIT",
            "message": "Twitter API rate limit reached. Try again later."
        }
    except Exception as e:
        return {
            "error": "UNKNOWN_ERROR",
            "message": f"Failed to post tweet: {str(e)}"
        }

def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "USAGE_ERROR",
            "message": "Usage: post.py <text> [--media <path>] [--dry-run]"
        }))
        sys.exit(1)
    
    text = sys.argv[1]
    media_path = None
    dry_run = False
    
    # Parse optional arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--media" and i + 1 < len(sys.argv):
            media_path = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--dry-run":
            dry_run = True
            i += 1
        else:
            i += 1
    
    # Validate text length
    if len(text) > 280:
        print(json.dumps({
            "error": "TEXT_TOO_LONG",
            "message": f"Tweet is {len(text)} characters (max 280)",
            "length": len(text)
        }))
        sys.exit(1)
    
    # Post tweet
    result = post_tweet(text, media_path, dry_run)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
