# coding:utf-8
# life is short, you need Python！
from .models import CustomUser

class EmailBackend(object):
    def authenticate(self, request, **credentials):

        email = credentials.get('email', credentials.get('username'))
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        """

        """
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
