"""
Authors: Will Escamilla, Zack Edwards, Grace Miguel, Viviane Farnung

This is the main code for our slack bot
"""
import os
import random
import data
from slack_bolt import App
from slack_bolt.oauth.internals import get_or_create_default_installation_store
import requests

#our database
link = 'https://sheetdb.io/api/v1/7a4208wp8ee6d'


#what is ngrok.exe???

# Initializes your app with your bot token and signing secret
#what is a signing secret?
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Listens to incoming messages that contain "hello"

"""
This function returns a default message for various inputs
"""
@app.message("!distract me")
def default_message(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        {
            "attachments": [
                {
                    "color": "#f2c744",
                    "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "Distraction Time!"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*Please select a distraction <@{message['user']}>:*"
                            }
                        },
                        {
                            "type": "divider"
                        },
                        {
                            "type": "actions",
                            "elements": [
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Joke"
                                    },
                                    "action_id": "wants_joke"
                                },
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Website"
                                    },
                                    "action_id": "wants_web"
                                },
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Video"
                                    },
                                    "action_id": "wants_video"
                                },
                                {
                                    "type": "button",
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Quote"
                                    },
                                    "action_id": "wants_quote"
                                }
                            ]
                        }
                    ],
                }
            ]
        }
    )


@app.message("stress")
def stress_message(message, say):
    say(
       {
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Time for a Break"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"Hi <@{message['user']}> :wave:"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "You seem to be a tad stressed. Stretch your legs and go for a walk!",
					
				}
			]
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "You seem a tad stressed. You're working so hard, it's time you take a break. May I suggest one of the following:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "• Go for a walk \n • Meditate \n • Talk to a friend"
			}
		}
	]
}
    )

# @app.message("!distract web")
# @app.message("!distract quote")

@ app.action("wants_joke")
def joke_requested(body, ack, say):
    # Acknowledge the action
    r = requests.get(link).json()
    for i in r:
        if i['type'] == 'joke':
            answer = i['content']
    reply=f"*Okay <@{body['user']['id']}>, here's your joke:* " + answer
    ack()
    say(
        {
            "attachments": [
                {
                    "color": "#f2c744",
                    "text": reply
                }
            ]
        }
    )


@ app.action("wants_web")
def web_requested(body, ack, say):
    r = requests.get(link).json()
    for i in r:
        if i['type'] == 'link':
            answer = i['content']
    #acknowledge the answer
    reply=f"*Okay <@{body['user']['id']}>, here's your link:* " + answer
    ack()
    say(
        {
            "attachments":[
                {
                    "color": "#f2c744",
                    "text": reply
                }
            ]
        }
    )
@ app.action("wants_video")
def video_requested(body, ack, say):
    r = requests.get(link).json()
    for i in r:
        if i['type'] == 'video':
            answer = i['content']
    #acknowledge the answer
    reply=f"*Okay <@{body['user']['id']}>, here's your video:* " + answer
    ack()
    say(
        {
            "attachments":[
                {
                    "color": "#f2c744",
                    "text": reply
                }
            ]
        }
    )


@ app.action("wants_quote")
def quote_requested(body, ack, say):
    r = requests.get(link).json()
    for i in r:
        if i['type'] == 'quote':
            answer = i['content']
    #acknowledge the answer
    reply=f"*Okay <@{body['user']['id']}>, here's your quote:* " + answer
    ack()
    say(
        {
            "attachments":[
                {
                    "color": "#f2c744",
                    "text": reply
                }
            ]
        }
    )

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
