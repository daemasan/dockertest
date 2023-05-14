from config.settings import *
print('開発環境')
env.read_env(env_file)
DEBUG = True
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = ["*"]
#DATABASES = {"default": env.db()}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER': 'root',
        'PASSWORD': '1381023a',# 未設定の場合は、ブランクにする
        'HOST': 'localhost',# 明示的に設定する場合に記述する
        'PORT': '3306',# 明示的に設定する場合に記述する
    }
}