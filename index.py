from Silo.routing.router import Router
from routes import url_map

class App: 
    def wsgi_app(self, environ, start_response):
        response = Router(url_map).dispatch_request(environ)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = App()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
