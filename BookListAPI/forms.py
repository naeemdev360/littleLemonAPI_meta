from django.forms import ModelForm
from .models import BookListModel

class AddBookForm(ModelForm):
    class Meta:
        model = BookListModel
        fields = "__all__"