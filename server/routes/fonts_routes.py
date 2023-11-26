import threading
from flask import jsonify, request
from __main__ import app, font_service, GOOGLE_FONTS_API_KEY

from fonts.font_collector import start_collector


@app.route('/api/v1/fonts', methods=['GET'])
def get_all_fonts():
    fonts = font_service.get_all_fonts()
    return jsonify([font.as_dict() for font in fonts])

@app.route('/api/v1/fonts/<int:font_id>', methods=['GET'])
def get_font_by_id(font_id):
    font = font_service.get_font_by_id(font_id)
    if font:
        return jsonify(font.as_dict())
    return jsonify({'error': 'Font not found'}), 404


@app.route('/api/v1/fonts/name/<string:font_name>', methods=['GET'])
def get_font_by_name():
    font_name = request.args.get('name')
    font = font_service.get_font_by_name(font_name)
    if font:
        return jsonify(font.as_dict())
    return jsonify({'error': 'Font not found'}), 404


# random matching font pair
@app.route('/api/v1/fonts/pair', methods=['GET'])
def get_font_pair():
    font_pair = font_service.get_random_font_pair()
    if font_pair:
        return jsonify(font_pair)
    return jsonify({'error': 'Font pair not found'}), 404


# font that matches the given font
@app.route('/api/v1/fonts/pair/<int:font_id>', methods=['GET'])
def get_matching_font_pair(font_id):
    font_pair = font_service.get_matching_font_pair(font_id)
    if font_pair:
        return jsonify(font_pair)
    return jsonify({'error': 'Font pair not found'}), 404

# A threading event to signal task completion
task_running = threading.Event()
def task_start_font_collector():
    start_collector(GOOGLE_FONTS_API_KEY, font_service)
    task_running.clear()


# # TODO: start collector on an api call
# @app.route('/api/v1/fonts/collector', methods=['POST'])
# # @jwt_required()
# def start_font_collector():
#     # current_user = get_jwt_identity()

#     # Check if the current user is the admin
#     # if current_user != config.get('JWT', 'admin_username', raw=True):
#     #     return jsonify({'error': 'Unauthorized'}), 401

#     # # single thread
#     # save_fonts(font_service)

#     # start new thread for the font collector
#     task_running.set()
#     threading.Thread(target=task_start_font_collector).start()
#     return jsonify({'message': 'Font collector started'}), 200

    
# @app.route('/api/v1/fonts/collector', methods=['GET'])
# # @jwt_required()
# def get_font_collector_status():
#     # current_user = get_jwt_identity()

#     # Check if the current user is the admin
#     # if current_user != config.get('JWT', 'admin_username', raw=True):
#     #     return jsonify({'error': 'Unauthorized'}), 401

#     if task_running.is_set():
#         return jsonify({'status': 'running'}), 200
#     else:
#         return jsonify({'message': 'finished'}), 200