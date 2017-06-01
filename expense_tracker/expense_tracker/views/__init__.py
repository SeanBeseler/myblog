from .default import list_view_page, create_view_page, update_view_page, detail_view_page

def includeme(config):
    config.add_view(list_view_page, route_name ='home')
    config.add_view(detail_view_page, route_name ='detail')
    config.add_view(create_view_page, route_name ='create')
    config.add_view(update_view_page, route_name ='update')





#def main(global_config, **settings):
#    config.include('.views')
#    config.scan()
#    return config.make_wsgi_app()
