from Silo.routing.route import Route

url_map = [
    Route().get('/', 'home_controller@index'),
    Route().get('/test', 'home_controller@details'),
    Route().get('/test/', 'home_controller@details'),
    Route().get('/test/<some_var>', 'home_controller@details'),
    Route().get('/example', 'home_controller@details'),
    Route().get('/test/{required}', 'home_controller@test')
]
