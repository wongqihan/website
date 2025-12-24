# Instagram Graph API Setup Guide

## Prerequisites
1. Instagram Business or Creator account
2. Facebook Page connected to your Instagram account
3. Facebook Developer account

## Step 1: Convert to Business Account
1. Open Instagram app
2. Go to Settings → Account → Switch to Professional Account
3. Choose "Business" or "Creator"
4. Connect to a Facebook Page (create one if needed)

## Step 2: Create Facebook App
1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Click "My Apps" → "Create App"
3. Choose "Business" type
4. Fill in app details:
   - App Name: "Bobo and Stella Instagram Agent"
   - Contact Email: your email

## Step 3: Add Instagram Graph API
1. In your app dashboard, click "Add Product"
2. Find "Instagram" and click "Set Up"
3. Go to "Instagram Basic Display" → "Create New App"
4. Fill in required fields

## Step 4: Get Access Token
1. Go to Graph API Explorer: https://developers.facebook.com/tools/explorer/
2. Select your app from dropdown
3. Add permissions:
   - `instagram_basic`
   - `instagram_content_publish`
   - `pages_read_engagement`
4. Click "Generate Access Token"
5. **Important**: Convert to Long-Lived Token:
   ```
   https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token}
   ```

## Step 5: Get Instagram Business Account ID
1. In Graph API Explorer, query:
   ```
   me/accounts
   ```
2. Find your Facebook Page ID
3. Query:
   ```
   {page-id}?fields=instagram_business_account
   ```
4. Save the `instagram_business_account` ID

## Step 6: Update .env
Add these to your `.env` file:
```
INSTAGRAM_ACCESS_TOKEN=your_long_lived_token
INSTAGRAM_BUSINESS_ACCOUNT_ID=your_account_id
```

## Next Steps
Once you have these credentials, I'll update the code to use Graph API instead of `instagrapi`.
