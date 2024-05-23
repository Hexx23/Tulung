from model.account_profile import AkunProfileModel

class Admin(AkunProfileModel):
    def __init__(self):
        AkunProfileModel.__init__(self)
        self.role = "Admin"
    

