from django.db import models

class AccountUser(models.Model):
    uid = models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField(default=None,blank=True,null=True)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    img=models.ImageField(upload_to='images',default=None,blank=True,null=True)
    work=models.CharField(max_length=500,default=None,blank=True,null=True)
    qualification=models.CharField(max_length=200,default=None,blank=True,null=True)
    currentTown = models.CharField(max_length=50, default=None,blank=True,null=True)
    HomeTown = models.CharField(max_length=50, default=None,blank=True,null=True)
    friend=models.IntegerField(default=0,blank=True,null=True)
    relationship=models.CharField(max_length=50, default=None,blank=True,null=True)
    otp=models.IntegerField(default=None,blank=True,null=True)
    def __str__(self):
        return self.firstname + " " + self.surname + " " + self.username

class Post(models.Model):
    pid=models.AutoField(primary_key=True)
    user=models.ForeignKey(AccountUser,on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='images',default=None,blank=True,null=True)
    content=models.TextField()
    dt=models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='images', default=None, blank=True, null=True)

    def __str__(self):
        return str(self.pid) + " " + self.user.firstname

class Like(models.Model):
    lid=models.AutoField(primary_key =True)
    post=models.OneToOneField(Post,on_delete=models.CASCADE,default=None,blank=True,null=True)
    user=models.ManyToManyField(AccountUser,default=None,blank=True)
    counter=models.IntegerField(default=0)



