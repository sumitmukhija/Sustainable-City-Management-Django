import pusher
from SCMBackend.env import Environ
from SCMBackend.singleton import singleton

@singleton
class Notifier(object):
    """Singleton class to dispatch a notification using Pusher
    """

    def __init__(self):
        """Creates a pusher client with environment variables
        """
        self.pusher_client = pusher.Pusher(app_id=Environ().get_pusher_app_id(), key=Environ().get_pusher_key(),secret=Environ().get_pusher_secret(), cluster='eu',ssl=False)
    
    def dispatch_notification(self, content, event="notification-event", channel="notification-channel"):
        """Method to dispatch notification.
        
        Arguments:
            content string -- Text content of the notification
            event -- event to be pushed. Defaults to notification-event. Can be managed 
            in Pusher dashboard.
            channel -- channel to be pushed to. Defaults to notification-channel. Can be managed 
            in Pusher dashboard.
        
        Keyword Arguments:
            event {str} -- [description] (default: {"notification-event"})
            channel {str} -- [description] (default: {"notification-channel"})
        """
        if self.pusher_client is not None:
            self.pusher_client.trigger(channel, event, content)
