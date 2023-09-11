from django.shortcuts import render
from datetime import datetime ,timezone, timedelta
from django.http import JsonResponse

# Create your views here.
def endpoint(request):
    slack_name = request.GET.get('slack_name','Kaosara Bakare')
    track = request.GET.get('track','backend')
    current_utc_time = datetime.now(timezone.utc)
    current_utc_time_str = current_utc_time.strftime('%d-%m-%Y %H:%M:%S %Z')
    current_day = current_utc_time.strftime('%A')
    github_file_url = 'https://github.com/KaosaraBakare/zuri_taskone/blob/main/zuri/zuri/zuri_taskone'
    github_repo_url = 'https://github.com/KaosaraBakare/zuri_taskone'

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_utc_time_str,
        'track': track,
        'github_url_file': github_file_url,
        'github_url_source': github_repo_url,
        'status_code': 200
    }

    return JsonResponse(response_data, status = 200)
