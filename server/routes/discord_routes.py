from flasgger import swag_from
from flask import jsonify, Blueprint


def create_discord_blueprint(discord_bot_service):
    discord_bp = Blueprint('discord_bot', __name__)

    @discord_bp.route('/api/v1/discord_messages', methods=['GET'])
    @swag_from({
        'summary': 'Get Discord messages',
        'responses': {
            200: {
                'description': 'Returns Discord messages',
                'schema': {
                    'type': 'array',
                    'items': {'$ref': '#/definitions/DiscordMessage'}
                }
            }
        }
    })
    def get_messages():
        """
        Get Discord messages
        ---
        responses:
          200:
            description: Returns Discord messages
        """
        return jsonify(discord_bot_service.messages)

    return discord_bp
