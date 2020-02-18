from rest_framework import permissions
from mongo_auth.utils import login_status


class AppPermissions(permissions.BasePermission):

    def has_permits(self, request, view, key):
        try:
            flag, user_obj = login_status(request)
            request.user = None
            if flag and user_obj['permits'][key]:
                request.user = user_obj
                return True
            else:
                return False
        except Exception as e:
            return False


class BikeAuth(AppPermissions):

    def has_permission(self, request, view):
        return super().has_permits(request, view, 'bike')


class BusAuth(AppPermissions):

    def has_permission(self, request, view):
        return super().has_permits(request, view, 'bus')


class LuasAuth(AppPermissions):

    def has_permission(self, request, view):
        return super().has_permits(request, view, 'luas')


class DartAuth(AppPermissions):

    def has_permission(self, request, view):
        return super().has_permits(request, view, 'dart')
