if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1882387496:AAG4tG_inVamsAOqbiaXhMLAc92RI_NNtmQ"
    OWNER_ID = "1453690249"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "AidanNia"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://nqfytkniogdnux:e71df9255f09444f19d0fd41dbf79493de7697bb9d8f2a88eedecaaa988cf679@ec2-3-216-129-140.compute-1.amazonaws.com:5432/d5bb7cqvnjbrr'  # needed for any database modules
    MESSAGE_DUMP = -1001435803865  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation', 'rss', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1453690249]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [1453690249]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [1453690249]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = ''  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
