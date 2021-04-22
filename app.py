"""
Authors: Will Escamilla, Zack Edwards, Grace Miguel, Viviane Farnung

This is the main code for our slack bot
"""
import os
from slack_bolt import App
from slack_bolt.oauth.internals import get_or_create_default_installation_store

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
    reply=f"*Okay <@{body['user']['id']}>, here's your joke:* _poopie poopie poop head_"
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

@ app.action("wants_quote")
def quote_requested(body, ack, say):
    reply=f"Okay <@{body['user']['id']}>, here's your quote: *'It's not whether you get knocked down, it's whether you get up.' -Vince Lombardi"
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


# @ app.action("wants_web")
# @ app.action("wants_video")
#This is the quote response

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
