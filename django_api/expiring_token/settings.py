from datetime import timedelta

from django.conf import settings


class CustomSettings(object):

    @property
    def EXPIRING_TOKEN_DURATION(self):
        try:
            val = settings.EXPIRING_TOKEN_DURATION
        except AttributeError:
            val = timedelta(hours=12)

        return val


custom_settings = CustomSettings()
