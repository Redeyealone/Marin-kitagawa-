# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 24683098 # Get this value from my.telegram.org/apps
    API_HASH = "e4055cd239464e50e69bd73057c05dd3"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://oaykvtmj:bsIGPV7wmId1x1CNH9eqxQVX5t25cHI3@manny.db.elephantsql.com/oaykvtmj"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002074034670
    MESSAGE_DUMP = -1002105665930

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://herobh123456:hasnainkk07@hasnainkk07.uqjekii.mongodb.net/?retryWrites=true&w=majority"
    # Support chat and support ID
    SUPPORT_CHAT = "ANIME_NETWORK07"
    SUPPORT_ID = -1002074034670

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "6798827644:AAFrnnRyY2FMBeRVLr3BepDvycrhFKrxZos"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 6346273488
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
