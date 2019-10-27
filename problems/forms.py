from django import forms


class ProblemForm(forms.Form):
    title = forms.CharField(max_length = 100, label ='Problem Title', widget = forms.TextInput(
        attrs={
            'placeholder':'Not more than 100 words'
        }
    ))
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={
            'placeholder':'Describe the problem'
        }
    ))
    constraint = forms.CharField(required= False, max_length = 100, label ='Constraints', widget = forms.Textarea(
        attrs={
            'placeholder':'e.g. 1<=N<=100',
            'rows':2
        }
    ))

    input_desc = forms.CharField(label = 'Input Description', widget = forms.Textarea(
        attrs={
            'placeholder':'Describe the input format',
            'rows':4
        }
    ))

    output_desc = forms.CharField(label = 'Output Description', widget = forms.Textarea(
        attrs={
            'placeholder':'Describe the output format',
            'rows':4
        }
    ))

    sample_input = forms.CharField(required=False, label = 'Sample Input', widget = forms.Textarea(
        attrs={
            'placeholder':'Sample Input',
            'rows':5,
            'cols':6
        }
    ))

    sample_output = forms.CharField(label = 'Sample Input', widget = forms.Textarea(
        attrs={
            'placeholder':'Sample Output',
            'rows':5,
            'cols':6
        }
    ))

