from django.apps import AppConfig
import boto3
import tensorflow_hub as hub

# %USERPROFILE%\AppData\roaming\Python\Python38\Scripts
class NstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nstapp'
    # magenta 모델 불러오기
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
