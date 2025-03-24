from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AddVacancy, AddComment
from .models import Vacancy, Comment


# @login_required
def index(request):
    vacancy = Vacancy.objects.all()

    if request.method == 'POST':
        form = AddVacancy(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddVacancy()

    return render(request, 'index.html', {'vacancy': vacancy, 'form': form})


def detail_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(pk=vacancy_id)
    comments = Comment.objects.filter(vacancy=vacancy)

    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.vacancy = vacancy
            comment.save()
            return redirect('detail_vacancy', vacancy_id=vacancy.id)
    else:
        form = AddComment()

    return render(request, 'detail_vacancy.html', {'vacancy': vacancy, 'comments': comments, 'form': form})
