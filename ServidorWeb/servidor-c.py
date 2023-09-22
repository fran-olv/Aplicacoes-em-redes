from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Informe seu nome e idade:</h1>')
            self.wfile.write(b'<form method="POST" action="/enviar">')
            self.wfile.write(b'Nome: <input type="text" name="nome"><br>')
            self.wfile.write(b'Idade: <input type="text" name="idade"><br>')
            self.wfile.write(b'<input type="submit" value="Enviar">')
            self.wfile.write(b'</form>')
            self.wfile.write(b'</body></html>')
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/enviar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parametros = self.parse_parametros(post_data)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body>')
            self.wfile.write(b'<h1>Resposta Recebida:</h1>')
            self.wfile.write(f'<p>Nome: {parametros["nome"]}</p>'.encode('utf-8'))
            self.wfile.write(f'<p>Idade: {parametros["idade"]}</p>'.encode('utf-8'))
            self.wfile.write(b'</body></html>')
        else:
            self.send_error(404)

    def parse_parametros(self, data):
        parametros = {}
        params = data.split('&')
        for param in params:
            chave, valor = param.split('=')
            parametros[chave] = valor
        return parametros


def run():
    endereco_servidor = ('', 8000)
    servidor_http = HTTPServer(endereco_servidor, HTTPRequestHandler)
    print('Servidor rodando em http://localhost:8000')
    servidor_http.serve_forever()


if __name__ == '__main__':
    run()