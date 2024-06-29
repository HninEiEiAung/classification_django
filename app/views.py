from django.http import JsonResponse
from django.shortcuts import render
from transformers import pipeline

# Create your views here.

pipe = pipeline("text-classification", model="hnin-ei1/my_awesome_model")

def home(request):
    print("Hello")
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        ans = pipe(input_text)
        print(ans)
        return render(request,'index.html',{'classify':ans})

    return render(request,'index.html')