
class User_Info(models.Model):
    User_id = models.IntegerField(primary_key=True)
    User_name =models.CharField(max_length=20)
   
class Expense_Category(models.Model):
    Breakfast = models.IntegerField(max_length=15)
    Trip = models.IntegerField(max_length=15)
    Hangout = models.IntegerField(max_length=15)
    User_name = models.ForeignKey(User_Info, on_delete=models.CASCADE)
