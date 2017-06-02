
"""my files"""
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound

#ENTRY =[
#    {'id': 0, 'date': '5/24/17', 'text': 'Entry Here'},
#    {'id': 1, 'date': '5/25/17', 'text': 'Entry Here'},
#    {'id': 2, 'date': '5/26/17', 'text': 'Entry Here'},
#    {'id': 3, 'date': '5/27/17', 'text': 'Entry Here'},
#    {'id': 4, 'date': '5/28/17', 'text': 'Entry Here'},
#    {'id': 5, 'date': '5/29/17', 'text': 'Entry Here'},
#    {'id': 6, 'date': '5/30/17', 'text': 'Entry Here'},
#    {'id': 7, 'date': '5/31/17', 'text': 'Entry Here'},
#    {'id': 8, 'date': '6/1/17', 'text': 'Entry Here'}
    
#    ]
@view_config(route_name='home',renderer='../templates/index.jinja2')
def list_view_page(request):
    """Retruns the index.html as the home page"""
    return {'entry': ENTRY}

@view_config(route_name='detail',renderer='../templates/post.jinja2')
def detail_view_page(request):
    """Retruns the about.html as the home page"""
    try:
        the_id = int(request.matchdict['id'])
        entrys = ENTRY[the_id]
        return {'entry': entrys}
    except IndexError:
        raise HTTPNotFound

@view_config(route_name='create',renderer='../templates/New.jinja2')
def create_view_page(request):
    """Retruns the new.html as the home page"""
    return {'entry': ENTRY}

@view_config(route_name='update',renderer='../templates/about.jinja2')
def update_view_page(request):
    """Retruns the post.html as the home page"""
    return {'entry': ENTRY}

