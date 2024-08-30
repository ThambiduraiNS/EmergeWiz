def user_context_processor(request):
    return {'user': request.user}
