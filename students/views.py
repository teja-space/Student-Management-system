from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})


def edit(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()
        return redirect('index')

    return render(request, 'edit.html', {'student': student})


def delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('index')