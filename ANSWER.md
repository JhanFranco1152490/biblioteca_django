# Analisis

En este primer entregable aprendimos a cómo, desde cero, crear un proyecto con Django. Para eso reforzamos el uso de los comandos con django-admin y manage.py.

También creamos los modelos, con los cuales aprendimos a crearles atributos y sobreescribir su método de lectura para reconocerlos más fácilmente cuando los llamemos. También, después de cada cambio en el modelo, realizamos una migración para implementarlo en la base de datos real.

Luego registramos esos modelos en el admin y, gracias a los modelos de admin, pudimos darle más personalización a las vistas de estas tablas. En esta vista pudimos realizar el CRUD exitosamente con los modelos que creamos.

Después creamos un script para poder poblar los datos de las tablas cada vez que queramos, con unos datos por defecto.

Por último, creamos validadores para los modelos, los cuales nos permitían crear condiciones más complejas a los parámetros que vienen por defecto en los Fields(). Muchas de estos parámetros o validadores ya están implementados en Django, pero crearlos nosotros mismos nos permite entender cómo funcionan.