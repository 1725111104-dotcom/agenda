import web

urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos', 'controllers.lista_contactos.ListaContactos',
    '/ver_contacto/(.*)', 'controllers.ver_contacto.VerContacto',
    '/editar_contacto/(.*)', 'controllers.editar_contacto.EditarContacto',
    '/insertar_contacto', 'InsertarContacto',
    '/borrar_contacto/(.*)', 'controllers.borrar_contacto.BorrarContacto'
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