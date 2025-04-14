from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    # Dynamically construct the base URL
    base_url = request.build_absolute_uri('/')[:-1]  # Remove trailing slash
    api_suffix = '/api'  # Add API suffix
    return Response({
        'users': base_url + api_suffix + '/users/?format=api',
        'teams': base_url + api_suffix + '/teams/?format=api',
        'activities': base_url + api_suffix + '/activities/?format=api',
        'leaderboard': base_url + api_suffix + '/leaderboard/?format=api',
        'workouts': base_url + api_suffix + '/workouts/?format=api'
    })