from django.contrib      import admin
from .models.user        import User
from .models.post        import Article
from .models.comunidad   import Comunidad
from .models.clase       import Clase


# Register your models here.
admin.site.register(User)
admin.site.register(Clase)
admin.site.register(Article)
admin.site.register(Comunidad)