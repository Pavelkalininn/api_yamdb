from django.contrib.auth.backends import ModelBackend, UserModel


class AuthenticationWithoutPassword(ModelBackend):

    def authenticate(self, request, username=None):
        if username is None:
            username = request.data.get('username', '')
        try:
            return UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
