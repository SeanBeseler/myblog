
"""my files"""
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound
from ..models import Entry
import datetime

ENTRY =[
   {'entry_id': 0, 'date': '5/24/17', 'text': 'Entry Here'},
   {'entry_id': 1, 'date': '5/25/17', 'text': 'Entry Here'},
   {'entry_id': 2, 'date': '5/26/17', 'text': 'Entry Here'},
   {'entry_id': 3, 'date': '5/27/17', 'text': 'Entry Here'},
   {'entry_id': 4, 'date': '5/28/17', 'text': 'Entry Here'},
   {'entry_id': 5, 'date': '5/29/17', 'text': 'Entry Here'},
   {'entry_id': 6, 'date': '5/30/17', 'text': 'Entry Here'},
   {'entry_id': 7, 'date': '5/31/17', 'text': 'Entry Here'},
   {'entry_id': 8, 'date': '6/1/17', 'text': 'Entry Here'}
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
    # print(request)
    entry = session.query(Entry).get(the_id)
    entry.date = entry.date.strftime("%b/%m/%Y")
    return {
        'entry': entry
    }

@view_config(route_name='create',renderer='../templates/New.jinja2')
def create_view_page(request):
    """Reruns the new.html as the home page"""
    return {'entry': ENTRY}

@view_config(route_name='update',renderer='../templates/about.jinja2')
def update_view_page(request):
    """Retruns the post.html as the home page"""
    return {'entry': ENTRY}

