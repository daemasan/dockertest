from config.settings import *
print('ドッカー環境')
env.read_env(env_file)
DEBUG = True
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]
#DATABASES = {"default": env.db()}
DATABASES  = {"default": env.db()}