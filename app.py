import web

urls = (
    '/', 'Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.*)', 'controllers.ver_contacto.VerContacto',
    '/insertar_contacto', 'InsertarContacto',
    '/editar_contacto', 'EditarContacto',
    '/borrar_contacto', 'BorrarContacto'
)

app = web.application(urls, globals())
render = web.template.render('views')


class Index:
    def GET(self):
        return render.index()


class ListaContactos:
    def GET(self):
        return render.lista_contactos()


class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()


class VerContacto:
    def GET(self):
        return render.ver_contacto()


class EditarContacto:
    def GET(self):
        return render.editar_contacto()


class BorrarContacto:
    def GET(self):
        return render.borrar_contacto()


if __name__ == "__main__":
    app.run()
