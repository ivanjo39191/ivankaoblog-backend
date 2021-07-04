from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple, AdminFileWidget
from django.utils.translation import ugettext_lazy as _
# from easy_select2 import Select2
from .models import Blog
class BlogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'types': FilteredSelectMultiple(_('Blog Type'), is_stacked=False),
            'subtypes': FilteredSelectMultiple(_('Blog Type'), is_stacked=False),
            'tags': FilteredSelectMultiple(_('Blog Type'), is_stacked=False),
            # 'subtype': Select2()
        }