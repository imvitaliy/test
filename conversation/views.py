import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializer import SentenceSerializer
from .models import Sentence, SentenceCounter

def get_next_element(sentences, num):
    index = sentences.index(num)
    if len(sentences)-1 > index:
        return sentences[index+1]
    else:
        return sentences[0]

@csrf_exempt
def sentence_list(request):
    """
    List all code Sentences, or create a new sentence.
    """
    if request.method == 'GET':
        s_counter = SentenceCounter.objects.last()
        if not s_counter:
            return JsonResponse({"no":"data"}, safe=False)
        else:
            next_item = get_next_element(json.loads(s_counter.sentences),s_counter.sentence_number)
            s_counter.sentence_number = next_item
            s_counter.save()
            sentence = Sentence.objects.get(id=next_item)
            serializer = SentenceSerializer(sentence)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SentenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            s_counter = SentenceCounter.objects.first()
            if not s_counter:
                s_counter = SentenceCounter()
                s_counter.sentences="[{}]".format(serializer.instance.id)
                s_counter.sentence_number=serializer.instance.id
                s_counter.save()
            else:
                counter = json.loads(s_counter.sentences)
                counter.append(serializer.instance.id)
                s_counter.sentences = str(counter)
                s_counter.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

