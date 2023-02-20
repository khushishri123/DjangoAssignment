from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Department,Employee

# Create your views here.
def index(request):
    data = Department.objects.all().values()
    emp = Employee.objects.all().values()
    return HttpResponse(render(request, 'index.html', {'depts': zip(data, emp)}))


def add(request):
    return render(request,'add.html')


@csrf_exempt
def save(request):
    dept_id = request.POST.get("dept_id")
    name = request.POST.get("name")
    managername = request.POST.get("manager")
    e = Employee(name=managername)
    dept = Department(dept_id=dept_id, name=name, manager=e)
    e.save()
    dept.save()
    return HttpResponse("Department added successfully")

def update(request,id):
    dept=Department.objects.get(manager_id=id)
    emp=Employee.objects.get(id=id)
    return render(request,'update.html',{'dept':dept,'emp':emp})

def edit(request,id):
    dept=Department.objects.get(manager_id=id)
    emp=Employee.objects.get(id=id)
    dept_id=request.POST.get('dept_id')
    dept_name=request.POST.get('name')
    manager=request.POST.get('manager')
    dept.dept_id=dept_id
    dept.name=dept_name
    emp.name=manager
    dept.manager=emp
    emp.save()
    dept.save()
    depts=Department.objects.all().values()
    emps=Employee.objects.all().values()
    return render(request,"index.html",{'depts': zip(depts, emps)})


def delete(request,id):
    dept=Department.objects.get(manager_id=id)
    emp=Employee.objects.get(id=id)
    dept.delete()
    emp.delete()
    d=Department.objects.all().values()
    e=Employee.objects.all().values()
    return render(request,'index.html',{'depts':zip(d,e)})
