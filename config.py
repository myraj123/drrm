import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '6522419017:AAFG583zNPeM_GZ0UMF4q776s0BSvR3vrGA')
    API_ID = int(os.environ.get("API_ID", '27536109'))
    API_HASH = os.environ.get("API_HASH", 'b84d7d4dfa33904d36b85e1ead16bd63')
    AUTH_USER = os.environ.get('AUTH_USERS','6133987831').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    WEBHOOK = True  # Don't change this
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "ALONE🛡️"#Here You Can Change with Your Name  or any custom name or title you prefer
    PORT = int(os.environ.get('PORT', 8080))  # Default to 8000 for local testing

