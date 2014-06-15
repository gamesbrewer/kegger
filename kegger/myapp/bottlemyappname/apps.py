import bottle

def create_app():
    import views
    bottle.run(app=views.app, server='gae')
    bottle.debug(True)
    return views.app