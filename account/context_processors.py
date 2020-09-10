def absolute_uri(request):
    return {'absolute_uri': request.build_absolute_uri('/')}
