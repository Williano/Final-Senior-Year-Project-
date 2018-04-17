from django.core.exceptions import PermissionDenied

class EditOwnProfileMixin():
    def get_object(self, *args, **kwargs):
        obj = super(EditOwnProfileMixin, self).get_object(*args, **kwargs)
        self.check_permission(obj)
        return obj
    def check_permission(self, obj):
        if hasattr(obj, 'user'):
            obj = obj.user
            if obj == self.request.user:
                return
            else:
                raise PermissionDenied()

class EditOwnLoginMixin():
    def get_object(self, *args, **kwargs):
        obj = super(EditOwnLoginMixin, self).get_object(*args, **kwargs)
        if obj.email == self.request.user.email:
            return obj
        else:
            raise PermissionDenied

