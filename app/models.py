from django.db import models

class Me(models.Model):
    image=models.ImageField(upload_to='My_images')
    name_surname=models.CharField(max_length=200)
    phone = models.IntegerField(max_length=13)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    year=models.DateField()
    about_me=models.TextField()
    def __str__(self):
        return f"{self.name_surname} | {self.year}"
    class Meta:
        verbose_name = 'Me'
        verbose_name_plural = "We"

class Statistic(models.Model):
    name=models.CharField(max_length=200)
    count=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.name} | {self.count}"
    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = "Statistics"


class Portfolio(models.Model):
    image=models.ImageField(upload_to="portfolio_images")
    name=models.CharField(max_length=200)
    about=models.TextField()
    def __str__(self):
        return f"{self.name} "
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = "Portfolios"



class Social(models.Model):
    name=models.CharField(max_length=200)
    link=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name} | {self.link}"
    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = "Socials"
    







    