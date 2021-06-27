import os, time

from django.conf import settings


def upload_handle(instance, filename):
    dir = settings.MEDIA_ROOT + '/' + instance.__class__.__name__.lower() + 'f'
    if not os.path.exists(dir):
        os.mkdir(dir)
    ext = filename.find('.') and '.%s' % os.path.basename(filename).split('.', 1)[1] or ''
    return '/'.join([instance.__class__.__name__.lower() + 'f', str(int(time.time())) + ext])
