from django.db import models
from USER.models import User

# Create your models here.

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # project titles, tech stacks, descriptions, social links
    title=models.CharField(max_length=100)
    tech_stack=models.CharField(max_length=100)
    description=models.TextField()
    social_link=models.URLField()
    intrests=models.TextField()
    education = models.ManyToManyField('Portfolio.Education', related_name='portfolios')
    projects = models.ManyToManyField('Portfolio.Projects', related_name='portfolios')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'


class Education(models.Model):
    user = models.ForeignKey('USER.User', on_delete=models.CASCADE) 
    college = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    cgpa = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        unique_together = ('user', 'degree')

class Projects(models.Model):
    user = models.ForeignKey('USER.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=100)
    description = models.TextField()
    project_link = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title   

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        unique_together = ('user', 'title')
