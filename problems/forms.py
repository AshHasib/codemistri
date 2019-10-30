from django import forms
from .models import Problem
'''
fields - 
title, description, constraint, input_desc, output_desc, sample_input, sample_output, category
'''

CATEGORIES = [
    ('Basics','Basics'),('Mathematics','Mathematics'),
    ('Data Structures','Data Structures'),('Greedy Algorithms','Greedy Algorithms'),
    ('Dynamic Programming','Dynamic Programming'),('Graph Theory','Graph Theory')
]

DIFFICULTY =[
    ('Easy','Easy'),
    ('Medium', 'Medium'),
    ('Hard','Hard')
]
class CreateProblemForm(forms.Form):

    title= forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Not more than 200 words'}), label = 'Enter Problem Title')
    description= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Describe the problem'}), label = 'Description')
    constraint= forms.CharField(required= False, widget = forms.TextInput(attrs={'placeholder':'e.g. 1<=N<=100'}), label = 'Constraints')
    input_desc= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Describe how the input will be', 'rows':5}), label = 'Input Description')
    output_desc= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Describe how the output will be', 'rows':5}), label = 'Output Description')
    sample_input= forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder':'Give a sample input', 'rows':5}), label='Sample Input')
    sample_output= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Give a sample output', 'rows':5}), label='Sample Output')
    category= forms.CharField(widget=forms.Select(choices=CATEGORIES), label='Category')
    difficulty= forms.CharField(widget=forms.Select(choices=DIFFICULTY), label='Difficulty')
