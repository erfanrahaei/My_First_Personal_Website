from django.core.paginator import(
    Paginator,
    PageNotAnInteger,
    EmptyPage
)
from django.db.models import Q
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from posts.models import Post


def home(request):
    queryset_list=Post.objects.filter(draft=False)


    query=request.GET.get('q',None)
    if query:
        queryset_list=queryset_list.filter(
            Q(title__icontains=query)  |
            Q(content__icontains=query)|
            Q(user__profile_name__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'posts': queryset,
        'lists': queryset_list,
        'page_request_var': page_request_var,
        'page': page,
    }
    template = 'home.html'
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return render(request, template, context)    