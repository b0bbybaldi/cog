from cogk8s.settings.base import *

DEBUG = True

INSTALLED_APPS += (
                   # other apps for local development
                   minio_storage,
                   )

# Minio server
STATIC_URL = '/static/'
STATIC_ROOT = './static_files/'

DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_ENDPOINT = 'localhost:9000'
MINIO_STORAGE_ACCESS_KEY = 'geobeyond'
MINIO_STORAGE_SECRET_KEY = 'geobeyond'
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'local-media'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'local-static'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True

# These settings should generally not be used:
# MINIO_STORAGE_MEDIA_URL = 'http://localhost:9000/local-media'
# MINIO_STORAGE_STATIC_URL = 'http://localhost:9000/local-static'

# COG
MINIO_STORAGE_COG_BUCKET_NAME = "cog"
MINIO_STORAGE_COG_URL = "http://localhost:9000"
MINIO_STORAGE_AUTO_CREATE_COG_BUCKET = False
MINIO_STORAGE_AUTO_CREATE_COG_POLICY = False
MINIO_STORAGE_COG_USE_PRESIGNED = False
MINIO_STORAGE_COG_BACKUP_FORMAT = False
MINIO_STORAGE_COG_BACKUP_BUCKET = False
