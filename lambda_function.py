WELCOME_SPEECH = 'What would you like to know?'

HELP_INTENT, CANCEL_INTENT, STOP_INTENT, CONTENT_INTENT, NUTRITION_INTENT, EXPIRATION_INTENT = 'AMAZON.HelpIntent', 'AMAZON.CancelIntent', 'AMAZON.StopIntent', 'content', 'nutrition', 'expiration'

LAUNCH_REQUEST, INTENT_REQUEST, SESSION_ENDED_REQUEST = 'LaunchRequest', 'IntentRequest', 'SessionEndedRequest'

expirations = {'apple': 30, 'tomato': 14, 'orange': 30}


def get_nutrition(item, d):
    items = get_items(d)

    return d[items.index(item)][item]


def get_items(d):
    items = []
    for item in d:
        items.append(list(item.keys())[0])

    return items


def get_data():
    AWS_ACCESS_KEY_ID = '-----------'
    AWS_SECRET_ACCESS_KEY = '-------------'

    bucket_name = 'smart-fridge-basehacks'

    # conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
    #         AWS_SECRET_ACCESS_KEY)

    # testfile = "image.jpg"
    # print('Uploading %s to Amazon S3 bucket %s' % (testfile, bucket_name))

    def percent_cb(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()

    import boto3

    # bucket = conn.get_bucket(bucket_name)

    # # add new file
    # k = Key(bucket)
    # k.key = testfile
    # k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)

    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)
    body = 'no body found'

    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read().decode("utf-8")

    #
    # key = obj.key
    # body = obj.get()['Body'].read()
    # print(body)

    import json

    return json.loads(body)


# Speech
def say(output='', reprompt_text='', title='', should_end_session=True):
    """ Builds a spoken response and will end the session by default """
    if reprompt_text == '':
        reprompt_text = output

    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': title,
                'content': output
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': reprompt_text
                }
            },
            'shouldEndSession': should_end_session
        }
    }


def question(question_base, extension='', intro=''):
    """ Asks a question and prepares the users response """

    if extension != '':
        extension = ' ' + str(extension)

    question_text = question_base + extension

    return say(output=intro + ' ' + question_text, reprompt_text=question_text, should_end_session=False)


def welcome():
    """ Welcomes the user with a message and randomly picks a question to ask the user about their number """
    return question(WELCOME_SPEECH)


def help():
    return question(WELCOME_SPEECH)


def end():
    """ Terminates the current session """
    return say()


def unexpected_response():
    """Returns the unexpected response speech."""
    return say('unexpected')


# Event handlers and related variables
def handle_intent(event):
    intent_name = event['request']['intent']['name']
    """ Called when the user specifies an intent for this skill """
    if intent_name in name_to_handler:  # for no slot intents
        return name_to_handler[intent_name]()
    elif intent_name == NUTRITION_INTENT:
        d = get_data()
        items = get_items(d)

        item = event['request']['intent']['slots']['food']['value']

        if item in items:
            nutrition = get_nutrition(item, d)

            # fat carbs calories protein

            return say(
                'A ' + item + " has {} calories, {} grams of fat, {} grams of carbs, and {} grams of protein".format(
                    nutrition['calories'], nutrition['fat'], nutrition['carbs'], nutrition['protein']))
        else:
            return say('Nutrition facts for ' + item + " are not available.")
    elif intent_name == EXPIRATION_INTENT:
        d = get_data()
        items = get_items(d)

        item = event['request']['intent']['slots']['food']['value']

        if item in items:
            if item in expirations:
                return say('your ' + item + " will expire in {} days".format(expirations[item]));
            else:
                return say('this item is in your refrigerator, but no expiration date data could be found.')
        else:
            return say('could not find expiration date information for ' + item)
    elif intent_name == CONTENT_INTENT:
        d = get_data()

        items = get_items(d)

        if len(items) == 1:
            return say('there is only ' + items[0])
        elif len(items) == 0:
            return say('there is currently nothing recognized in the fridge')
        else:
            return say('there are ' + ', '.join(items[:len(items) - 1]) + ', and ' + items[len(items) - 1])
    else:
        return say(intent_name + ' could not be launched')


def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    # Have to add 'attributes' entry into the event session since it could not find
    # it from a physical device even though it worked in the online testing
    if 'attributes' not in event['session']:
        event['session']['attributes'] = {}

    global session_attributes
    session_attributes = event['session']['attributes']

    return request_to_handler[event['request']['type']](event)


name_to_handler = {HELP_INTENT: help,
                   CANCEL_INTENT: end,
                   STOP_INTENT: end}

request_to_handler = {LAUNCH_REQUEST: lambda event: welcome(),
                      INTENT_REQUEST: lambda event: handle_intent(event),
                      SESSION_ENDED_REQUEST: lambda event: end()}