from .notification import Notification


class SegmentNotification(Notification):
    ALL = "All"

    def __init__(self,
                 included_segments=None,
                 excluded_segments=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.included_segments = included_segments
        self.excluded_segments = excluded_segments

    def get_data(self):
        return {
            "included_segments": self.included_segments,
            "excluded_segments": self.excluded_segments,
            **self.get_parent_data()
        }