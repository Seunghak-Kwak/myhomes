from django.shortcuts import render
from .models import Data
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def data_list(request):

    return render(request, 'mysite/data_list.html', {})

@csrf_exempt
def submit_ok(request):
    if request.method == 'POST': # If the form has been submitted...

        items = dict(request.POST)

        nickname = "".join(items['nickname'])
  
        Data(
        nickname = nickname,
        age = "".join(items['age']),
        sex = "".join(items['sex']),
        job = "".join(items['job']),
        contact = "".join(items['contact']),

        location = "".join(items['location']),
        moving_date = "".join(items['moving_date']),
        deal_type ='|'.join(items['deal_type']),
        residence_type = '|'.join(items['residence_type']),
        room_type = '|'.join(items['room']),
        roomfloor = '|'.join(items['floor']),
        room_size = '|'.join(items['size']),
        option = '|'.join(items['option']),

        deposit = "".join(items['deposit_min']) + "~"+ "".join(items['deposit_max']),
        price = "".join(items['price_min']) + "~"+ "".join(items['price_max']),
        manage_price = '월세에 포함',
        detail = "".join(items['detail'])).save()

        context = {
            'nickname': nickname
        }


    return render(request, 'mysite/submit_ok.html', context=context)
