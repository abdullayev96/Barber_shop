from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

###   {"title":"Barber Shop", "url_name":"about"},

# menu = [{"title":"Barber Shop", "url_name":"home"},
#         {"title":"Add page", "url_name":"add_page"},
#         {"title": "contact", "url_name":"contact"},
#         # {"title":"Back go","url_name": "login"},
# ]

def home_page(request):
    return render(request, 'home.html')


def magazine(request):
    posts= Customer.objects.all()
    ctx = {
        'posts':posts,
        "cat_selected": 0,
    }

    return render(request, 'shop.html', ctx)

# def about(request):
#     return render(request, 'about.html', {"menu":menu, 'title':"About title"})


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #try:
#                 # Women.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('shop')
#             # except:
#             #     form.add_error(None, "Error your requested  try again please")
#
#     else:
#         form =  AddPostForm()
#     return render(request, 'addpage.html', {'form':form, "menu": menu, 'title': "About title"})

# def contact(request):
#     return HttpResponse(f"Contact page")


def show_post(request, post_slug):
    post = get_object_or_404(Customer, slug=post_slug)

    ctx = {
        "post": post,
        "title": post.title,
        "cat_selected": post.cat_id,

    }
    return render(request, 'post.html', ctx)


def show_category(request, cat_id):
    posts = Customer.objects.filter(cat_id=cat_id)
    ctx = {
        "posts": posts,
        "title": "Barber shop",
        "cat_selected": cat_id,

    }
    return render(request, 'shop.html', ctx)

