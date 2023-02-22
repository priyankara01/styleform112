from django.shortcuts import render
from .forms import StudentForm
# Create your views here.


def student_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            r = form.cleaned_data.get('roll')
            n = form.cleaned_data.get('name')
            print(r, n)
    template_name = 'app1/student.html'
    context = {'form': form}
    return render(request, template_name, context)



