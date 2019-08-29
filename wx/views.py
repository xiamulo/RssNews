from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from wx.models import sites, label
# Create your views here.
import json
def index(request):
    if request.session.get('is_login', None):
        # return HttpResponse(request.session['username'])
        return render(request, 'home.html')
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login" % current_namespace))
    pass


def wxarticle(request):
    if request.session.get('is_login', None):
        # return HttpResponse(request.session['username'])
        labellist = label.objects.filter(type="1")
        labellist = list(labellist)
        labelName = request.GET.get("labelName");
        begin = request.GET.get("begin");
        end = request.GET.get("end");
        current = request.GET.get("current");
        if labelName == None or labelName == "":
            labelName = "app 提现"
        if current == None or current == "":
            current = "1"

        if begin == None and end == None:
            begin = "0"
            end = "100"
        else:
            begin = str((int(begin) - 1) * int(end));
        wxList = sites.objects(key=labelName).skip(int(begin)).limit(int(end))
        total = wxList.count()
        context = {'labellist': labellist, "wxList": list(wxList), "total": total, "current": current,
                   "labelName": labelName}
        return render(request, 'wxarticle.html', context=context)
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login" % current_namespace))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
        pass

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ret = {"flag": False, "error_msg": None}
        if username == 'admin' and password == '1342751882':
            request.session['username'] = username
            request.session['is_login'] = True
            request.session.set_expiry(0)
            current_namespace = request.resolver_match.namespace
            ret["flag"] = True
        else:
            ret["error_msg"] = "用户名和密码错误"
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
