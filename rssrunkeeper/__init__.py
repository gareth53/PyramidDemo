from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPNotFound
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def notfound(request):
    return HTTPNotFound()

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('profiles', '/profiles/')
    config.add_route('profile_add', '/profiles/add/')
    config.add_route('profile_view', '/profiles/{name}/')
    config.add_notfound_view(notfound, append_slash=True)

    config.scan()
    return config.make_wsgi_app()
