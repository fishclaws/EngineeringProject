
class ConcurrentModificationError(Exception):
    def __init__(self, message, *args):
        self.message = message
        super(ConcurrentModificationError, self).__init__(message, *args)
