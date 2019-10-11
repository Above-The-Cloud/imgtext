import json
import traceback

from MySQLdb._exceptions import IntegrityError
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from articles.models import Article


def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def create(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    # if not {'user_id','title','label','content'}.issubset(request.POST.keys()):
    #     return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': json.dumps(request.POST.dict())}))
    try:
        params = request.POST.dict()
        dis=Article.objects.create(**params)
        res['data']['id']=dis.id
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': e, 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def list(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    try:
        params = request.POST.dict()
        page=0
        size=5
        if 'page' in params:
            page=int(params['page'])
            params.pop('page')
        if 'size' in params:
            size=int(params['size'])
            params.pop('size')
        params['status']=1
        res['data']['total']=Article.objects.filter(**params).count()
        res['data']['articles']=[]
        qset=Article.objects.filter(**params).order_by('-ctime')[page*size:(page+1)*size]
        articles=json.loads(serializers.serialize("json", qset))

        for article in articles:
            data_row=article['fields']
            data_row['id']=article['pk']
            del data_row['status']
            res['data']['articles'].append(data_row)
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': e, 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def update(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'id','update'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        Article.objects.filter(id=request.POST['id']).update(**json.loads(request.POST['update']))
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': e, 'data': []}))
    return HttpResponse(json.dumps(res))


@csrf_exempt
def delete(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'id'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        Article.objects.filter(id=request.POST['id']).update(status=0)
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': e, 'data': []}))
    return HttpResponse(json.dumps(res))