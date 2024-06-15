from django.forms import ModelForm

from blog.models import Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fields in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'photo')


class BlogContentManagerForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'is_published')
