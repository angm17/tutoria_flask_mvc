def init_app_routes(app):
    from .controllers.home_controller import home
    from .controllers.usuario_controller import usuario
    
    app.register_blueprint(usuario, url_prefix='/usuarios')
    
    
    app.register_blueprint(home, url_prefix='/')
