from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/notificationClient', methods=['POST'])
def notification_client():
    change_notification = request.json['value'][0]

    # Microsoft sends a validation request when creating the subscription
    validation_token = request.args.get('validationToken')
    if validation_token:
        return validation_token

    # When a real notification is received
    # send a message to Discord using a Discord webhook URL
    discord_webhook_url = 'your-discord-webhook-url-here'

    message = {
        'content': 'A change happened in the monitored resource!',
        # Customize the message based on `changeNotification` properties
    }

    requests.post(discord_webhook_url, json=message)

    return '', 200  # Respond to Graph API that the notification was received

if __name__ == "__main__":
    app.run(port=3000, debug=True)
