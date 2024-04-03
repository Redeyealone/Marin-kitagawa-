# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = "27389764"  # Get this value from my.telegram.org/apps
    API_HASH = "75ecb2e1879c9e805c5aa934a5ff4b5f"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://fodrfyzd:fozO611cVktRfkPLfRb1S52saC6AsKAe@castor.db.elephantsql.com/fodrfyzd"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = "-1001991974760"
    MESSAGE_DUMP = "-1001991974760"

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Nonalcoholic:8eVPSTcJa2c3FkH@cluster0.bprf1b2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "fubuki_supports"
    SUPPORT_ID = "-1001991974760"

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7092177721:AAFRm41i2XVcBbO5ski4VQYtZbvORmoI_qU"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = "6083498673"
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
