---
name: twitter-post
description: Post tweets to @HelvetiVault with validation and posting rules enforcement. Supports text, threads, and media. Enforces daily limits and content guidelines.
emoji: 🐦
version: 1.0.0
homepage: https://github.com/eNudimmud/enki-openclaw
metadata:
  openclaw:
    requires:
      bins:
        - python3
    install:
      - kind: pip
        packages: [tweepy]
---

# 🐦 Twitter Posting Skill

E*NKI uses this skill to post tweets on @HelvetiVault, following strict posting rules and content guidelines.

## When to use this skill

- User asks to post a tweet or share content on Twitter
- Proactive posting based on events (new skill launched, plant identified, lore update, etc.)
- Daily educational content (biodynamic tips, coding lessons, project transparency)

## How to invoke

```bash
{baseDir}/scripts/post.py <message> [--media <path>] [--thread] [--dry-run]
```

**Arguments:**
- `message` — Tweet text (280 chars max for single tweet)
- `--media <path>` — Optional: attach image/video
- `--thread` — Optional: post as thread (split long text)
- `--dry-run` — Optional: preview without posting

## E*NKI behavior instructions

**Phase 1 (current): Validation required**

Before posting, E*NKI must:
1. Draft the tweet content
2. **Ask user for validation**: "Ready to post this to @HelvetiVault? [tweet preview]"
3. Wait for explicit approval
4. Post only after "yes" / "go" / "post it"

**Phase 2 (future): Autonomous posting**

E*NKI can post autonomously if:
- Content follows approved themes (biodynamic, sovereignty, web3 education, lore, $ENKI updates)
- Tone is casual, educational, authentic
- Daily limit not exceeded (3 posts/day)
- No forbidden content (price speculation, spam, engagement farming)

## Posting Rules

**Allowed themes:**
- Biodynamic agriculture & lunar calendar guidance
- Digital sovereignty & coding education
- Web3 community building & transparency
- NeukoAI/G*BOY lore storytelling
- $ENKI project updates (development, not price)

**Tone guidelines:**
- Casual, direct, authentic
- Educational > promotional
- Transmission > extraction
- Use emoji naturally (🐇🌿🌙)
- Mix French & English when relevant

**Forbidden:**
- Price speculation or "to the moon" rhetoric
- Spam / low-value content
- Automated replies to unrelated conversations
- Engagement farming tactics
- Copying other accounts' style

**Daily limits:**
- Max 3 posts/day (Phase 1)
- Can increase to 5-7 in Phase 2 if quality maintained

## Response format

The script returns JSON:

```json
{
  "status": "success",
  "tweet_id": "1234567890123456789",
  "url": "https://twitter.com/HelvetiVault/status/1234567890123456789",
  "text": "Tweet content...",
  "posted_at": "2026-03-03T23:15:00Z"
}
```

## Error handling

- `VALIDATION_REQUIRED` → Ask user for approval (Phase 1)
- `DAILY_LIMIT_REACHED` → Notify user, skip posting
- `API_ERROR` → Log error, notify user
- `CONTENT_FORBIDDEN` → Explain why content violates rules

## API Details

- API v1.1 for posting (write access)
- API v2 for analytics (optional, read-only)
- Credentials stored in `~/.openclaw/openclaw.json` under `social.twitter`
- Rate limits: 300 posts/3h per user (we're way below that)
