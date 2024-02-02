from django.db import models


#Implement a way of storing works associated with this author specifically
class Author(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    bio = models.TextField()

    def getName(self):
        return self.name

    def getBio(self):
        return self.bio

    def __str__(self):
        return self.getName()

#Implement a way to get other books in series if there are any
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author.getName()

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price
    def setPrice(self, new):
        self.price = new

    def __str__(self):
        return self.getTitle()

