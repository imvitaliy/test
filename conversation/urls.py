from rest_framework.routers import Route, SimpleRouter

class CustomRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]
