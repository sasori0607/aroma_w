from django.shortcuts import render


def home(reqest):

    return render(reqest, 'content/index.html')


def about(reqest):

    return render(reqest, 'content/about.html')

def delivery(reqest):

    return render(reqest, 'content/delivery.html')


def returns(reqest):

    return render(reqest, 'content/returns.html')
