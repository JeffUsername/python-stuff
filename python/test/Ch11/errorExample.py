# def spam():
#     bacon()

# def bacon():
#     raise Exception('This is the error message.')

# spam()
# import traceback
# try:
#    raise Exception('This is the error message.')
# except:
#           errorFile = open('errorInfo.txt', 'w')
#           errorFile.write(traceback.format_exc())
#           errorFile.close()
#           print('The traceback info was written to errorInfo.txt.')
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}
switchLights(market_2nd)
