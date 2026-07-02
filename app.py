import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.*)', 'controllers.ver_contacto.VerContacto',
    '/insertar_contacto', 'InsertarContacto',
    '/ver_contacto', 'VerContacto',
    '/editar_contacto', 'EditarContacto',
    '/borrar_contacto', 'BorrarContacto'
)

app = web.application(urls, globals())
render = web.template.render('views')


class EditarContacto:
    def GET(self):
        return render.editar_contacto()


class BorrarContacto:
    def GET(self):
        return render.borrar_contacto()


if __name__ == "__main__":
    app.run()