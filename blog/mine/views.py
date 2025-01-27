from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request, 'mine/all_mine.html')
# def order(request):
#     return render(request, 'chai/order.html')
