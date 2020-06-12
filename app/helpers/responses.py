def responseSuccess(field, data=[], message=None):
    response = dict()
    response['result'] = 'success'
    if len(data) > 0: response[field] = data
    if message is not None: response['message'] = message
    return response


def responseError(message):
    response = dict()
    response['result'] = 'error'
    response['message'] = message
    return response
