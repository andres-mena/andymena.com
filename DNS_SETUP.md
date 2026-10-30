# andymena.com — acceso y DNS

El correo de confirmación acredita la compra; no reemplaza el acceso a la cuenta del registrador.

## Recuperar acceso a Name.com

1. Abrir `https://www.name.com/` directamente y elegir **Log in**.
2. Si no recordás la contraseña, usar la opción de recuperación de contraseña. Si tampoco recordás el usuario, usar la recuperación de usuario.
3. Usar el correo asociado a la compra. Revisar spam si no llega el mensaje.
4. Después de ingresar, buscar **My Domains** y seleccionar **andymena.com**.
5. Buscar **DNS Records** o **Manage DNS Records**. Si el dominio usa nameservers de otro proveedor, la configuración se administra allí.

No enviar contraseñas, códigos de recuperación ni códigos de verificación por chat. Si el dominio no aparece en la cuenta, contactar al soporte de Name.com con el número de orden que figura en el correo.

La ruta exacta de los menús debe verificarse en la cuenta: no se pudo cargar la documentación de soporte durante la preparación local.

## Cuando el sitio esté listo para publicar

Primero se seleccionará y configurará el hosting. Si usamos GitHub Pages:

1. Verificar la propiedad de `andymena.com` en la cuenta personal de GitHub mediante el registro TXT que indique GitHub.
2. Crear/configurar el repositorio y Pages, desplegando únicamente `site/`.
3. Configurar `andymena.com` como dominio personalizado en Pages.
4. Agregar los registros A del dominio raíz y el CNAME de `www` que indique la documentación vigente de GitHub Pages.
5. Mantener los registros de correo MX/TXT existentes. Revisar conflictos antes de sustituir registros web.
6. Esperar la validación y habilitar HTTPS; comprobar el dominio raíz y `www`.

Los valores exactos de DNS se determinarán cuando exista el hosting. No hace falta comprar hosting adicional para preparar el sitio ni modificar registros ahora.
