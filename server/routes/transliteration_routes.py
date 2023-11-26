import os

from flasgger import swag_from
from flask import request, send_file, jsonify, Blueprint


def create_transliteration_blueprint(transliteration_service, gpt_service):
    transliteration_bp = Blueprint('transliteration', __name__)

    @transliteration_bp.route('/api/v1/transliterate_pdf', methods=['POST'])
    @swag_from({
        'summary': 'Transliterate PDF file',
        'parameters': [
            {
                'name': 'file',
                'in': 'formData',
                'type': 'file',
                'required': True,
                'description': 'PDF file to be transliterated',
            }
        ],
        'responses': {
            200: {
                'description': 'Transliteration successful',
                'content': {'application/pdf': {}}
            },
            400: {
                'description': 'No file part or No selected file'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def transliterate_pdf():
        """
        Transliterate PDF file
        ---
        parameters:
          - name: file
            in: formData
            type: file
            required: true
            description: PDF file to be transliterated
        responses:
          200:
            description: Transliteration successful
          400:
            description: No file part or No selected file
          500:
            description: Internal Server Error
        """
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file and file.filename.endswith(".pdf"):
            edited_file_path = transliteration_service.transliterate_pdf(file)

            if edited_file_path is None:
                return "Error: file path is None"

            response = send_file(edited_file_path,
                                 as_attachment=True,
                                 download_name="edited_file.pdf",
                                 mimetype="application/pdf")

            # Delete files after sending
            os.remove("uploads" + os.sep + file.filename)
            os.remove(edited_file_path)

            return response
        return "Invalid file format. Please upload a .pdf file."

    @transliteration_bp.route('/api/v1/transliterate_txt', methods=['POST'])
    @swag_from({
        'summary': 'Transliterate TXT file',
        'parameters': [
            {
                'name': 'file',
                'in': 'formData',
                'type': 'file',
                'required': True,
                'description': 'TXT file to be transliterated',
            }
        ],
        'responses': {
            200: {
                'description': 'Transliteration successful',
                'content': {'text/plain': {}}
            },
            400: {
                'description': 'No file part or No selected file'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def transliterate_txt_file():
        """
        Transliterate TXT file
        ---
        parameters:
          - name: file
            in: formData
            type: file
            required: true
            description: TXT file to be transliterated
        responses:
          200:
            description: Transliteration successful
          400:
            description: No file part or No selected file
          500:
            description: Internal Server Error
        """
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        if file and file.filename.endswith('.txt'):
            edited_file_path = transliteration_service.transliterate_txt(file)

            response = send_file(edited_file_path,
                                 as_attachment=True,
                                 download_name="edited_file.txt",
                                 mimetype="text/plain")

            # Delete files after sending
            os.remove(edited_file_path)

            return response

        return "Invalid file format. Please upload a .txt file."

    @transliteration_bp.route('/api/v1/transliterate_text', methods=['POST'])
    @swag_from({
        'summary': 'Transliterate text',
        'parameters': [
            {
                'name': 'prompt',
                'in': 'formData',
                'type': 'string',
                'required': True,
                'description': 'Text to be transliterated',
            }
        ],
        'responses': {
            200: {
                'description': 'Transliteration result',
                'schema': {'$ref': '#/definitions/TransliterationResult'}
            },
            400: {
                'description': 'No prompt provided'
            },
            500: {
                'description': 'Internal Server Error'
            }
        }
    })
    def transliterate_text():
        """
        Transliterate text
        ---
        parameters:
          - name: prompt
            in: formData
            type: string
            required: true
            description: Text to be transliterated
        responses:
          200:
            description: Transliteration result
          400:
            description: No prompt provided
          500:
            description: Internal Server Error
        """
        try:
            data = request.json
            prompt = data.get('prompt', '')

            if not prompt:
                return jsonify({'error': 'No prompt provided'}), 400

            prompt = 'Transliterate the following text from Serbian latin to Serbian cyrillic: ' + prompt
            response = gpt_service.call_gpt_api(prompt)
            return jsonify({'result': response})

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return transliteration_bp
