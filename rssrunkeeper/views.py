from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        conn_err_msg = "Pyramid is having a problem using your SQL database."
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'RssRunKeeper'}

@view_config(route_name='profiles', renderer='templates/profiles.pt')
def profiles(request):
    return { 'project': 'RssRunKeeper'}

@view_config(route_name='profile_view', renderer='templates/profile.pt')
def profile_view(request):
    return {'name': request.matchdict['name'], 'project': 'RssRunKeeper'}

@view_config(route_name='profiles_list', renderer='templates/profiles_list.pt')
def profiles_list(request):
    return { 'page': request.matchdict['page_no'], 'project': 'RssRunKeeper'}

