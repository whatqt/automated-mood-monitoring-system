def insert_user_pk(func):
    def wraper(self, *args, **kwargs):
        request = args[0]
        request.data["username"] = request.user.pk
        return func(self, request)
    return wraper