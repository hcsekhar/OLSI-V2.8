from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class category_Db(models.Model):
    ctg_Name = models.CharField(max_length=400)

    def __str__(self):
        return self.ctg_Name
    

class product_Db(models.Model):
    category = models.ForeignKey(category_Db, on_delete=models.CASCADE)
    PRDT_Image = models.ImageField(upload_to='images', null=True)
    PRDT_Title = models.CharField(max_length=1000)
    PRDT_price = models.IntegerField(max_length=100)
    PRDT_Size = models.CharField(max_length=10, null=True,blank='True')
    PRDT_Description = models.TextField(null=True,blank='True')
    PRDT_Usage = models.TextField(null=True,blank='True')
    PRDT_Features = models.TextField(null=True,blank='True')
    PRDT_Benefits = models.TextField(null=True,blank='True')
    
    def __str__(self):
        return self.PRDT_Title

class Product_FAQ(models.Model):
    product = models.ForeignKey(product_Db,on_delete=models.CASCADE)
    PRDT_FAQ_Title = models.CharField(max_length=1000, null=True)
    question = models.CharField(max_length=5000)
    answer = models.TextField(null=True)

    def __str__(self):
        return self.question
    
class Product_feat(models.Model):
    product = models.ForeignKey(product_Db,on_delete=models.CASCADE)
    PRDT_FEAT_Title = models.CharField(max_length=1000, null=True)
    Desc = models.CharField(max_length=5000)

    def __str__(self):
        return self.Desc
    
class Product_usage(models.Model):
    product = models.ForeignKey(product_Db,on_delete=models.CASCADE)
    PRDT_USE_Title = models.CharField(max_length=1000, null=True)
    use = models.CharField(max_length=5000)

    def __str__(self):
        return self.use
    
class Product_dsc(models.Model):
    product = models.ForeignKey(product_Db,on_delete=models.CASCADE)
    PRDT_DSC_Title = models.CharField(max_length=1000, null=True)
    content = models.CharField(max_length=5000)
    def __str__(self):
        return self.content
    

class Trainer(models.Model):
    name = models.CharField(max_length=100,null=True)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
   
    class Meta:
        verbose_name_plural = "Trainer"
        db_table = "Trainer"
    
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
   
    
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Location"
        db_table = "Location"
    
    
class State(models.Model):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
   
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "State"
        db_table = "State"

class Trainer_type(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
   
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Trainer_type"
        db_table = "Trainer_type"

class Session(models.Model):
    name = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    types = models.ForeignKey(Trainer_type, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    address = models.TextField( max_length=10000)
    venue = models.CharField(max_length=500,null=True,blank=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name.name
    
    class Meta:
        verbose_name_plural = "Session"
        db_table = "Session"

    

class Events(models.Model):
    heading  = models.TextField( max_length=10000)
    content = models.CharField(max_length=500,null=True,blank=True)
    
class Gallery(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images', null=True)




class Branch(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Branch"
        db_table = "Branch"

class Branches(models.Model):
    state = models.ForeignKey(Branch, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='state', editable=False, always_update=True)
    District = models.CharField(max_length=150)
    Address = models.TextField(max_length=20000)
    name = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Branches"
        db_table = "Branches"    