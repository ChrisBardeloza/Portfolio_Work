#This is the town class
class town:
    def __init__(self, name, vendor, stash, inn, healer, is_safe_zone):
        self.name=name
        self.vendor=vendor
        self.stash=stash
        self.inn=inn
        self.hearler=healer
        self.is_safe_zone=is_safe_zone