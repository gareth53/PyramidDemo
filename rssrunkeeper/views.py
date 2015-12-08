from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from .models import Profile

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    Profile
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
    if request.POST:
        profile_id = request.params['profile_id']
        delete_profiles = DBSession.query(Profile).filter(Profile.id==profile_id).all()
        for profile in delete_profiles:
            DBSession.delete(profile)
    profiles = DBSession.query(Profile).all()
    return { 'profiles': profiles }

@view_config(route_name='profile_add', renderer='templates/profile_add.pt')
def profile_add(request):
    if request.POST:
        name = request.params['profile_name']
        slug = request.params['profile_slug']
        check_slug = DBSession.query(Profile).filter(Profile.slug==slug).all()
        if check_slug:
            return { 'errors': ['The slug %s is already in use' % slug]}
        profile = Profile(username=name, slug=slug)
        DBSession.add(profile)
        # rediret to profiles page
        return HTTPFound(location='/profiles/')
    else:
        return { 'errors': False }


class ProfileView(object):
    """
    sample class view
    """
    
    def __init__(self, request):
        self.request = request

    @view_config(route_name='profile_view', renderer='templates/profile.pt')
    def __call__(self):
        slug = self.request.matchdict['name']
        profiles = DBSession.query(Profile).filter(Profile.slug==slug)
        try:
            profile = profiles[0]
        except IndeError:
            profile = None
        return {'profile': profile }