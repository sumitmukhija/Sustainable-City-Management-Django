import pusher
from SCMBackend.env import Environ

class Notifier(object):

    def __init__(self):
        self.pusher_client = pusher.Pusher(app_id=Environ().get_pusher_app_id(), key=Environ().get_pusher_key(),secret=Environ().get_pusher_secret(), cluster='eu',ssl=False)
    
    def dispatch_notification(self, content, event = "notification-event", channel = "notification-channel"):
        if self.pusher_client is not None:
            self.pusher_client.trigger(channel, event, content)
