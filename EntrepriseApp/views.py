from django.shortcuts import redirect, render

from EntrepriseApp.forms import RegisterUserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})