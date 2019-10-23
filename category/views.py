import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from category.models import Category1, Category2


@csrf_exempt
def list(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    try:
        params = request.POST.dict()
        page=0
        size=50
        if 'page' in params:
            page=int(params['page'])
            params.pop('page')
        if 'size' in params:
            size=int(params['size'])
            params.pop('size')

        params['status'] = 1
        res['data']['categories'] = []

        if('sub' in params):
            params.pop('sub')
            res['data']['total']=Category2.objects.filter(**params).count()
            qset = Category2.objects.filter(**params)[page*size:(page+1)*size]

        else:
            res['data']['total'] = Category1.objects.filter(**params).count()
            qset = Category1.objects.filter(**params)[page * size:(page + 1) * size]

        categories=json.loads(serializers.serialize("json", qset))
        for categorie in categories:
            data_row=categorie['fields']
            data_row['id']=categorie['pk']
            del data_row['status']
            res['data']['categories'].append(data_row)
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': "error|%s" % e, 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def delete(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'id'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        if('sub' in request.POST):
            Category2.objects.filter(id=request.POST['id']).update(status=0)
        else:
            Category1.objects.filter(id=request.POST['id']).update(status=0)
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': "error|%s" % e, 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def update(request):
    res = {'code': 0, 'msg': 'success', 'data': []}
    if not {'id','update'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': []}))
    try:
        if ('sub' in request.POST):
            Category2.objects.filter(id=request.POST['id']).update(**json.loads(request.POST['update']))
        else:
            Category1.objects.filter(id=request.POST['id']).update(**json.loads(request.POST['update']))
    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': "error|%s" % e, 'data': []}))
    return HttpResponse(json.dumps(res))

@csrf_exempt
def create(request):
    res = {'code': 0, 'msg': 'success', 'data': {}}
    if not {'name'}.issubset(request.POST.keys()):
        return HttpResponse(json.dumps({'code': -1, 'msg': 'error-1|unexpected params!', 'data': json.dumps(request.POST.dict())}))
    try:
        params = request.POST.dict()
        if ('sub' in request.POST):
            if not {'father_id'}.issubset(request.POST.keys()):
                return HttpResponse(json.dumps(
                    {'code': -1, 'msg': 'error-1|unexpected params!', 'data': json.dumps(request.POST.dict())}))
            params.pop('sub')
            dis=Category2.objects.create(**params)
            res['data']['id']=dis.id
        else:
            dis = Category1.objects.create(**params)
            res['data']['id'] = dis.id

    except Exception as e:
        # traceback.print_exc()
        print(e)
        return HttpResponse(json.dumps({'code': -2, 'msg': "error|%s" % e, 'data': []}))
    return HttpResponse(json.dumps(res))