from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/ia/pesquisador', methods=['POST'])
def pesquisador():
    try:
        data = request.get_json()
        query_result = data.get('queryResult', {})
        parameters = query_result.get('parameters', {})
        nicho = parameters.get('nicho', '')
        persona = parameters.get('persona', '')

        # Aqui você pode adicionar a lógica para processar os dados recebidos
        # e gerar a resposta desejada.
        resposta = {
            "fulfillmentText": f"Nicho: {nicho}, Persona: {persona}"
        }

        return jsonify(resposta)

    except Exception as e:
        return jsonify({"fulfillmentText": f"Erro: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)