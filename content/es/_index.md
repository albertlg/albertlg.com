---
title: ''
summary: 'Albert López Gálvez — Consultor SEO, Content Marketing e IA (LLMs). Blog personal con reflexiones sobre posicionamiento web, estrategia de contenidos y tecnología.'
seo:
  title: 'Albert López — Consultor SEO, Content Marketing e IA | albertlg.com'
date: 2024-01-01
type: landing

design:
  spacing: '5rem'

sections:
  # 1 — Hero
  - block: hero
    content:
      title: "Albert L.G. - Experto SEO, Content Marketing e IA"
      text: "🔎 No se encuentra nada si no se busca algo.<br>Yo soy **Albert López Gálvez** y tú no."
      primary_action:
        text: Leer el blog
        url: /post/
      secondary_action:
        text: Contacto
        url: /contacto/
    design:
      background:
        image:
          filename: herobg.jpg
          filters:
            brightness: 0.31
          parallax: true
          size: cover
          position: bottom
      css_class: dark

  # 2 — Posts
  - block: collection
    id: posts
    content:
      title: Artículos recientes
      subtitle: Lo último que he escrito
      page_type: post
      count: 6
      offset: 0
      order: desc
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
    design:
      view: article-grid
      columns: 3
      fill_image: true

  # 3 — Tag Cloud
  - block: tag-cloud
    id: tags
    content:
      title: "Temas populares"
      subtitle: "Basado en los tags de mis posts"
  # 4 — Bio
  - block: resume-biography-3
    id: about
    content:
      username: admin
      text: |
        Allá por 1998 me topé con Internet mientras estudiaba ingeniería informática, y en el año 2000 su efecto ya me tenía trabajando en ello. He sido diseñador, maquetador, programador, especialista en usabilidad, SEO, emprendedor, directivo, mentor, consultor… Total, que seguramente haya participado al 99% de todo lo que abarca un negocio en internet, y siempre con pasión, entusiasmo y EQUIPO!

        A lo largo de mi carrera he tenido la suerte de poder rodearme de gente mejor que yo y, gracias a una incesante curiosidad y eterna sed de aprender, siempre me han movido lo nuevo, lo inexplorado, la optimización y la medición, y en especial la experiencia de usuario y el posicionamiento de contenidos para convertir.

        Por el momento, he trabajado en Solostocks (Grupo Intercom), Softonic, Uvinum (marca de la que fui orgulloso creador y co-fundador), Drinks&Co Marketplace, y he colaborado con muuuuchas startups. Recientemente he estado implicado en CryptoAdvisor.club y he buceado en el nuevo mundo cripto (criptomonedas, criptoactivos, NFTs, Web3, metaverso, DeFi, etc).

        Hoy, mi aventura profesional continúa evolucionando. Desde 2022 he unido mi experiencia a la eclosión de la IA (inteligencia artificial), y entré como socio y SEO Manager de Mindset Digital, la agencia boutique de crecimiento digital en Barcelona. Junto a Hugo Palomar y equipo (Iván González, Jordi Gost…), estamos expandiendo los horizontes del marketing y la presencia digital gracias al SEO para LLMs. Y por si fuera poco, también estoy inmerso en varios 'side projects' que prometen ser emocionantes. Entre ellos se encuentran VinomadaWine (con Juan Manuel Gonzalvo), Logoteo, TheHowlerMonkeys.club y LeGoodAnfitrión, una app móvil que estamos desarrollando con gran entusiasmo.

        Siempre en movimiento, buscando constantemente nuevas oportunidades y desafíos que me permitan seguir creciendo y aprendiendo en este mundo digital tan dinámico. Si buscas innovación, creatividad y experiencia, ¡aquí me tienes!

        Encuéntrame si buscas algo.
      headings:
        about: Sobre mí
        education: Formación
        interests: Intereses

  # 5 — Experience
  - block: resume-experience
    id: experience
    content:
      title: Experiencia laboral
      subtitle: Mi carrera (o parte de ella)
      username: admin
    design:
      experience_limit: 4
      show_education: false

  # 6 — Skills
  - block: features
    id: skills
    content:
      title: "Habilidades"
      subtitle: "Cómo me defino (o me definen)"
      items:
        - icon: hero/hand-raised
          name: Tenaz
          description: "101%"
        - icon: hero/sparkles
          name: Orientado al detalle
          description: "99,99%"
        - icon: hero/face-smile
          name: Actitud convivial
          description: "98%"
        - icon: hero/user-group
          name: Compromiso con el equipo
          description: "99%"
        - icon: hero/academic-cap
          name: Aprendizaje
          description: "10%"
        - icon: hero/globe-europe-africa
          name: Amigable con el medio ambiente
          description: "80%"
        - icon: hero/cake
          name: Gastrónomo
          description: "100%"
        - icon: hero/musical-note
          name: Música
          description: "78%"
        - icon: hero/camera
          name: Fotografía
          description: "42,8%"

  # 7 — Contact
  - block: contact-cta
    id: contact
    content:
      title: "¿Hablamos?"
      text: "Si quieres comentar un proyecto de SEO, contenidos o IA, escríbeme."
      buttons:
        - text: Escríbeme
          url: /contacto/
        - text: LinkedIn
          url: https://www.linkedin.com/in/albertlg/

---
