def init_app_routes(app):
    from .controllers.home_controller import home
    app.register_blueprint(home, url_prefix='/')
