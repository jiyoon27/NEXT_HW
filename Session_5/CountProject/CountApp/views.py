from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    without_blank = len(text.replace(" ",""))
    word_count = len(text.split())
    return render(request, 'result.html', {'text': text, 'total_len': total_len, 'without_blank': without_blank, 'word_count': word_count, })
