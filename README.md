# ckanext-dge-drupal-users

`ckanext-dge-drupal-users` es una extensión para CKAN utilizada en la plataforma [datos.gob.es](https://datos.gob.es/) para delegar la autenticación/integración de usuarios en Drupal.

> [!TIP]
> Guía base y contexto del proyecto: https://github.com/datosgobes/datos.gob.es

## Descripción general

- Proporciona un plugin CKAN para integración de usuarios con Drupal.

## Requisitos

### Compatibilidad

Compatibilidad con versiones de CKAN:

| Versión de CKAN | ¿Compatible?                                                              |
|--------------|-----------------------------------------------------------------------------|
| 2.8          | ❌ No (requiere Python 3+)                                                   |
| 2.9          | ✅ Sí                                                                        |
| 2.10         | ❓ Desconocido                                                               |
| 2.11         | ❓ Desconocido                                                               |


### Dependencias

- Una instancia de CKAN.
- Dependencias Python adicionales:

```sh
pip install -r requirements.txt
```

## Instalación

```sh
pip install -e .
```

## Configuración

Activa el plugin en tu configuración de CKAN:

```ini
ckan.plugins = … dge_drupal_users
```

### Plugins

- `dge_drupal_users`

### Ejemplo de activación (datos.gob.es)

La documentación operativa de la plataforma (ver [Documentacion CKAN.md](https://github.com/datosgobes/datos.gob.es/blob/master/docs/202512_datosgobes-ckan-doc_es.pdf), sección 3.11) muestra una activación conjunta típica de extensiones:

```ini
ckan.plugins = dge_brokenlinks dge dge_dashboard dge_ga_report dge_ga dcat
dge_harvest dge_nti_rdf_harvester dge_dcat_ap_es_rdf_harvester harvest fluent
scheming_datasets dge_dataservice dge_scheming stats report comments
dge_drupal_users
```

### Ajustes de integración con Drupal

Ejemplo de configuración:

```ini
ckanext.dge_drupal_users.domain = ENV_DOMAIN
ckanext.dge_drupal_users.connection = mysql://MYSQL_USERNAME:MYSQL_PASSWORD@MYSQL_HOST/drupal
```

## Licencia

Este proyecto se distribuye bajo licencia **GNU Affero General Public License (AGPL) v3.0 o posterior**. Consulta el fichero [LICENSE](LICENSE).
