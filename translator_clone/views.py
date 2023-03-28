from django.shortcuts import render
from googletrans import Translator
# Create your views here.



def translate_app(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)

        translator = Translator()
        detected_lang = translator.detect(txt).lang
        tr = translator.translate(txt, dest=lang, src=detected_lang)

        return render(request, 'translate.html', {"result":tr.text})

    return render(request, 'translate.html')