from django import forms
from .models import Problem
'''
fields - 
title, description, constraint, input_desc, output_desc, sample_input, sample_output, category
'''

CATEGORIES = [
    ('basic','Basics'),('math','Mathematics'),
    ('ds','Data Structures'),('greedy','Greedy Algorithms'),
    ('dp','Dynamic Programming'),('graph','Graph Theory')
]
class CreateProblemForm(forms.Form):

    title= forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Not more than 200 words'}), label = 'Enter Problem Title')
    description= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Describe the problem'}), label = 'Description')
    constraint= forms.CharField(required= False, widget = forms.TextInput(attrs={'placeholder':'e.g. 1<=N<=100'}), label = 'Constraints')
    input_desc= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Describe how the input will be'}), label = 'Input Description')
    output_desc= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Describe how the output will be'}), label = 'Output Description')
    sample_input= forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder':'Give a sample input', 'rows':5}), label='Sample Input')
    sample_output= forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Give a sample output', 'rows':5}), label='Sample Output')
    category= forms.CharField(widget=forms.Select(choices=CATEGORIES), label='Category')