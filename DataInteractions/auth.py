from rest_framework import permissions
from mongo_auth.utils import login_status


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


class BikeAuth(permissions.BasePermission):

    def has_permission(self, request, view):
        return has_permits(self, request, view, 'bike')


class BusAuth(permissions.BasePermission):

    def has_permission(self, request, view):
        return has_permits(self, request, view, 'bus')


class LuasAuth(permissions.BasePermission):

    def has_permission(self, request, view):
        return has_permits(self, request, view, 'luas')


class DartAuth(permissions.BasePermission):

    def has_permission(self, request, view):
        return has_permits(self, request, view, 'dart')
