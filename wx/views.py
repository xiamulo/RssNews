from django.shortcuts import render, redirect, HttpResponse, reverse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from wx.models import wx, label,kuan,liqu,wb
# Create your views here.
import datetime
import json
def index(request):
    if request.session.get('is_login', None):
        # return HttpResponse(request.session['username'])
        return render(request, 'home.html')
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login" % current_namespace))
    pass
def kaarticle(request):
    if request.session.get('is_login', None):
        now_time = datetime.datetime.now()
        times=datetime.datetime.now().strftime('%Y-%m-%d')
        labellist = label.objects.filter(type="2")
        labellist = list(labellist)
        labelName = request.GET.get("labelName");
        begin = request.GET.get("begin");
        end = request.GET.get("end");
        current = request.GET.get("current");
        if labelName == None or labelName == "":
            labelName = "酷安"
        if current == None or current == "":
            current = "1"

        if begin == None and end == None:
            begin = "0"
            end = "50"
        else:
            begin = str((int(begin) - 1) * int(end));
        if  labelName == "酷安":
            kaList = kuan.objects(creattime____contains=times).skip(int(begin)).limit(int(end))
            total = kaList.count()
        else:
            kaList = liqu.objects(creattime____contains=times).skip(int(begin)).limit(int(end))
            total = kaList.count()

        context = {'labellist': labellist, "wxList": list(kaList), "total": total, "current": current,
                   "labelName": labelName}
        return render(request, 'kaarticle.html', context=context)
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login" % current_namespace))


def wxarticle(request):
    if request.session.get('is_login', None):
        now_time = datetime.datetime.now()
        times = datetime.datetime.now().strftime('%Y-%m-%d')
        # return HttpResponse(request.session['username'])
        labellist = label.objects.filter(type="1")
        labellist = list(labellist)
        redis_Name= request.GET.get("redis_Name");
        begin = request.GET.get("begin");
        end = request.GET.get("end");
        current = request.GET.get("current");
        if redis_Name == None or redis_Name == "":
            redis_Name = "wx_app_keyword"
        if current == None or current == "":
            current = "1"

        if begin == None and end == None:
            begin = "0"
            end = "100"
        else:
            begin = str((int(begin) - 1) * int(end));
        #wxList = wx.objects()
        wxList = wx.objects(redis_db=redis_Name,nowtime____contains=times).order_by("-nowtime").skip(int(begin)).limit(int(end))
        total = wxList.count()
        context = {'labellist': labellist, "wxList": list(wxList), "total": total, "current": current,
                   "redis_Name": redis_Name}
        return render(request, 'wxarticle.html', context=context)
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login" % current_namespace))

def wbarticle(request):
    if request.session.get('is_login', None):
        now_time = datetime.datetime.now()
        times = datetime.datetime.now().strftime('%Y-%m-%d')
        # return HttpResponse(request.session['username'])
        labellist = label.objects.filter(type="3")
        labellist = list(labellist)
        labelName = request.GET.get("labelName");
        keywords = request.GET.get("keywords");
        begin = request.GET.get("begin");
        end = request.GET.get("end");
        current = request.GET.get("current");
        if labelName == None or labelName == "":
            labelName = "政法类微博"
        if current == None or current == "":
            current = "1"

        if begin == None and end == None:
            begin = "0"
            end = "100"
        else:
            begin = str((int(begin) - 1) * int(end));

        if keywords!=None:
            wbList = wb.objects(name____contains=keywords).order_by("-pubish_time").skip(int(begin)).limit(int(end))
        else:
            wbList = wb.objects().order_by("-pubish_time").skip(int(begin)).limit(int(end))
        total = wbList.count()
        context = {'labellist': labellist, "wxList": list(wbList), "total": total, "current": current,
                   "labelName": labelName}
        return render(request, 'wbarticle.html', context=context)
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
            ret["flag"] = True
        else:
            ret["error_msg"] = "用户名和密码错误"
        return HttpResponse(json.dumps(ret, ensure_ascii=False))
