
"""my files"""
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound
)
from ..models import Entry
import datetime

ENTRY = [
   {'date': '5/24/17', 'text': 'Entry Here'},
   {'date': '5/25/17', 'text': 'Entry Here'},
   {'date': '5/26/17', 'text': 'Entry Here'},
   {'date': '5/27/17', 'text': 'Entry Here'},
   {'date': '5/28/17', 'text': 'Entry Here'},
   {'date': '5/29/17', 'text': 'Entry Here'},
   {'date': '5/30/17', 'text': 'Entry Here'},
   {'date': '5/31/17', 'text': 'Entry Here'},
   {'date': '6/1/17', 'text': 'Entry Here'}
]


@view_config(route_name='home',renderer='../templates/index.jinja2')
def list_view_page(request):
    all_entries = request.dbsession.query(Entry).all()
    """Returns the index.html as the home page"""
    for temp_entry in all_entries:
        temp_entry.date = temp_entry.date.strftime("%b/%m/%Y")
    return {'entries': all_entries }


@view_config(route_name='detail',renderer='../templates/post.jinja2')
def detail_view_page(request):
    """Retruns the about.html as the home page"""
    the_id = int(request.matchdict['entry_id'])
    session = request.dbsession
    entry = session.query(Entry).get(the_id)
    entry.date = entry.date.strftime("%b/%m/%Y")
    return {
        'entry': entry
    }


@view_config(route_name='create',renderer='../templates/New.jinja2')
def create_view_page(request):
    """Reruns the new.html as the home page"""
    if request.method == "POST" and request.POST:
        new_entry = Entry(
            title=request.POST["usrname"],
            text=request.POST["j_entry"],
            date=datetime.datetime.now()
        )
        
        request.dbsession.add(new_entry)
        return HTTPFound(
            location=request.route_url("home")
        )

    return {}


@view_config(route_name='update',renderer='../templates/about.jinja2')
def update_view_page(request):
    """Returns the post.html as the home page"""
    session = request.dbsession
    the_id = int(request.matchdict['id'])
    # print(request)
    entry = session.query(Entry).get(the_id)
    if not entry:
        raise HTTPNotFound
    entry.date = entry.date.strftime("%b/%m/%Y")
    if request.method == "GET":
        return {
            'entry_id': entry.entry_id,
            'text': entry.text
               }
    if request.method == "POST":
        entry.entry_id = request.POST['entry_id']
        entry.text = request.POST['text']
        return HTTPFound(request.route_url('detail',id=entry.entry_id))

