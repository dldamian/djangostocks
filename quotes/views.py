from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+ ticker +'/quote?token=pk_1c49f5d82af74a05bf4d2276092e5cee')

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error...'

        return render(request, 'home.html', {'api':api,})


    else:
        return render(request, 'home.html', {'ticker':'Entra algo...',})

    #pk_1c49f5d82af74a05bf4d2276092e5cee
    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_1c49f5d82af74a05bf4d2276092e5cee')



def about(request):
    return render(request, 'about.html', {})

def agregar_stock(request):
    import requests
    import json

    if request.method == 'POST':

        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Agregado a la lista'))
            return redirect('agregar_stock')
        
    else:
        ticker = Stock.objects.all()
        
        salida = []
        for ticker_item in ticker:
            api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+ str(ticker_item) +'/quote?token=pk_1c49f5d82af74a05bf4d2276092e5cee')

            try:
                api = json.loads(api_request.content)
                salida.append(api)
            except Exception as e:
                api = 'Error...'
        
        return render(request, 'agregar_stock.html', {'ticker':ticker,
        'salida':salida})

def eliminar(request, id):
    item = Stock.objects.get(pk=id)
    item.delete()
    messages.success(request, ('Item eliminado correctamente'))
    return redirect('eliminar_stock')


def eliminar_stock(request):
    item = Stock.objects.all()
    return render(request, 'eliminar.html', {'item':item})