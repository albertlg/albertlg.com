# Plan: Mejoras Homepage Hugo Blox

## Contexto

Tras la migración inicial a Hugo Blox (rama `migration/hugo-blox`), la homepage compila pero le faltan secciones y elementos visualales del tema anterior. Este plan añade todo lo que falta y ajusta el diseño.

---

## Paso 0: Guardar este plan

Copiar este plan a `docs/plans/homepage-improvements.md` para documentación del proyecto.

---

## Paso 1: Assets (logo, favicon)

Copiar archivos a donde Hugo Blox los auto-detecta:

```
cp assets/images/logo.png assets/media/logo.png
cp assets/images/icon-pack/icon.png assets/media/icon.png
```

- `get_logo.html` busca `assets/media/logo.{svg,png}` → navbar mostrará el logo
- `get_site_icon.html` busca `assets/media/icon.{svg,png}` → favicon aparecerá

**Ficheros:** 2 nuevos (`assets/media/logo.png`, `assets/media/icon.png`)

---

## Paso 2: Custom tag-cloud block

Crear `layouts/_partials/hbx/blocks/tag-cloud/block.html`

Hugo Blox busca bloques en esa ruta. El template itera `site.Taxonomies.tags`, escala font-size logarítmicamente por conteo, y usa clases Tailwind del tema.

Parámetros YAML: `content.title`, `content.subtitle`

**Ficheros:** 1 nuevo

---

## Paso 3: Override contact-info para Netlify Forms

Crear `layouts/_partials/hbx/blocks/contact-info/block.html` copiando el original del módulo y añadiendo `data-netlify="true"` al `<form>`.

**Ficheros:** 1 nuevo (override)

---

## Paso 4: Reestructurar `content/es/_index.md`

Secciones en orden:

### 4.1 — `hero` block
- `content.title`: "Albert L.G. en la red..."
- `content.text`: "🔎 No se encuentra nada si no se busca algo.\nYo soy **Albert López Gálvez** y tú no."
- `design.background.image.filename`: herobg.jpg (con brightness 0.31, parallax, position bottom)
- `design.css_class`: dark

### 4.2 — `resume-biography-3` block
- `content.username`: admin
- Bio completa en `content.text`
- Headings: Sobre mí / Formación / Intereses
- SIN background image (se movió al hero)

### 4.3 — `resume-experience` block
- `content.username`: admin (lee `experience[]` de `data/authors/admin.yaml`)
- Timeline con 7 puestos de trabajo + 1 formación
- Hugo Blox traduce automáticamente los encabezados via i18n

### 4.4 — `features` block (Skills 3x3)
- `content.title`: "Habilidades"
- `content.text`: "Cómo me defino (o me definen)"
- 9 items con Heroicons equivalentes:
  - Tenaz → `hand-raised`
  - Orientado al detalle → `sparkles`
  - Actitud convivial → `face-smile`
  - Compromiso equipo → `user-group`
  - Aprendizaje → `academic-cap`
  - Medio ambiente → `globe-europe-africa`
  - Gastrónomo → `cake`
  - Música → `musical-note`
  - Fotografía → `camera`

### 4.5 — `collection` block (Posts)
- `content.title`: "Artículos recientes"
- `content.subtitle`: "Últimos posts de mi blog (como ves, escribo poco)"
- 4 posts, **list view** (`design.view: date-title-summary`)
- Traducir "Read more": crear `i18n/es.yaml` con `read_more: "Leer más"` y `i18n/ca.yaml` con `read_more: "Llegir més"` (el módulo no incluye estas traducciones)

### 4.6 — `tag-cloud` block
- `content.title`: "Temas populares"
- `content.subtitle`: "Basado en los tags de mis posts"

### 4.7 — `contact-info` block
- `content.title`: "Contacto"
- `content.subtitle`: "Escríbeme... pero aviso: leo ocasionalmente el correo personal"
- `content.email`: albert@albertlg.com
- `content.social[]`: linkedin, x (NO `contact_links` — campo correcto es `social`)
- `content.show_form`: true

---

## Paso 5: Reestructurar `content/en/_index.md`

Misma estructura, textos en inglés:
- Hero: "Albert L.G. online..." / "🔎 Nothing is found if nothing is sought..."
- Experience, Skills, Posts, Tags, Contact — todos traducidos
- Los datos de experience vienen del mismo `admin.yaml` (están en español, pero es aceptable ya que son nombres de empresas y cargos)

---

## Paso 6: Reestructurar `content/ca/_index.md`

Misma estructura, textos en catalán.

---

## Paso 7: Verificar Heroicons disponibles

Antes de implementar, verificar que los nombres de iconos existen en el set Hero del módulo. Si alguno no existe, buscar alternativa.

Ruta de verificación: `blox@v0.11.0/assets/icons/hero/*.svg`

---

## Paso 8: Build y test

```bash
hugo server --disableFastRender
```

Verificar:
- Logo en navbar ✓
- Favicon en pestaña ✓
- Avatar en sección bio ✓
- Hero con H1 + subtítulo + background limitado ✓
- Bio sin background ✓
- Experience timeline ✓
- Skills grid 3x3 con iconos ✓
- Posts con título y subtítulo ✓
- Tag cloud ✓
- Formulario de contacto (submit test) ✓
- Cambio de idioma ES/EN/CA ✓

---

## Resumen de ficheros

| Acción | Fichero |
|--------|---------|
| Copiar | `assets/media/logo.png` (desde `assets/images/logo.png`) |
| Copiar | `assets/media/icon.png` (desde `assets/images/icon-pack/icon.png`) |
| Crear | `layouts/_partials/hbx/blocks/tag-cloud/block.html` |
| Crear | `layouts/_partials/hbx/blocks/contact-info/block.html` (override Netlify Forms) |
| Crear | `i18n/es.yaml` (traducciones: read_more, more_pages) |
| Crear | `i18n/ca.yaml` (traducciones: read_more, more_pages) |
| Copiar | `docs/plans/homepage-improvements.md` (este plan) |
| Modificar | `content/es/_index.md` |
| Modificar | `content/en/_index.md` |
| Modificar | `content/ca/_index.md` |
