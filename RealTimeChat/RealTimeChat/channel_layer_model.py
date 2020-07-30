from channels.layers import BaseChannelLayer

class CustomChannelLayer(BaseChannelLayer):

    def __init__(self, expiry=60, capacity=1000, channel_capacity=None):
        self.expiry = expiry
        self.capacity = capacity
        self.channel_capacity = channel_capacity or {}
        self.groups={}
        self.channels={}
        



