from django.db import models
from django.urls import reverse 


class Commission(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField() 
    people_required = models.IntegerField() 
    created_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,auto_now_add=False)
    
    class Meta: 
        ordering = ['created_on'] 

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self): 
        return reverse('commissions:commission-detail', args=[self.pk])


class Comment(models.Model): 
    commission = models.ForeignKey(Commission,
                                   on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta: 
        ordering = ['-created_on']

    def __str__(self): 
        return self.entry