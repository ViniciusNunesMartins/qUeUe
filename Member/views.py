from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Queue.models import Queue
from .models import Member
from .forms import MemberForm


def member_index(request):
    try:
        if Member.objects.get(session=request.COOKIES.get('sessionid')):
            return redirect('member_queue')
    except:
        return render(request, 'member_index.html', {
            "form": MemberForm({
                "session": request.COOKIES.get('sessionid')
            })
        })


def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            request.session = session.session
            session.save()
            return redirect('member_queue')
    else:
        return redirect('member_index')



def member_queue(request):
    p = Member.objects.get(session=request.COOKIES.get('sessionid'))
    print(p)
    return render(request, 'member_queue.html', {
        "position": p
    })


def member_exit(request):
    Member.objects.get(session=request.COOKIES.get('sessionid')).delete()
    return redirect('member_index')