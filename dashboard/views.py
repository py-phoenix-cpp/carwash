from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def DriversView(request):
    return render(request, 'drivers.html')

def asasd(request):
    return render(request, 'index.html')

def Account_setting(request):
    return render(request, 'index.html')


def test():
    discond = Discond.objects.create(
        all_sum = 200,
        quantity = 2
    )
    client = Client.objects.get(id=2)
    cliend.price += discond.all_sum
    cliend.quantiy += discond.quantity
    cliend.save()
