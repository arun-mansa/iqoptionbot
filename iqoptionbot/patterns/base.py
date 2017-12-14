"""Module for IQ Option API base pattern."""
import time


class Base(object):
    """Class for IQ Option API base pattern."""

    def __init__(self, api, active):
        """
        :param api: The instance of
            :class:`IQOptionAPI <iqoptionapi.api.IQOptionAPI>`.
        """
        self.api = api
        self.active = active

    @property
    def candles(self):
        """Property to get candles."""
        if self.api.timesync.server_datetime.second == 0:
            self.api.getcandles(self.active, 60)
            time.sleep(0.5)
            return self.api.candles

    def call(self):
        """Method to check call pattern."""
        pass

    def put(self):
        """Method to check put pattern."""
        pass
