from django.db import models
from main.models import Profile
# Create your models here.

class ProblemManager(models.Manager):

    def createProblem(self, title, desc, constraint, input_desc, output_desc, sample_input, sample_output):
        problem = Problem(
            title = title, 
            description = desc, 
            constraint = constraint, 
            input_desc= input_desc, 
            output_desc = output_desc,
            sample_input = sample_input,
            sample_output= sample_output
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

    objects = ProblemManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'description'], name='problem_identity')
        ]
    
    def __str__(self):
        return self.title