from django.db import models
from main.models import Profile
# Create your models here.

class ProblemManager(models.Manager):

    def createProblem(self,**kwargs):
        problem = Problem(
            title = kwargs['title'], 
            description = kwargs['description'], 
            constraint = kwargs['constraint'], 
            category = kwargs['category'],
            input_desc= kwargs['input_desc'], 
            output_desc = kwargs['output_desc'],
            sample_input = kwargs['sample_input'],
            sample_output= kwargs['sample_output']
            )
        return problem


class Problem(models.Model):
    id = models.AutoField(primary_key = True)
    setter = models.ForeignKey(Profile, on_delete= models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    constraint = models.TextField()
    input_desc = models.TextField()
    output_desc = models.TextField()
    sample_input = models.TextField()
    sample_output = models.TextField()
    category = models.CharField(max_length = 100)

    objects = ProblemManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'description'], name='problem_identity')
        ]
    
    def __str__(self):
        return self.title