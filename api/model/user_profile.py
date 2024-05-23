from model.account_profile import AkunProfileModel

class User(AkunProfileModel):
    def __init__(self):
        AkunProfileModel.__init__(self)
        self.role = "User"



