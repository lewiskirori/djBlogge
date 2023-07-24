from django.core.wsgi import get_wsgi_application
from vercel_serverless_sdk import VercelServerlessSdk

sdk = VercelServerlessSdk()

def handler(request):
    application = get_wsgi_application()
    response = sdk.WsgiHandler(application, request)
    return response
