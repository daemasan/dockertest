from config.settings import *
import io
import google.auth
from urllib.parse import urlparse
from google.cloud import secretmanager

DEBUG = True
# Attempt to load the Project ID into the environment, safely failing on error.
_, os.environ["GOOGLE_CLOUD_PROJECT"] = google.auth.default()

# Pull secrets from Secret Manager
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
client = secretmanager.SecretManagerServiceClient()
settings_name = os.environ.get("SETTINGS_NAME", "secret")
name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")
env.read_env(io.StringIO(payload))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!

CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
if CLOUDRUN_SERVICE_URL:
    ALLOWED_HOSTS = [urlparse(CLOUDRUN_SERVICE_URL).netloc]
    CSRF_TRUSTED_ORIGINS = [CLOUDRUN_SERVICE_URL]
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
else:
    ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#HOSTはdocker-compose使う場合はサービス名を記述
DATABASES = {"default": env.db()}

#staticファイル環境に寄って変える必要あり
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_DEFAULT_ACL = "publicRead"
