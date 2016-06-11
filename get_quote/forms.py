from django.forms import ModelForm
from .models import GetQuote

class QuoteForm(ModelForm):
    class Meta:
        model = GetQuote
        fields = '__all__'
