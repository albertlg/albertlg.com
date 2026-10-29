---
title: ''
summary: 'Albert López Gálvez — Consultor SEO, Content Marketing i IA (LLMs). Blog personal amb reflexions sobre posicionament web, estratègia de continguts i tecnologia.'
seo:
  title: 'Albert López — Consultor SEO, Content Marketing i IA | albertlg.com'
date: 2024-01-01
type: landing

design:
  spacing: '5rem'

sections:
  # 1 — Hero
  - block: hero
    content:
      title: "Albert L.G. - Expert SEO, Content Marketing i IA"
      text: "🔎 No es troba res si no es busca alguna cosa.<br>Jo soc l'**Albert López Gálvez** i tu no."
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

  # 2 — Bio
  - block: resume-biography-3
    id: about
    content:
      username: admin
      text: |
        Cap al 1998 em vaig topar amb Internet mentre estudiava enginyeria informàtica, i a l'any 2000 el seu efecte ja m'hi tenia treballant. He estat dissenyador, maquetador, programador, especialista en usabilitat, SEO, emprenedor, directiu, mentor, consultor... Total, que segurament hagi participat al 99% de tot allò que abasta un negoci a internet, i sempre amb passió, entusiasme i EQUIP!

        Al llarg de la meva carrera he tingut la sort de poder envoltar-me de gent millor que jo i, gràcies a una incessant curiositat i eterna set d'aprendre, sempre m'han mogut allò nou, allò inexplorat, l'optimització i el mesurament, i en especial l'experiència d'usuari i el posicionament de continguts orientat a convertir.

        De moment, he treballat a Solostocks (Grupo Intercom), Softonic, Uvinum (marca de la qual vaig ser orgullós creador i cofundador), Drinks&Co Marketplace, i he col·laborat amb mooooltes startups. Recentment he estat implicat en CryptoAdvisor.club i he aprofundit en el món cripto (criptomonedes, criptoactius, NFTs, Web3, metavers, DeFi, etc.).

        Avui, la meva aventura professional continua evolucionant. Des del 2022 he unit la meva experiència a l'eclosió de la IA, i he entrat com a soci i SEO Manager de Mindset Digital, l'agència boutique de creixement digital a Barcelona. Juntament amb en Hugo Palomar i l'equip (Iván González, Jordi Gost...), estem expandint els horitzons del màrqueting i de la presència digital gràcies al SEO per a LLMs. I, per si no n'hi hagués prou, també estic immers en diversos side projects que prometen ser estimulants: VinomadaWine (amb Juan Manuel Gonzalvo), Logoteo (amb Miquel Pascual) i LeGoodAnfitrión, una aplicació mòbil que estem desenvolupant amb molta il·lusió.

        Sempre en moviment, sempre cercant noves oportunitats i reptes per seguir creixent i aprenent en aquest món digital tan dinàmic. Si busques innovació, creativitat i experiència, aquí em tens!

        Troba'm si busques alguna cosa.
      headings:
        about: Sobre mi
        education: Formació
        interests: Interessos

  # 3 — Experience
  - block: resume-experience
    id: experience
    content:
      title: Experiència laboral i formació
      subtitle: La meva carrera (o part d'ella)
      username: admin

  # 4 — Skills
  - block: features
    id: skills
    content:
      title: "Habilitats"
      subtitle: "Com em defineixo (o em defineixen)"
      items:
        - icon: hero/hand-raised
          name: Tenaç
          description: "101%"
        - icon: hero/sparkles
          name: Orientat al detall
          description: "99,99%"
        - icon: hero/face-smile
          name: Actitud convivial
          description: "98%"
        - icon: hero/user-group
          name: Compromís amb l'equip
          description: "99%"
        - icon: hero/academic-cap
          name: Aprenentatge
          description: "10%"
        - icon: hero/globe-europe-africa
          name: Respectuós amb el medi ambient
          description: "80%"
        - icon: hero/cake
          name: Gastrònom
          description: "100%"
        - icon: hero/musical-note
          name: Música
          description: "78%"
        - icon: hero/camera
          name: Fotografia
          description: "42,8%"

  # 5 — Posts
  - block: collection
    id: posts
    content:
      title: Articles recents
      subtitle: Darrers posts del meu bloc (com pots veure, escric poc sovint)
      page_type: post
      count: 4
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
      columns: 2
      fill_image: true

  # 6 — Tag Cloud
  - block: tag-cloud
    id: tags
    content:
      title: "Temes populars"
      subtitle: "Basat en els tags dels meus posts"

---
