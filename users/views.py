from django.shortcuts import render
from .models import User


def Users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/users.html', context)

def UserSingle(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'users/user.html', context)

# def my_view(request):
#     if not request.user.is_authenticated:
#         return render(request, "myapp/login_error.html")