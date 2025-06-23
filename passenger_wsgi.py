import os
import sys

sys.path.insert(0, "/home/dfrpicje/repositories/f3Paulding")
sys.path.insert(0, "/home/dfrpicje/repositories/f3Paulding/f3PauldingWebsite")

os.environ["DJANGO_SETTINGS_MODULE"] = "f3PauldingWebsite.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
