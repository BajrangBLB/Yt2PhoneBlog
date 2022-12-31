from django import forms
from .models import Post, Category
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

# category_choices = [('Money', 'Money'), ('Knowledge', 'Knowledge'), ('Tech', 'Tech')]
category_set = Category.objects.all().values_list('name','name')
category_choices = [item for item in category_set]

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','header_image','author', 'category', 'body','snippets')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'post_author', 'type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=category_choices, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippets':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body','snippets')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(choices=category_choices, attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippets':forms.Textarea(attrs={'class':'form-control'}),
        }