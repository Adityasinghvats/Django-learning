from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all() #returns array
    return render(request, 'mine/all_mine.html', {'chais': chais})

# def order(request):
#     return render(request, 'chai/order.html')
def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'mine/chai_detail.html', {'chai': chai})
