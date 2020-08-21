from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import TalkingsOn
from homepage.forms import ConvoForm

import string
import random
# Create your views here.


def index(request):
    roastboast = TalkingsOn.objects.all().order_by('post_date')
    return render(request, "index.html", {"roastboast": roastboast})


def make_post_view(request):
    if request.method == "POST":
        form = ConvoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # secretkey = "".join(random.choices(string.ascii_letters + string.digits, key=6))
            TalkingsOn.objects.create(
                choices=data.get('choices'),
                body=data.get('body'),
                # s_key=secretekey
            )
            # return render(request, "sorted_by_vote.html", {"post": votes})
            return HttpResponseRedirect(reverse('homepage'))

    form = ConvoForm()
    return render(request, "basic_form.html", {"form": form})


# code by Sohail Aslam during study hall
def sorted_by_vote_view(request):
    posts = TalkingsOn.objects.all()
    posts = list(posts)
    posts = sorted(posts, key=lambda x: x.votes, reverse=True)
    return render(request, "sorted_by_vote.html", {"votes": posts})


def roast_view(request):
    roast = TalkingsOn.objects.all().order_by('post_date')
    return render(request, "roast.html", {"posts": roast})


def boast_view(request):
    boast = TalkingsOn.objects.all().order_by('post_date')
    return render(request, "boast.html", {"posts": boast})


def up_vote_view(request, up_vote_id):
    post = TalkingsOn.objects.filter(id=up_vote_id).first()
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def down_vote_view(request, down_vote_id):
    post = TalkingsOn.objects.filter(id=down_vote_id).first()
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def delete_post_view(request, post_id):
#     return redirect('/')
