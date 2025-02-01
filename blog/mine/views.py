from django.shortcuts import render
from .models import ChaiVarity, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all() #returns array
    return render(request, 'mine/all_mine.html', {'chais': chais})

# def order(request):
#     return render(request, 'chai/order.html')
def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'mine/chai_detail.html', {'chai': chai})

def chai_stores(request):
    stores = None
    # when user submits the form
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_varity)
    else:
        form = ChaiVarityForm()
    return render(request, 'mine/chai_stores.html', {'stores': stores, 'form': form})
