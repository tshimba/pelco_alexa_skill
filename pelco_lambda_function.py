#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) 2018 Taiki Shimba. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# --------------------------------------------------------------------------------------------

import random

data = ("https://s3.amazonaws.com/alexa-sound-2326/catbattle1.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catdrink1.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catkitty1.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catkitty2.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal1.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal2.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal3.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal4.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal5.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal6.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal7.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal8.mp3",
        "https://s3.amazonaws.com/alexa-sound-2326/catnormal9.mp3")

def build_speechlet_response(title, output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Main handler ------------------
def lambda_handler(event, context):
    session_attributes = {}
    card_title = "Pelco meow"
    speech_output = "<speak>" \
                    "<audio src='" + random.choice(data) + "'/>" \
                    "</speak>"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

