# -*- coding: utf-8 -*-
"""Données des slides : Module 1 — Liminaires & Partie 1 (Introduction)."""

SLIDES_INTRO = [
    # SLIDE 1 : COUVERTURE OFFICIELLE (Gérée spécifiquement dans le builder)
    {
        "type": "cover",
        "title": "Ma couronne, mes règles",
        "subtitle": "Le guide complet des cheveux texturés en Afrique",
        "tagline": "Comprendre ses cheveux, préserver sa longueur et en prendre soin avec ce qu'on a dans sa cuisine.",
        "author": "Édition Complète — Bénin & Afrique de l'Ouest",
        "date": "Octobre 2026",
        "image": "cover_crop.png"
    },

    # SLIDE 2 : FICHE D'IDENTITÉ & CONTEXTE LOCAL
    {
        "type": "two_card",
        "tracker": "Cadre & Contexte de l'ouvrage",
        "title": "Un guide pensé pour nos réalités quotidiennes",
        "subtitle": "Parce qu'un conseil inapplicable au marché de Dantokpa ou de Ganhi ne sert à rien.",
        "card1": {
            "title": "Les réalités béninoises au cœur du livre",
            "accent": "terra",
            "paragraphs": [
                ("Le climat sahélien & côtier :", "L'harmattan assèche la fibre en quelques heures ; l'humidité côtière ouvre la cuticule. Nos soins s'adaptent au calendrier réel."),
                ("L'eau locale du robinet et de forage :", "Très calcaire et minéralisée, elle dépose un voile invisible qui bloque l'hydratation. Nous enseignons le rinçage acide neutralisant."),
                ("Des ingrédients à portée de main :", "Tout se trouve au marché de quartier ou dans les étals de Dantokpa, Ganhi et Ouando : karité brut du Nord, huile de coco fraîche, gombo, miel sauvage, savon noir local.")
            ]
        },
        "card2": {
            "title": "L'accessibilité financière absolue",
            "accent": "indigo",
            "paragraphs": [
                ("Zéro ruine en cosmétiques importés :", "Prendre soin de ses cheveux naturels ne doit pas coûter 40 000 FCFA par mois en gammes américaines ou européennes formulées pour d'autres climats."),
                ("Un panier de départ à moins de 3 000 FCFA :", "Avec cinq ingrédients de base achetés au marché pour 3 000 FCFA, vous avez de quoi réaliser trois mois complets de soins hebdomadaires."),
                ("Un ton bienveillant et complice :", "Le vouvoiement chaleureux est la règle : nous partageons une expérience vécue, sans culpabilisation, avec des encadrés de confidences.")
            ]
        },
        "callout": "Ce livre n'est pas un luxe : c'est un manuel d'autonomie pour que chaque femme devienne l'experte de sa propre couronne."
    },

    # SLIDE 3 : ÉDITO — POURQUOI CE GUIDE EXISTE
    {
        "type": "two_card",
        "tracker": "Avant-propos de l'autrice",
        "title": "Pourquoi ce guide existe (et ce qui le rend unique)",
        "subtitle": "Rompre avec les recettes floues trouvées sur Internet qui abîment les cheveux.",
        "card1": {
            "title": "Les 3 questions auxquelles personne ne répond",
            "accent": "gold",
            "paragraphs": [
                ("1. POURQUOI ça marche ?", "On vous dit « mettez de l'avocat et de l'huile ». Mais que fait le gras ? Que fait l'eau ? Nous expliquons la chimie simple de chaque geste."),
                ("2. COMBIEN exactement ?", "Fini le vague « un peu d'huile ». Chaque recette indique la dose en cuillères à café, cuillères à soupe, verres ou noisettes, selon la longueur de vos cheveux."),
                ("3. À QUELLE FRÉQUENCE ?", "Le secret d'un cheveu qui s'épanouit n'est pas le produit miracle, c'est le tempo. Nous donnons le calendrier précis : hebdomadaire, bimensuel ou mensuel.")
            ]
        },
        "card2": {
            "title": "Le piège de la fausse paresse",
            "accent": "green",
            "paragraphs": [
                ("La paresse n'est pas un défaut moral :", "C'est souvent le signe d'une routine trop lourde, trop compliquée ou décevante. Quand une routine prend 4 heures pour un résultat médiocre, on abandonne."),
                ("Le minimalisme efficace :", "Ce livre propose des gestes de 2 à 15 minutes. Deux gestes bien ciblés valent mille fois mieux qu'un rituel épuisant abandonné au bout de 15 jours."),
                ("La règle des 80 / 20 :", "80 % de la santé de vos cheveux dépend de 3 gestes : hydrater à l'eau, sceller au karité, et protéger les pointes la nuit.")
            ]
        },
        "callout": "La simplicité régulière bat toujours la complexité intermittente. Vous n'avez pas besoin de courage : vous avez besoin d'une méthode."
    },

    # SLIDE 4 : LES TROIS VÉRITÉS DU CHEVEU TEXTURÉ
    {
        "type": "three_card",
        "tracker": "Fondations scientifiques",
        "title": "Les trois vérités incontournables sur nos cheveux",
        "subtitle": "Comprendre ces trois lois biologiques change à jamais votre rapport à votre chevelure.",
        "col1": {
            "title": "1. Le cheveu pousse toujours",
            "accent": "indigo",
            "body": [
                "Biologiquement, le cheveu texturé pousse de 0,8 à 1,25 cm par mois (soit environ 12 à 15 cm par an).",
                "Si vos cheveux semblent stagner depuis des années, ce n'est PAS un problème de pousse : vos pointes se cassent au même rythme que vos racines poussent.",
                "Le but de ce livre n'est pas de faire pousser miraculeusement, mais de CONSERVER la longueur acquise."
            ]
        },
        "col2": {
            "title": "2. C'est une matière morte",
            "accent": "terra",
            "body": [
                "La tige capillaire qui sort de votre crâne est constituée de kératine morte : aucun produit au monde ne peut la « nourrir » au sens biologique.",
                "On ne nourrit pas un cheveu : on le lave, on l'hydrate avec de l'eau, on le gaine avec des lipides pour retenir cette eau, et on évite de le briser.",
                "La seule vraie nourriture du cheveu passe par vos vaisseaux sanguins et votre assiette."
            ]
        },
        "col3": {
            "title": "3. Moins c'est mieux",
            "accent": "green",
            "body": [
                "L'accumulation frénétique de crèmes, beurres, sérums et huiles étouffe la cuticule et attire la poussière.",
                "Un cheveu saturé de gras devient poisseux, imperméable à l'eau, et finit par casser de l'intérieur.",
                "Trois ingrédients bien choisis dans votre cuisine suffisent pour bâtir la chevelure de vos rêves."
            ]
        },
        "callout": "Retenez cette équation d'or : Santé capillaire = Pousse naturelle (génétique + alimentation) MOINS la Casse (frottements + sécheresse + manipulation)."
    },

    # SLIDE 5 : SYSTÈME DE PREUVE & REPÈRES
    {
        "type": "two_card",
        "tracker": "Méthodologie & Charte d'honnêteté",
        "title": "Comment lire ce livre : nos badges de preuve",
        "subtitle": "Une transparence scientifique totale pour distinguer le prouvé, le prometteur et la tradition.",
        "card1": {
            "title": "Les trois niveaux de preuve scientifique",
            "accent": "indigo",
            "paragraphs": [
                ("● ÉTAYÉ (Études humaines publiées) :", "Bénéfice prouvé en laboratoire et sur l'humain. Exemple : l'huile de coco qui pénètre la fibre et réduit la perte de protéines de près de 40 % (étude Rele & Mohile, 2003)."),
                ("◐ PROMETTEUR (Études préliminaires) :", "Mécanisme scientifiquement plausible ou études cliniques sur petits échantillons non encore répliquées. Exemple : l'action stimulante de l'huile essentielle de romarin."),
                ("○ TRADITION (Usage séculaire éprouvé) :", "Pratique ancestrale africaine documentée depuis des siècles, efficace sur le terrain mais n'ayant pas fait l'objet d'essais cliniques formels. Exemple : le gel de gombo.")
            ]
        },
        "card2": {
            "title": "Les 4 pictogrammes universels",
            "accent": "gold",
            "paragraphs": [
                ("QUANTITÉ EXACTE :", "Toujours exprimée en ustensiles simples (cuillère à café = 5 ml, cuillère à soupe = 15 ml, verre = 250 ml, noisette ou noix)."),
                ("TEMPS DE POSE :", "La durée exacte pour que l'actif agisse sans saturer ou faire gonfler la cuticule inutilement."),
                ("FRÉQUENCE :", "Le rythme hebdomadaire, bimensuel ou mensuel indispensable pour obtenir un résultat visible et durable."),
                ("Attention : ATTENTION :", "La contre-indication, le risque d'allergie ou la mauvaise pratique qui ruine les bienfaits de l'ingrédient.")
            ]
        },
        "callout": "Chaque fiche ingrédient et chaque astuce du livre affiche clairement son badge et ses repères. Vous savez exactement où vous mettez les pieds."
    },

    # SLIDE 6 : GRAND SOMMAIRE DE L'OUVRAGE
    {
        "type": "four_boxes",
        "tracker": "Table des matières complète",
        "title": "L'architecture globale de l'ouvrage en 4 parties",
        "subtitle": "Un parcours logique en 4 étapes progressives complété par une boîte à outils pratique.",
        "box1": ("PARTIE 1 — INTRODUCTION", "La couronne & l'identité", "Histoire culturelle de la chevelure en Afrique · L'anatomie de la fibre en spirale · Pourquoi nos cheveux cassent · Le climat béninois : harmattan, eau calcaire de forage · Ce que ce livre est et ne fera pas."),
        "box2": ("PARTIE 2 — DÉVELOPPEMENT", "Diagnostic & Cuisine", "Typologie du 2A au 4C · Les 3 vrais tests de porosité · Bilan élasticité protéines/humidité · Fiche diagnostic · La pharmacie de la cuisine : 25 ingrédients décortiqués · Le tableau maître · Les 8 faux amis."),
        "box3": ("PARTIE 3 — ASTUCES & SOINS", "Routines & L'Assiette", "Le rythme de la semaine (15 min, 45 min, 1h30) · Laver sans casser · Démêler en 4 sections · La méthode LCO · L'Assiette Cheveux (nutrition & fer) · Garder ce qui pousse · Le Kit Anti-Paresse (défis & checklists)."),
        "box4": ("PARTIE 4 — TRESSES PROTECTRICES", "Héritage & Préservation", "La science des coiffures protectrices · 31,7 % d'alopécie de traction : chiffres & prévention · Catalogue de 12 coiffures avec scores de risque · Protocole J-7 à J+30 · Fiche à remettre à la coiffeuse · Boîte à outils.")
    },

    # SLIDE 7 : INTERTITRE PARTIE 1
    {
        "type": "divider",
        "part_num": "PREMIÈRE PARTIE",
        "title": "La Couronne & l'Identité",
        "quote": "« Les cheveux sont la gloire de la femme. Comprendre sa couronne, c'est reprendre le pouvoir sur elle sans jamais la dénaturer. »",
        "subtitle": "Redécouvrir la beauté, l'histoire et la biologie singulière de notre chevelure texturée."
    },

    # SLIDE 8 : « LES CHEVEUX, LA GLOIRE DE LA FEMME »
    {
        "type": "two_card",
        "tracker": "Partie 1 · Chapitre 1 — Signification culturelle",
        "title": "« Les cheveux, la gloire de la femme » : histoire et société",
        "subtitle": "En Afrique de l'Ouest, la chevelure n'est jamais neutre : elle est un langage social vivant.",
        "card1": {
            "title": "Un langage social codé et puissant",
            "accent": "terra",
            "paragraphs": [
                ("La royauté et le rang social :", "Dans les royaumes du Danxomè et en pays yoruba, la forme des tresses, le dessin des raies et les parures indiquaient la royauté, l'appartenance clanique ou le célibat."),
                ("Les étapes majeures de la vie :", "La coiffure accompagnait les rites de passage : virginité, mariage, maternité, veuvage. Les cheveux étaient le réceptacle de la force vitale spirituelle."),
                ("Une mémoire transmise de mère en fille :", "Les séances de coiffage sur le pas de la porte étaient des moments de transmission orale, de complicité intergénérationnelle et de confidences intimes.")
            ]
        },
        "card2": {
            "title": "La double pression contemporaine",
            "accent": "indigo",
            "paragraphs": [
                ("L'injonction contradictoire :", "« Sois naturelle et fière de tes racines », mais « aie des cheveux disciplinés, lisses et sans volume au bureau ou à l'église »."),
                ("Le mythe du cheveu « dur » ou « difficile » :", "Nos cheveux ne sont pas durs : ils ont simplement soif. Dès qu'ils reçoivent l'eau et les lipides dont ils ont besoin, ils deviennent souples comme du velours."),
                ("Prendre soin de soi n'est pas de la vanité :", "Consacrer dix minutes à hydrater sa chevelure est un acte d'estime de soi, de respect de sa santé et d'affirmation culturelle.")
            ]
        },
        "callout": "Vos cheveux ne sont pas un problème à corriger. C'est une couronne vivante qui attend simplement d'être comprise et respectée."
    },

    # SLIDE 9 : L'ANATOMIE EN SPIRALE DU CHEVEU TEXTURÉ
    {
        "type": "two_card",
        "tracker": "Partie 1 · Chapitre 2 — Biologie du cheveu texturé",
        "title": "L'anatomie de la fibre en spirale : pourquoi elle casse",
        "subtitle": "La forme elliptique et torsadée explique pourquoi nos cheveux ont des besoins uniques.",
        "card1": {
            "title": "Le mystère du sébum qui ne descend pas",
            "accent": "gold",
            "paragraphs": [
                ("Le follicule incurvé en crosse de golf :", "Contrairement au cheveu asiatique ou caucasien qui pousse droit d'un follicule rond, le cheveu afro pousse d'un follicule incliné et courbé."),
                ("La forme de ruban torsadé :", "La fibre ressemble à un ressort ou un ruban qui tourne sur lui-même. Chaque virage de la boucle crée un point de torsion mécanique très vulnérable."),
                ("La barrière du sébum :", "Le sébum produit par le cuir chevelu glisse facilement sur une tige droite. Sur une spirale 4C serrée, il reste bloqué aux racines : les longueurs et pointes restent sèches par nature.")
            ]
        },
        "card2": {
            "title": "Les trois couches de la tige capillaire",
            "accent": "indigo",
            "paragraphs": [
                ("1. La cuticule (l'armure protectrice) :", "Formée d'écailles de kératine superposées comme les tuiles d'un toit. Si les écailles sont fermées, le cheveu retient l'eau et brille. Si elles sont ouvertes, l'eau s'échappe."),
                ("2. Le cortex (le cœur et la force) :", "Constitue 85 % de la fibre. Contient les chaînes de kératine hélicoïdales et la mélanine. C'est lui qui donne au cheveu son élasticité et sa couleur."),
                ("3. La moelle (le canal central) :", "Parfois absente chez les cheveux très fins. Elle n'a pas de rôle mécanique direct mais participe au volume.")
            ]
        },
        "callout": "Le cheveu crépu n'est pas fragile par faiblesse génétique : il est vulnérable parce que sa géométrie en ressort l'expose aux frottements et à la sécheresse."
    },

    # SLIDE 10 : LE CLIMAT BÉNINOIS ET NOS CHEVEUX
    {
        "type": "two_card",
        "tracker": "Partie 1 · Chapitre 3 — Facteurs environnementaux",
        "title": "L'impact du climat ouest-africain sur la fibre capillaire",
        "subtitle": "Harmattan, humidité équatoriale et eau de forage : les trois défis du quotidien béninois.",
        "card1": {
            "title": "L'Harmattan et la saison sèche (Décembre - Février)",
            "accent": "terra",
            "paragraphs": [
                ("Le vent du désert :", "L'harmattan apporte un vent sec chargé de micro-poussières de silice. L'humidité de l'air tombe en dessous de 20 % : le cheveu perd toute son eau par évaporation directe."),
                ("L'effet « paille cassante » :", "Sans protection occlusive lourde (beurre de karité brut), les cuticules se soulèvent et la tige se brise au moindre coup de peigne."),
                ("La poussière abrasive :", "La poussière s'infiltre dans les spirales et agit comme du papier de verre lors du brossage. D'où la nécessité de protéger les cheveux sous des foulards en satin.")
            ]
        },
        "card2": {
            "title": "L'eau dure de forage et de robinet",
            "accent": "green",
            "paragraphs": [
                ("Une eau chargée en calcium et magnésium :", "Dans la plupart des quartiers de Cotonou, Calavi, Porto-Novo ou Parakou, l'eau de pompe ou de forage est très dure (fortement minéralisée)."),
                ("Le piège du dépôt invisible :", "Les sels minéraux insolubles se déposent sur les écailles des cheveux. Ils forment un film rigide et terne qui empêche les masques et l'eau de pénétrer."),
                ("La solution souveraine : le rinçage acide :", "Une seule cuillère à soupe de vinaigre de cidre dans un grand verre d'eau tiède dissout instantanément ces dépôts calcaires et lisse la fibre.")
            ]
        },
        "callout": "Adapter ses soins à la saison et neutraliser le calcaire de l'eau locale règle à lui seul la moitié des problèmes de cheveux ternes et cassants."
    },

    # SLIDE 11 : CE QUE CE LIVRE EST / CE QU'IL NE FERA JAMAIS
    {
        "type": "two_card",
        "tracker": "Partie 1 · Chapitre 4 — Contrat de confiance",
        "title": "Ce que ce livre est / Ce qu'il ne fera jamais",
        "subtitle": "Notre engagement d'honnêteté et de respect absolu de votre intelligence.",
        "card1": {
            "title": "Ce qu'il ne fera JAMAIS",
            "accent": "terra",
            "paragraphs": [
                ("Pas de promesse de pousse éclair :", "Nous ne vous dirons jamais que l'huile de ricin fait pousser de 10 cm en trois semaines. La biologie ne ment pas."),
                ("Pas de gammes à acheter :", "Aucune marque de cosmétique sponsorisée, aucun flacon coûteux introuvable à Cotonou. Votre supermarché, c'est votre cuisine et votre marché."),
                ("Pas de diabolisation des tresses :", "Les nattes et tresses africaines sont un art magnifique. Nous ne vous disons pas d'arrêter : nous vous apprenons à les porter sans perdre votre lisière."),
                ("Pas de routines de 4 heures :", "Nous refusons les protocoles en 12 étapes qui épuisent les mères de famille et les femmes actives.")
            ]
        },
        "card2": {
            "title": "Ce qu'il est VRAIMENT",
            "accent": "indigo",
            "paragraphs": [
                ("Un guide d'autonomie pratique :", "25 ingrédients locaux décortiqués avec précision : pourquoi ça marche, quelle quantité exacte, quelle fréquence."),
                ("Un remède à la paresse :", "Le Kit Anti-Paresse intégré vous donne le minimum vital qui fonctionne quand vous êtes fatiguée ou débordée."),
                ("Une méthode validée pour conserver sa longueur :", "Apprendre à démêler sans arracher, sceller sans graisser, et laver sans décaper."),
                ("Un support à annoter et corriger :", "Ce livre vous appartient. Notez vos observations, adaptez les dosages et faites-en votre manuel personnel.")
            ]
        },
        "callout": "Vous avez désormais entre les mains un outil de liberté. Entrons maintenant dans la pratique et le diagnostic de votre chevelure."
    }
]
print("slides_data_intro.py défini avec succès :", len(SLIDES_INTRO), "slides")
