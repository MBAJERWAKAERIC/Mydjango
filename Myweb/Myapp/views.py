from .models import Student
def student_show(request):
student = Student.objects.order_by('roll_no')
return render(request, 'template/index.html', {'student': student})
