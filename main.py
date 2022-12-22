import logging
from slack_bolt import App
from chat import chat_ai
import os

logging.basicConfig(level=logging.DEBUG)

slack_token = os.getenv('SLACK_TOKEN')
signing_secret = os.getenv('SIGN_IN_SECRET')

app = App(token=slack_token,
          signing_secret=signing_secret,
          raise_error_for_unhandled_request=True)


@app.middleware
def log_request(logger, body, next):
    logger.debug(body)
    return next()


@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)
    question = body['event']['blocks'][0]['elements'][0]['elements'][1]['text']
    if question is not None:
        answer = chat_ai(question)
        say(answer)
    else:
        say(
            text="I didn't understand. Can please explain again?"
        )

@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


if __name__ == "__main__":
    app.start(3000)
