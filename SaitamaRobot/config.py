from SaitamaRobot.sample_config import Config

class Development(Config):
    OWNER_ID = 1131653685  # your telegram ID
    OWNER_USERNAME = "kavinduaj"  # your telegram username
    API_KEY = "1428003210:AAGaq_PphUbLpNof_f5_2Cks16AORUEnpag"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://kaj12:dkkajcmd@0951357@postgresql/postgres'  # sample db credentials
    JOIN_LOGGER = '-1001329348574' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [1131653685]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    ALLOW_CHATS = [1131653685]
    AI_API_KEY = "1a07c3a5bff02e4cc38b0ff89fcb05fc4b1675f357844ee0b2604e9d7d9769ba27efb72057e4759cd4dd4118959fb02089f641d7bb06c1532698c48789bd8250"
    TIME_API_KEY = "R5GZ4QBTQAEE"
