from django.shortcuts import render, redirect, reverse
from .models import *
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# import allauth.account.models
# Create your views here.

def quiz_home(request):
    return render(request, 'game/mainpage.html')

def create(request):
    if request.method== 'GET':
        queryset = Quiz.objects.all()
        context = {
            'quizs': queryset,
        }
        return render(request, 'game/create.html', context=context)
    if request.method == 'POST':
        # user = User.objects.first()
        title = request.POST['quiz_title']
        username = request.POST['user_name']
        ans1 = request.POST['1']
        ans2 = request.POST['2']
        ans3 = request.POST['4']
        ans4 = request.POST['5']
        ans5 = request.POST['6']
        ans6 = request.POST['7']
        ans7 = request.POST['8']
        ans8 = request.POST['9']
        ans9 = request.POST['10']
        ans10 = request.POST['11']
        ans = [ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]

        user = User.objects.create(quiz_title=title, answer=ans, name=username, count=1)
        #user.answer = ans
        #user.quiz_title = title
        # user.name = username
        #user.save()

        url=reverse('game:quiz_home')
        return redirect(to=url)

def solve_list(request):
    queryset = User.objects.all()
    context = {
        'users': queryset,
    }
    return render(request, 'game/solve_list.html', context=context)

def solve(request, pk):
    if request.method== 'GET':
        queryset = Quiz.objects.all()
        user = User.objects.get(id=pk)
        context = {
            'quizs': queryset,
            'user': user,
        }
        return render(request, 'game/solve.html', context=context)
    if request.method == 'POST':
        #challenger = Challenger.objects.first()
        user = User.objects.get(id=pk)
        challenger = request.POST['user_name']
        ans1 = request.POST['1']
        ans2 = request.POST['2']
        ans3 = request.POST['4']
        ans4 = request.POST['5']
        ans5 = request.POST['6']
        ans6 = request.POST['7']
        ans7 = request.POST['8']
        ans8 = request.POST['9']
        ans9 = request.POST['10']
        ans10 = request.POST['11']
        ans = [ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8,ans9,ans10]
        rightanswer = user.answer
        rightanswer = rightanswer.lstrip('[').rstrip(']').split(', ')

        count = 0
        for i in range(len(rightanswer)):
            if rightanswer[i].strip("'") == ans[i]:
                count += 1
            else:
                continue

        final_result = count

        challenger = Challenger.objects.create(name=challenger, answer=ans, user_obj=user.name, result=final_result)

        #challenger.answer = ans
        #challenger.save()

        url = reverse('game:ranking', kwargs={'pk': pk})
        return redirect(to=url)

def ranking(request, pk):
    user = User.objects.get(id=pk)
    challengers_10 = Challenger.objects.filter(user_obj=user, result=10)
    challengers_9 = Challenger.objects.filter(user_obj=user, result=9)
    challengers_8 = Challenger.objects.filter(user_obj=user, result=8)
    challengers_7 = Challenger.objects.filter(user_obj=user, result=7)
    challengers_6 = Challenger.objects.filter(user_obj=user, result=6)
    challengers_5 = Challenger.objects.filter(user_obj=user, result=5)
    challengers_4 = Challenger.objects.filter(user_obj=user, result=4)
    challengers_3 = Challenger.objects.filter(user_obj=user, result=3)
    challengers_2 = Challenger.objects.filter(user_obj=user, result=2)
    challengers_1 = Challenger.objects.filter(user_obj=user, result=1)
    challengers_0 = Challenger.objects.filter(user_obj=user, result=0)


    challengers_10 = str(challengers_10).replace('<QuerySet [<Challenger:','').replace('>]>','').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_9 = str(challengers_9).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_8 = str(challengers_8).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_7 = str(challengers_7).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_6 = str(challengers_6).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_5 = str(challengers_5).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_4 = str(challengers_4).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_3 = str(challengers_3).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_2 = str(challengers_2).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_1 = str(challengers_1).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')
    challengers_0 = str(challengers_0).replace('<QuerySet [<Challenger:', '').replace('>]>', '').replace('>, <Challenger:',',').replace('<QuerySet []>','')


    context = {
        'user' : user,
        'challengers_10': challengers_10,
        'challengers_9': challengers_9,
        'challengers_8': challengers_8,
        'challengers_7': challengers_7,
        'challengers_6': challengers_6,
        'challengers_5': challengers_5,
        'challengers_4': challengers_4,
        'challengers_3': challengers_3,
        'challengers_2': challengers_2,
        'challengers_1': challengers_1,
        'challengers_0': challengers_0,
    }

    return render(request, 'game/ranking.html', context=context)