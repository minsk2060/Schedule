from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.viber_requests import (
    ViberMessageRequest,
    ViberUnsubscribedRequest,
    ViberSubscribedRequest,
    ViberConversationStartedRequest
)

from tokens import viber_users, vibertoken
from flask import Flask, request, Response


app = Flask(__name__)

bot_config = BotConfiguration(name="Вентиляция ФСК", avatar="C:/Users/BMS/projects/schedules/logo.jpg", auth_token=vibertoken)
viber = Api(bot_config)


@app.route("/", methods={"POST"})
def incoming():
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        message = viber_request.message
        viber.send_messages(viber_request.sender.id, [message])
        # print(viber_request.sender.id)
        # print([message.text])
        # print(viber.get_user_details(viber_users["Artur"]))


    # elif isinstance(viber_request, ViberSubscribedRequest):
    #     viber.send_messages(viber_request.get_user().get_id(), [TextMessage( text ="Спасибо за подписку!")])
    elif isinstance(viber_request, ViberConversationStartedRequest):
        print(viber_request.user.id)
    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port =8443, debug=True )
