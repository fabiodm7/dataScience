from django import forms

from .models import BlogPost

class BlogPostEntry(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        labels = {'title':'Título','text':'História'}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}