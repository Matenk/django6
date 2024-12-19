from django.shortcuts import render, HttpResponse
from .forms import UserRegister


# def sign_up_by_html(request):
#     users = ['Alex', 'Dana', 'Bob', 'Vergil']
#     info = {}
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeat_password = request.POST.get('repeat_password')
#         age = request.POST.get('age')
#
#         try: # проверили тип данных чтобы в будущем сравнить >18
#             age = int(age)
#         except(ValueError, TypeError):
#             info['error'] = 'Возраст должен быть числом!'
#             return render(request, 'fifth_task/registration_page.html', info)
#
#         if username in users:
#             info['error'] = 'Пользователь уже существует!'
#         elif password != repeat_password:
#             info['error'] = 'Пароли не совпадают!'
#         elif age < 18:
#             info['error'] = 'Вы должны быть старше 18 лет!'
#         else:
#             return HttpResponse(f'Приветствуем, {username}!')
#
#     return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_django(request):
    users = ['Alex', 'Dana', 'Bob', 'Vergil']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


            if username in users:
                info['error'] = 'Пользователь уже существует!'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет!'
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        context = {'form': form}
        context.update(info)
    return render(request, 'fifth_task/registration_page.html', context)