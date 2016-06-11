from django.shortcuts import render
from .forms import QuoteForm
from .models import GetQuote

def index(request):
    dict1 = {}
    if request.method == 'POST':
        f = QuoteForm(request.POST)
        if f.is_valid():
            quoteform = f.save()
            return render(request,'get_quote/success.html', dict1)
    else:
        form = QuoteForm()
        dict1.update({ 'form':form })
        return render(request,'get_quote/index.html', dict1)
