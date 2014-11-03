import json
from django.shortcuts import render
from .models import Paper

# Create your views here.

def show(request):
    paper = Paper.objects.all()[0]
    
    return render(request, 'psytest/show.html', {
        'data': json.dumps(paper_to_json(paper))
    })

def paper_to_json(paper):
    json_paper = {'name':paper.name}
    json_paper['questions'] = []
    for q in paper.question_set.all():
        q_item = {'text': q.text, 'order': q.order,'id':q.pk}
        q_item['options'] = []
        for o in q.option_set.all():
            op = {'text': o.text, 'score':o.score, 'show_result':o.show_result}
            if o.next_question is not None:
                op['next'] = o.next_question.id
            else:
                op['next'] = None
            q_item['options'].append(op)
        
        json_paper['questions'].append(q_item)
    json_paper['results'] = []
    for r in paper.result_set.all():
        res = {'text':r.text, 'score_begin':r.score_begin,
               'score_end':r.score_end, 'id':r.pk}
        json_paper['results'].append(res)
    return json_paper
