from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from apps.user.models import UserProfile
# Create your views here.


def bank(request):
    if request.user.id:
        userProfile = UserProfile.objects.get(user_id=request.user.id)
        user_obj = UserProfile.objects.order_by("-deposit")
        return render(request, "bank.html", {'user_obj': user_obj, 'userProfile': userProfile})
    else:
        return HttpResponse("请登录后再进入银行操作")


def deposit(request):
    method = request.method
    if method == "POST":
        if request.user.id:
            author = UserProfile.objects.get(user__username=request.user.username)
            deposit_amount = request.POST.get("deposit_amount")
            # 欲存款数量 < 当前金币则返回成功
            if int(deposit_amount) <= author.coin:
                UserProfile.objects.filter(user=request.user).update(coin=author.coin-int(deposit_amount))
                UserProfile.objects.filter(user=request.user).update(deposit=author.deposit+int(deposit_amount))
                return HttpResponse(str(deposit_amount) + "金币\n存款成功!")
            else:
                return HttpResponse("当前"+str(author.coin)+"金币不足存款!")
        else:
            return HttpResponse("Bad request")
    else:
        return HttpResponse("Bad request")


def withdraw(request):
    method = request.method
    if method == "POST":
        if request.user.id:
            author = UserProfile.objects.get(user__username=request.user.username)
            withdraw_amount = request.POST.get("withdraw_amount")
            # 存款 < 取款金额
            if author.deposit < int(withdraw_amount):
                return HttpResponse("取款金额大于当前存款数!")
            else:
                UserProfile.objects.filter(user=request.user).update(deposit=author.deposit - int(withdraw_amount))
                UserProfile.objects.filter(user=request.user).update(coin=author.coin + int(withdraw_amount))
                return HttpResponse(str(withdraw_amount) + "金币\n取款成功!")
        else:
            return HttpResponse("Bad request")
    else:
        return HttpResponse("Bad request")


def transfer(request):
    method = request.method
    if method == "POST":
        if request.user.id:
            author = UserProfile.objects.get(user__username=request.user.username)
            transfer_to = request.POST.get("transfer_to")
            transfer_amount = request.POST.get("transfer_amount")
            if int(transfer_amount) > author.deposit:
                return HttpResponse("当前存款不足转账!")
            else:
                user_to = User.objects.get(username=transfer_to)
                if user_to:
                    user_to_profile = UserProfile.objects.get(user=user_to)
                    UserProfile.objects.filter(user=user_to).update(deposit=user_to_profile.deposit+int(transfer_amount))
                    UserProfile.objects.filter(user=request.user).update(deposit=author.deposit - int(transfer_amount))
                    return HttpResponse("转账成功!")
                else:
                    return HttpResponse(transfer_to + "用户不存在!")
        else:
            return HttpResponse("Bad request")
    else:
        return HttpResponse("Bad request")
