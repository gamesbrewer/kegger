def create_app():
    import views
    app = views.config.make_wsgi_app()
    return app