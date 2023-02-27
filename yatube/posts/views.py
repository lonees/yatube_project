from django.shortcuts import render


# Главная страница
def index(request):
    context = {
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, 'posts/index.html', context)


# Страница со списком мороженого
def group_posts(request, slug):
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, 'posts/group_list.html', context)
