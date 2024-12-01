# 2
class Customer:
    def __init__(self, ID, Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Dt_Customer, Country, Complain, Successful_Campaigns):
        self.ID = ID
        self.Year_Birth = Year_Birth
        self.Education = Education
        self.Marital_Status = Marital_Status
        self.Income = Income
        self.Kidhome = Kidhome
        self.Teenhome = Teenhome
        self.Dt_Customer = Dt_Customer
        self.Country = Country
        self.Complain = Complain
        self.Successful_Campaigns = Successful_Campaigns
# 3
    def __repr__(self):
        return f"Customer(ID={self.ID}, Year_Birth={self.Year_Birth}, Income={self.Income})"
