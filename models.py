
class UserInfo(models.Model):
    Userid = models.IntegerField(primary_key=True)
    Username =models.CharField(max_length=20)
   
class ExpenseCategory(models.Model):
    Breakfast = models.IntegerField(max_length=15)
    Trip = models.IntegerField(max_length=15)
    Hangout = models.IntegerField(max_length=15)
    Username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
