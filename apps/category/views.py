from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect
from django.contrib import auth

from .models import BBS, CatgoryName, Reply
from apps.user.models import UserProfile

# Create your views here.


# def index(request):
#     bbs_list = BBS.objects.filter(category='easy_talk')
#     return render_to_response('forum.html', {'bbs_list': bbs_list, 'user': request.user})


def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponseRedirect("../")


def category(request, cat_id):
    bbs_list = BBS.objects.filter(category=cat_id)
    cat_obj = CatgoryName.objects.get(cat_id=cat_id)
    if request.user.id:
        userProfile = UserProfile.objects.get(user_id=request.user.id)
        return render(request, "category.html", {'bbs_list': bbs_list, 'cat_obj': cat_obj, 'userProfile': userProfile})
    return render(request, "category.html", {'bbs_list': bbs_list, 'cat_obj': cat_obj})


def thread(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    # 更新帖子查看次数
    BBS.objects.filter(id=bbs_id).update(view_count=bbs.view_count+1)
    # 找到该帖子的所有回复以及回复数量
    cat_obj = CatgoryName.objects.get(cat_id=bbs.category)
    reply_obj = Reply.objects.filter(thread_id=bbs_id)
    reply_obj.length = reply_obj.count()
    if request.user.id:
        userProfile = UserProfile.objects.get(user_id=request.user.id)
        return render(request, 'thread.html', {'bbs_obj': bbs, 'reply_obj': reply_obj, 'userProfile': userProfile, 'cat_obj': cat_obj})
    else:
        return render(request, 'thread.html', {'bbs_obj': bbs, 'reply_obj': reply_obj, 'cat_obj':cat_obj})


def post(request, bbs_id):
    method = request.method
    if method == 'GET':
        cat_obj = CatgoryName.objects.get(cat_id=bbs_id)
        if request.user.id:
            userProfile = UserProfile.objects.get(user_id=request.user.id)
            return render(request, "post.html", {'cat_obj': cat_obj, 'userProfile': userProfile})
        else:
            return HttpResponse("请登录后再发帖")
    else:
        title = request.POST.get("title")
        if title == "":
            return HttpResponse("标题不可为空")
        else:
            content = request.POST.get("content")
            author = UserProfile.objects.get(user__username=request.user.username)
            category = request.POST.get("cat_id")
            BBS.objects.create(
                title=title,
                content=content,
                author=author,
                view_count=0,
                category=category
            )
            # 金币+5、发帖数+1
            UserProfile.objects.filter(user=request.user).update(coin=author.coin + 5)
            UserProfile.objects.filter(user=request.user).update(posts=author.posts + 1)
            return HttpResponse("发帖成功\n金币+5")


def reply(request):
    method = request.method
    if method == "POST":
        author = UserProfile.objects.get(user__username=request.user.username)
        # 回复数+1、金币+1
        UserProfile.objects.filter(user=request.user).update(replies=author.replies+1)
        UserProfile.objects.filter(user=request.user).update(coin=author.coin+1)
        # 创建回复
        Reply.objects.create(
            content=request.POST.get("content"),
            author=author,
            thread_id=request.POST.get("thread_id")
        )
        return HttpResponse("回复成功\n金币+1")
    return HttpResponse("Bad request")
