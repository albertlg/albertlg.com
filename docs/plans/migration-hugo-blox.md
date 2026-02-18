# Plan: Migración de Hugo Academic v4.8.0 a Hugo Blox Academic CV

## Contexto

El sitio albertlg.com usa el tema Hugo Academic v4.8.0 (vendored en `themes/academic/`), un tema legacy que ya no se mantiene y es incompatible con Hugo moderno sin parches. El objetivo es migrar al sucesor oficial: **Hugo Blox Academic CV**, que usa Hugo Modules en lugar de un tema vendored. El usuario quiere **conservar el tema antiguo** en el repo para referencia.

## Estrategia

Trabajar en una **rama `migration/hugo-blox`** para poder validar incrementalmente sin afectar producción. La migración es fundamentalmente un cambio de sistema de temas (vendored → Hugo Modules) y de formato de configuración (TOML → YAML).

---

## Fases

### Fase 1: Preparación
1. Crear rama `migration/hugo-blox`
2. Inicializar Hugo Modules: `hugo mod init github.com/albertlg/albertlg.com`
3. Crear `config/_default/hugo.yaml` con imports de módulos Hugo Blox
4. Crear `config/_default/params.yaml` mapeando desde `params.toml` actual
5. Crear `config/_default/languages.yaml` (es, en, ca)
6. Crear `config/_default/menus.yaml` (+ `menus.en.yaml`, `menus.ca.yaml`)
7. Renombrar ficheros TOML antiguos a `.toml.old`
8. Renombrar `config.toml` raíz a `config.toml.old`
9. Descargar módulos: `hugo mod get -u && hugo mod tidy`

### Fase 2: Migración de datos de autor
1. Crear `data/authors/admin.yaml` con datos de `content/es/authors/admin/_index.md`
2. Copiar avatar a `assets/media/avatar.jpg`
3. Mantener `content/*/authors/` intacto (referencia)

### Fase 3: Homepage (widgets → bloques)
1. Crear `content/es/_index.md` con bloques Hugo Blox
2. Crear `content/en/_index.md` y `content/ca/_index.md` (traducciones)
3. Renombrar `content/*/home/` a `content/*/home.old/`

### Fase 4: Contenido existente
1. Mantener `content/*/post/` como está
2. Copiar `static/img/herobg.jpg` a `assets/media/`

### Fase 5: Netlify
1. Actualizar `netlify.toml` con `GO_VERSION`
2. Conservar TODOS los redirects existentes

### Fase 6: Validación y limpieza
1. Build completo local
2. Comprobar: homepage, posts, idiomas, URLs existentes
