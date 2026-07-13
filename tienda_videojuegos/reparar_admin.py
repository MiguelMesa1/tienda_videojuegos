import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path


BASE_DATOS = Path("db.sqlite3")

if not BASE_DATOS.exists():
    raise FileNotFoundError(
        f"No se encontró {BASE_DATOS.resolve()}"
    )

fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
RESPALDO = Path(f"db_respaldo_{fecha}.sqlite3")

shutil.copy2(BASE_DATOS, RESPALDO)

print(f"Respaldo creado: {RESPALDO}")

conexion = sqlite3.connect(BASE_DATOS)
cursor = conexion.cursor()

tablas = [
    fila[0]
    for fila in cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        """
    ).fetchall()
]

referencias = []

for tabla in tablas:
    nombre_seguro = tabla.replace('"', '""')

    claves_foraneas = cursor.execute(
        f'PRAGMA foreign_key_list("{nombre_seguro}")'
    ).fetchall()

    for clave in claves_foraneas:
        tabla_referenciada = clave[2]

        if tabla_referenciada == "auth_user":
            referencias.append(
                (
                    tabla,
                    clave[3],
                    clave[4],
                )
            )

print("\nReferencias existentes a auth_user:")

if referencias:
    for tabla, columna, columna_destino in referencias:
        print(
            f"- {tabla}.{columna} "
            f"-> auth_user.{columna_destino}"
        )
else:
    print("- Ninguna")

# Estas referencias son normales en la instalación antigua.
tablas_permitidas = {
    "django_admin_log",
    "auth_user_groups",
    "auth_user_user_permissions",
}

referencias_peligrosas = [
    referencia
    for referencia in referencias
    if referencia[0] not in tablas_permitidas
]

if referencias_peligrosas:
    print(
        "\nNo se hicieron cambios porque existen tablas "
        "de tu aplicación que utilizan auth_user."
    )
    conexion.close()
    sys.exit(1)

try:
    cursor.execute("BEGIN")

    # Se reconstruirá con la referencia correcta a usuarios.Usuario.
    cursor.execute(
        "DROP TABLE IF EXISTS django_admin_log"
    )

    eliminadas = cursor.execute(
        """
        DELETE FROM django_migrations
        WHERE app = 'admin'
        """
    ).rowcount

    conexion.commit()

    print(
        f"\nRegistros de migración de admin eliminados: "
        f"{eliminadas}"
    )
    print("La reparación inicial terminó correctamente.")

except Exception:
    conexion.rollback()
    raise

finally:
    conexion.close()