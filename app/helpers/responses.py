def responseSuccess(field, data):
    response = dict()
    response['result'] = 'success'
    response[field] = data
    return response


def responseError(message):
    response = dict()
    response['result'] = 'error'
    response['message'] = message
    return response
