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
