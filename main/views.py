from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone #to record current-time
from .models import Todo

# Create your views here.

def index(request):
    todo_items =Todo.objects.all().order_by("added_date")
    return render(request, 'main/index.html',{"todo_items": todo_items})


def add_todo(request):

    content_to_add= request.POST['content']  #get from form with name content
    if content_to_add.replace(" ","") != "":
        current_date = timezone.now() #to get time
        created_obj = Todo.objects.create(added_date=current_date, text=content_to_add)
    return HttpResponseRedirect("/")

def delete_todo(request,todo_id):
    try:
        if Todo.objects.all().count() >0:
            Todo.objects.get(id=todo_id).delete()
        return HttpResponseRedirect("/")
    except:
        return HttpResponseRedirect("/")