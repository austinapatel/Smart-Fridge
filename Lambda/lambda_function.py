# Sympathy Snake Alexa skill created by Austin Patel

WELCOME_SPEECH = 'What would you like to know?'

HELP_INTENT, CANCEL_INTENT, STOP_INTENT, CONTENT_INTENT = 'AMAZON.HelpIntent', 'AMAZON.CancelIntent', 'AMAZON.StopIntent', 'content'

LAUNCH_REQUEST, INTENT_REQUEST, SESSION_ENDED_REQUEST = 'LaunchRequest', 'IntentRequest', 'SessionEndedRequest'


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
    elif intent_name == CONTENT_INTENT:
        return say('I currently do not know what is inside')
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