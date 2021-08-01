from django.shortcuts import render

def erfan_portfolio_view(request):
    template='erfan_portfolio_info/portfolio.html'
    return render(request,template)
