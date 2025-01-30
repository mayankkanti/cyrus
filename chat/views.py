import json
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from . import chatbot

def chatbot_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('query')
            if not message:
                return JsonResponse({'error': "Invalid input: 'content' argument must not be empty. Please provide a non-empty value."}, status=400)
            response_text = chatbot.Reply.gemini_response(message)
            response_text = response_text.replace('\n', '')
            return JsonResponse(response_text, safe=False)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': "Invalid JSON format."}, status=400)

def home(request):
    return render(request, 'cover.html')

def about(request):
    return render(request, 'about.html')