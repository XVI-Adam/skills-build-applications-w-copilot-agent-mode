@api_view(['GET'])
def api_root(request, format=None):
    # Dynamically construct the base URL
    base_url = request.build_absolute_uri('/')[:-1]  # Remove trailing slash
    return Response({
        'users': base_url + '/api/users/?format=api',
        'teams': base_url + '/api/teams/?format=api',
        'activities': base_url + '/api/activities/?format=api',
        'leaderboard': base_url + '/api/leaderboard/?format=api',
        'workouts': base_url + '/api/workouts/?format=api'
    })