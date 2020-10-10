#!/usr/bin/env python

from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
# from wagtail.exhibitions.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet



# Create the router. "wagtailapi" is the URL namespace
from home.views import MediaAPIViewSet, ImagesAPIViewSet

api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, exhibitions). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
api_router.register_endpoint('exhibitions', ImagesAPIViewSet)
api_router.register_endpoint('media', MediaAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
