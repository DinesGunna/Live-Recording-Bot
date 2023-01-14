import os

# Bot token from @botfather
BOT_TOKEN = os.environ.get("5785157567:AAH1pfBnLM3khKHM79Pq1xKoWtToEFG4CDU")
# From my.telegram.org/
API_ID = int(os.environ.get("9976721", 0))
API_HASH = os.environ.get("3ef17a8cdb938335bd8ba292e6d816aa")
# For /log cmd
OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "1956698956").split(" ")]
# No time limit for this users
AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "1204927413").split(" ")]
# Time gap after each request (in seconds)
TIME_GAP = int(os.environ.get("TIME_GAP", "360"))
# Bot channel ID for ForceSub, don't forget to add bot in Bot Channel
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", False)
