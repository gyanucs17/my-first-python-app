from django import forms
#from flask import Flask, render_template, request, redirect
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)