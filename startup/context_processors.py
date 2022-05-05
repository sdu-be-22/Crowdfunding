def message_processor(request):
    is_authenticated = False
    username = 'Guest'
    if request.user.is_authenticated:
        is_authenticated = True
        username = request.user.username

    return {
        'is_authenticated': is_authenticated,
        'username': username
    }