from flask import jsonify, request, Blueprint, current_app
from flask_jwt_extended import jwt_required


def create_font_blueprint(font_service, jwt_service):
    font_bp = Blueprint('font', __name__)

    @font_bp.route('/api/v1/fonts', methods=['GET'])
    def get_all_fonts():
        fonts = font_service.get_all_fonts()
        return jsonify([font.as_dict() for font in fonts])

    @font_bp.route('/api/v1/fonts/<int:font_id>', methods=['GET'])
    def get_font_by_id(font_id):
        font = font_service.get_font_by_id(font_id)
        if font:
            return jsonify(font.as_dict())
        return jsonify({'error': 'Font not found'}), 404

    @font_bp.route('/api/v1/fonts/name/<string:font_name>', methods=['GET'])
    def get_font_by_name():
        font_name = request.args.get('name')
        font = font_service.get_font_by_name(font_name)
        if font:
            return jsonify(font.as_dict())
        return jsonify({'error': 'Font not found'}), 404

    # random matching font pair
    @font_bp.route('/api/v1/fonts/pair', methods=['GET'])
    def get_font_pair():
        font_pair = font_service.get_random_font_pair()
        if font_pair:
            return jsonify(font_pair)
        return jsonify({'error': 'Font pair not found'}), 404

    # font that matches the given font
    @font_bp.route('/api/v1/fonts/pair/<string:font_name>', methods=['GET'])
    def get_matching_font(font_name):
        font = font_service.get_matching_font(font_name, current_app.app_context())
        if font:
            return jsonify(font.as_dict())
        return jsonify({'error': 'Font not found'}), 404

    @font_bp.route('/api/v1/fonts/collector', methods=['POST'])
    @jwt_required()
    def start_font_collector():
        jwt_token = request.headers.get('Authorization').split('Bearer ')[1]
        if not jwt_service.has_jwt_token(jwt_token):
            return jsonify({'error': 'Unauthorized'}), 401

        font_service.start_collector(current_app.app_context())

        return jsonify({'message': 'Font collector started'}), 200

    @font_bp.route('/api/v1/fonts/collector', methods=['GET'])
    @jwt_required()
    def get_font_collector_status():
        jwt_token = request.headers.get('Authorization').split('Bearer ')[1]
        if not jwt_service.has_jwt_token(jwt_token):
            return jsonify({'error': 'Unauthorized'}), 401

        if font_service.is_collector_running():
            return jsonify({'status': 'running'}), 200
        else:
            return jsonify({'message': 'finished'}), 200

    return font_bp
