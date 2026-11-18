from django.shortcuts import render, redirect

# Create your views here.
from hr_department.form import EmployeeForm
def new_employee(request):
            form = EmployeeForm()
            if request.method == 'POST':
                form = EmployeeForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('home')  
            
            return render(request, 'hr_tem/emp_form.html', {'form': form})
