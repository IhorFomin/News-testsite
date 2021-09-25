from django.shortcuts import render


def test(request):
    return render(request, 'testapp/test.html')
