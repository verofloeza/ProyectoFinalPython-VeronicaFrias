# Proyecto: Sistema de Solicitudes de Reparaciones

## Descripción
Esta aplicación está diseñada para gestionar servicios de reparaciones. Permite a los usuarios registrar, gestionar y buscar solicitudes de reparaciones, así como administrar roles y usuarios relacionados con el sistema.

---

## Funcionalidades Principales

1. **Inicio de Sesión (Login):**
   - En la raíz del proyecto (`/`) se muestra la bienvenida al proyecto.

2. **Sobre Mí:**
   - Accediendo a la ruta `/about/` se puede encontrar información sobre mi trayectoria en esta carrera.

3. **Gestión de Usuarios:**
   - Accediendo a la ruta `/accounts/login` se puede iniciar sesión con usuario y contraseña.
   - Accediendo a la ruta `/accounts/register` se puede registrar un nuevo usuario.
   - Una vez registrado o iniciado sesión, se redirige a la página `/accounts/profile`, donde se puede ver toda la información del usuario. (También se puede acceder desde el menú de la derecha donde aparece el nombre del usuario).
   - Accediendo a la ruta `/accounts/edit-profile` se puede editar el perfil añadiendo más información personal y una imagen. (También se puede acceder desde el menú de la derecha donde aparece el nombre del usuario).
   - En el menú de la derecha se encuentra la opción de cerrar sesión, que realiza el logout.

4. **Gestión de Solicitudes de Repuestos:**
   - Este módulo permite visualizar todas las solicitudes realizadas y realizar operaciones CRUD:
     - **Crear:** Registrar nuevas solicitudes.
     - **Leer:** Consultar las solicitudes existentes.
     - **Actualizar:** Modificar la información de una solicitud.
     - **Eliminar:** Eliminar solicitudes innecesarias.

5. **Búsqueda Avanzada en Solicitudes de Repuestos:**
   - Permite buscar solicitudes específicas utilizando los siguientes filtros:
     - **Por Título y Descripción:** Encuentra solicitudes que coincidan con palabras clave.
     - **Por Fecha:** Filtra solicitudes realizadas en un rango de fechas específico.



