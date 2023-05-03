from django.shortcuts import render

from django.http import HttpResponse
def main(request):
    return render(request, "index.html")
def contact(request):
    return render("Контакты")
def about(request):
    return render("O Caйтe")