import datetime
#$from datetime import datetime
from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


todos = {
    "monday": "Do Django",
    "tuesday": "Do Python",
    "wednesday": "Do Java"

}


def todo_by_number(request, number):
    day_list = list(todos.keys())
    day_todo = day_list[number - 1]
    redirect_path = reverse("daily-todo", args=[day_todo])
    # return HttpResponseRedirect(f"/my_app{day_todo}")
    return HttpResponseRedirect(redirect_path)


def todo(request, day):
    try:
        return HttpResponse(todos[day])
    except KeyError:
        return HttpResponse("No day found")


def indexes(request):
    return HttpResponse("Hello Godman")


def godman(request):
    return HttpResponse("Hello World")


def index(request):
    return render(request, "Posts/index.html", context={"posts": posts})

def post_detail(request, post_id):
    post = posts[post_id - 1]

    return  render(request, "posts/post-detail.html", {"post": post})


posts = [
        {
             "id": 1,
             "title": "HTML in a nutshell",
             "content": "Smile spoke total few great had never their too. Amongst moments do in arrived at my replied. Fat "
                   "weddings servants but man believed prospect. Companions understood is as especially pianoforte "
                   "connection introduced. Nay newspaper can sportsman are admitting gentleman belonging his. Is "
                   "oppose no he summer lovers twenty in. Not his difficulty boisterous surrounded bed. Seems folly "
                   "if in given scale. Sex contented dependent conveying advantage can use.",
            'date': datetime.datetime.now(),
            'author': "John Wendy"
        },

        {
            "id": 2,
            'title': "Godman Godman",
            'name': "Other People's Money",
            'content': "True Riches for the Kingdom's Child",
            'date': datetime.datetime.now(),
            'author': "Mike Murdock "
        },

        {
            "id": 3,
            "title": "HTML in a nutshell",
            "content": "Smile spoke total few great had never their too. Amongst moments do in arrived at my replied. Fat "
                       "weddings servants but man believed prospect. Companions understood is as especially pianoforte "
                       "connection introduced. Nay newspaper can sportsman are admitting gentleman belonging his. Is "
                       "oppose no he summer lovers twenty in. Not his difficulty boisterous surrounded bed. Seems folly "
                       "if in given scale. Sex contented dependent conveying advantage can use.",
            'date': datetime.datetime.now(),
            'author': "ooooooo"
        },


        {
            "id": 4,
             "title": "CSS in a nutshell",
        "content": "Smile spoke total few great had never their too. Amongst moments do in arrived at my replied. Fat "
                   "weddings servants but man believed prospect. Companions understood is as especially pianoforte "
                   "connection introduced. Nay newspaper can sportsman are admitting gentleman belonging his. Is "
                   "oppose no he summer lovers twenty in. Not his difficulty boisterous surrounded bed. Seems folly "
                   "if in given scale. Sex contented dependent conveying advantage can use.",
            'date': datetime.datetime.now(),
            'author': "0ooooo"
        },

    ]
# def monday(request):
#   return HttpResponse("Do Django")

# def tueday(request):
#   return HttpResponse("Do Java")

# def wednesday(request):
#  return HttpResponse("Do React")
#


# Create your views here.
