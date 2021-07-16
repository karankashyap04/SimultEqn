from django.shortcuts import render  # , get_object_or_404
from django.http import HttpResponse
from .models import Question

import numpy as np

# from django.template import loader

# Create your views here.

def index(request):
    latest_questions = Question.objects.all()
    # output = ", ".join(ques.question_text for ques in latest_questions)
    # template = loader.get_template('eqnsolver2/index.html')
    context = {
        'latest_questions': latest_questions
    }
    # return HttpResponse('This is the index page of the eqnsolver2 application!')
    # return HttpResponse(output)
    # return HttpResponse(template.render(context))
    return render(request, 'eqnsolver2/index.html', context)


def determinant(arr):
    det = (arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0])
    return det

def adjoint(arr):  # See if there is a built-in function for computing the adjoint
    new_arr = np.empty(4).reshape(2, 2)
    new_arr[0][0] = arr[1][1]
    new_arr[1][1] = arr[0][0]
    new_arr[0][1] = -1 * arr[0][1]  # adjoint -> transpose of cofactors
    new_arr[1][0] = -1 * arr[1][0]
    return new_arr

def calculate_answer(arr, b):  # Confirm the logic here once
    det = determinant(arr)
    if det == 0 and b[0][0] == 0 and b[1][0] == 0:
        return "inf"
    elif det == 0 and (arr[1][0]/arr[0][0]) == (b[1][0]/b[0][0]):
        return "same"
    elif det == 0:
        return "impossible"
    else:
        adj = adjoint(arr)  # See if there is a built-in function for matrix multiplication
        ans = np.empty(2).reshape(2, 1)
        ans[0][0] = (adj[0][0] * b[0][0]) + (adj[0][1] * b[1][0])
        ans[1][0] = (adj[1][0] * b[0][0]) + (adj[1][1] * b[1][0])
        ans /= det
        return ans

def solve_2var(request):
    return render(request, 'eqnsolver2/solve_2var.html', {})
    # return HttpResponse('This is the solving page for the 2 variable simultaneous equations!')

def results_2var(request):
    try:
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        c = float(request.POST['c'])
        d = float(request.POST['d'])
        e = float(request.POST['e'])
        f = float(request.POST['f'])
    except:
        return render(request, 'eqnsolver2/solve_2var.html', {'error_message': "Please enter all values!"})
    else:
        A = np.array([[a, b], [d, e]])
        B = np.array([[c], [f]])

        answer = calculate_answer(A, B)
        if answer == "inf":
            return render(request, 'eqnsolver2/solve_2var.html',
                          {'error_message': "There are infinitely many solutions to this system of equations"})
        elif answer == "same":
            return render(request, 'eqnsolver2/solve_2var.html',
                          {'error_message': "Both these equations are essentially the same"})
        elif answer == "impossible":
            return render(request, 'eqnsolver2/solve_2var.html', {'error_message': "There are no solutions"})
        else:
            context = {
                'x': str(answer[0][0]),
                'y': str(answer[1][0])
            }
            return render(request, 'eqnsolver2/results_2var.html', context)
    # return HttpResponse('This is the results page for the 2 variable simultaneous equations!')


def solve_3var(request):
    return HttpResponse('The solving page for the 3 variable simultaneous equations will be operational shortly')

def results_3var(request):
    return HttpResponse('The results page for the 3 variable simultaneous equations will be operational shortly')