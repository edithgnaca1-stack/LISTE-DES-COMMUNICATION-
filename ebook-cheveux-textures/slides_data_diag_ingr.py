# -*- coding: utf-8 -*-
"""Données des slides : Module 2 — Diagnostic & Les 25 Ingrédients de la Cuisine."""

SLIDES_DIAG_INGR = [
    # SLIDE 12 : INTERTITRE PARTIE 2
    {
        "type": "divider",
        "part_num": "DEUXIÈME PARTIE",
        "title": "Connaître ses cheveux & La pharmacie de la cuisine",
        "quote": "« On ne soigne pas ce qu'on ne comprend pas. Le diagnostic est la clé : chaque ingrédient a sa place et son heure. »",
        "subtitle": "Diagnostic précis, mesures exactes et les 25 ingrédients de votre marché décortiqués sans jargon."
    },

    # SLIDE 13 : LA CARTE DES TEXTURES (DU TYPE 2 AU TYPE 4C)
    {
        "type": "three_card",
        "tracker": "Partie 2 · Chapitre 5 — Typologie capillaire",
        "title": "La carte des textures : du Type 2 au Type 4C",
        "subtitle": "Identifier sa boucle est utile, mais comprendre son comportement est fondamental.",
        "col1": {
            "title": "Type 3 : Les bouclés (3A à 3C)",
            "accent": "indigo",
            "body": [
                "3A / 3B : Boucles bien définies, ressort souple, forme de tire-bouchon ou de grand ressort.",
                "3C : Boucles très serrées de la taille d'un crayon. Beaucoup de volume et de ressort.",
                "Au mouillage : Allongement rapide, boucle immédiatement visible sans produit.",
                "Vulnérabilité : Frisottis fréquents sous l'humidité côtière, perte de définition rapide."
            ]
        },
        "col2": {
            "title": "Type 4A / 4B : Les frisés serrés",
            "accent": "terra",
            "body": [
                "4A : Petites spirales en S serrées de la taille d'une aiguille à tricoter. Bonne rétention d'eau.",
                "4B : Motif en forme de Z avec des angles vifs. Moins de spirales continues, texture cotonneuse.",
                "Le phénomène de rétrécissement (shrinkage) : Vos cheveux perdent 50 à 70 % de leur longueur visible en séchant.",
                "Vulnérabilité : Nœuds de fée fréquents aux extrémités."
            ]
        },
        "col3": {
            "title": "Type 4C : Le roi crépu",
            "accent": "green",
            "body": [
                "4C : Micro-frisures en Z très denses sans motif de boucle défini spontanément à l'air libre.",
                "Shrinkage spectaculaire : Peut rétrécir jusqu'à 75-80 % de sa longueur réelle lorsqu'il est mouillé puis séché.",
                "Densité et force : C'est le cheveu qui a le plus de volume et de tenue pour les coiffures traditionnelles.",
                "Règle d'or absolue : Ne JAMAIS manipuler ou peigner sur cheveux secs."
            ]
        },
        "callout": "Rappelez-vous : le chiffre (3 ou 4) indique la courbure, mais ce qui dicte votre routine, c'est la porosité et l'épaisseur du fil !"
    },

    # SLIDE 14 : LA VÉRITÉ SUR LE TEST DU VERRE D'EAU
    {
        "type": "two_card",
        "tracker": "Partie 2 · Chapitre 6 — Diagnostic de porosité",
        "title": "Le test de porosité : pourquoi le verre d'eau est faux",
        "subtitle": "Démystifier le mythe le plus répandu des réseaux sociaux grâce à la physique simple.",
        "card1": {
            "title": "Le piège du verre d'eau flottant",
            "accent": "terra",
            "paragraphs": [
                ("La théorie populaire :", "On vous dit de jeter un cheveu dans un verre d'eau : s'il flotte, porosité basse ; s'il coule au milieu, moyenne ; s'il coule au fond, haute."),
                ("Pourquoi ce test échoue scientifiquement :", "1. La tension superficielle de l'eau empêche tout corps léger de couler sans être agité mécaniquement.\n2. Le sébum naturel ou les résidus d'huile agissent comme un gilet de sauvetage hydrophobe : même un cheveu très poreux flotte s'il est gras."),
                ("Le résultat désastreux :", "90 % des femmes concluent à tort qu'elles ont une porosité basse et achètent des produits inadaptés qui assèchent leurs cheveux.")
            ]
        },
        "card2": {
            "title": "Ce qu'est réellement la porosité",
            "accent": "indigo",
            "paragraphs": [
                ("La définition biologique :", "La porosité est la capacité de votre cuticule à absorber et surtout à RETENIR l'eau."),
                ("L'état des écailles :", "• Écailles très serrées et collées = Porosité basse (l'eau a du mal à entrer, mais reste bien une fois dedans).\n• Écailles normales = Porosité moyenne.\n• Écailles ouvertes, soulevées ou trouées = Porosité haute (l'eau entre en un éclair, mais s'évapore en 10 minutes)."),
                ("L'impact du climat et du défrisage :", "Le défrisage chimique, les colorations et les fers chauds forcent l'ouverture des écailles et créent artificiellement une porosité haute.")
            ]
        },
        "callout": "Oubliez le verre d'eau. La porosité se mesure dans votre salle de bain, au contact réel de l'eau et de vos mains."
    },

    # SLIDE 15 : LES 3 VRAIS TESTS DE POROSITÉ
    {
        "type": "three_card",
        "tracker": "Partie 2 · Chapitre 6 — Diagnostic pratique",
        "title": "Les trois vrais tests de porosité à faire à la maison",
        "subtitle": "Trois observations croisées sous la douche pour connaître votre profil sans risque d'erreur.",
        "col1": {
            "title": "Test 1 : Le temps de mouillage",
            "accent": "indigo",
            "body": [
                "Sous le jet de la douche ou au seau, observez comment vos cheveux réagissent à l'eau :",
                "• L'eau perle à la surface, glisse comme sur une feuille de taro et met plus de 2 minutes à mouiller le cœur de la chevelure ? → Porosité BASSE.",
                "• Les cheveux boivent l'eau instantanément et sont gorgés en 10 secondes ? → Porosité HAUTE.",
                "• Mouillage normal et uniforme ? → Porosité MOYENNE."
            ]
        },
        "col2": {
            "title": "Test 2 : Le temps de séchage",
            "accent": "gold",
            "body": [
                "Après lavage et essorage doux au t-shirt en coton, sans ajouter aucun produit :",
                "• Vos cheveux mettent 4 à 8 heures (voire toute la journée) à sécher complètement à l'air libre ? → Porosité BASSE.",
                "• Vos cheveux sont secs comme du carton en moins de 30 à 45 minutes ? → Porosité HAUTE (l'eau s'est évaporée immédiatement).",
                "• Séchage complet en 2 à 3 heures ? → Porosité MOYENNE."
            ]
        },
        "col3": {
            "title": "Test 3 : Le test du toucher",
            "accent": "green",
            "body": [
                "Passez un cheveu propre et humide entre votre pouce et votre index, de la pointe vers la racine (à contre-sens des écailles) :",
                "• Le doigt glisse sans aucun accroc, la surface est parfaitement lisse comme un fil de soie ? → Écailles fermées = Porosité BASSE.",
                "• Vous sentez des aspérités rugueuses, le cheveu crisse sous les doigts ? → Écailles ouvertes = Porosité HAUTE."
            ]
        },
        "callout": "Si deux tests sur trois pointent vers le même résultat, vous tenez votre porosité avec certitude !"
    },

    # SLIDE 16 : LES 3 PROFILS DE POROSITÉ & LEURS RÈGLES
    {
        "type": "three_card",
        "tracker": "Partie 2 · Chapitre 7 — Stratégie par porosité",
        "title": "Les trois profils de porosité et leurs règles d'or",
        "subtitle": "À chaque porosité correspond un rituel précis : chaleur, légèreté ou scellage lourd.",
        "col1": {
            "title": "Profil 1 : Porosité Basse",
            "accent": "terra",
            "body": [
                "L'état : Écailles très compactes et hermétiques.",
                "La règle d'or : CHALEUR DOUCE.",
                "Il faut une serviette chaude ou un bonnet de bain pour soulever délicatement les écailles et laisser pénétrer les soins.",
                "Ingrédients amis : Huiles légères (coco fluide, sésame, tournesol), gel de lin, miel liquide, aloé vera.",
                "À bannir : Les beurres épais appliqués froids qui restent en croûte à la surface."
            ]
        },
        "col2": {
            "title": "Profil 2 : Porosité Moyenne",
            "accent": "green",
            "body": [
                "L'état : Écailles équilibrées, absorption et rétention optimales.",
                "La règle d'or : ÉQUILIBRE ET DOUCEUR.",
                "Vos cheveux acceptent presque tout. L'objectif est simplement de ne pas les abîmer par des manipulations excessives.",
                "Ingrédients amis : Karité fouetté, huile d'olive, yaourt, gel de gombo, infusion d'hibiscus.",
                "Fréquence : Lavage 1 fois par semaine, soin hydratant chaque semaine, soin protéiné tous les 2 mois."
            ]
        },
        "col3": {
            "title": "Profil 3 : Porosité Haute",
            "accent": "indigo",
            "body": [
                "L'état : Écailles soulevées, fibre défrisée, colorée ou usée.",
                "La règle d'or : RINÇAGE ACIDE & SCELLAGE.",
                "L'eau s'échappe trop vite. Il faut obligatoirement refermer les écailles au vinaigre de cidre et emprisonner l'hydratation sous un beurre dense.",
                "Ingrédients amis : Beurre de karité brut, huile de ricin diluée, masque protéiné à l'œuf (1×/mois), rinçage vinaigre.",
                "À bannir : Les lavages à l'eau trop chaude."
            ]
        },
        "callout": "Retenez : En porosité basse, on utilise la chaleur pour ouvrir. En porosité haute, on utilise le froid et l'acide pour refermer."
    },

    # SLIDE 17 : BILAN ÉLASTICITÉ & PROTÉINES / HUMIDITÉ
    {
        "type": "two_card",
        "tracker": "Partie 2 · Chapitre 8 — Équilibre biochimique",
        "title": "Le test d'élasticité : l'équilibre protéines-humidité",
        "subtitle": "La kératine donne la force (armature) ; l'eau donne la souplesse (flexibilité).",
        "card1": {
            "title": "Le test de la mèche mouillée",
            "accent": "indigo",
            "paragraphs": [
                ("Le protocole simple :", "Prenez un cheveu propre et mouillé tombé lors du démêlage. Tenez-le fermement entre les deux pouces et index, puis étirez-le très doucement."),
                ("Cas 1 : Le cheveu casse net sans s'étirer (rigidité) :", "Vos cheveux sont saturés en protéines ou manquent cruellement d'eau. La fibre est devenue dure et cassante comme du verre. Stopper les masques aux œufs !"),
                ("Cas 2 : Le cheveu s'étire indéfiniment comme du chewing-gum :", "Vos cheveux manquent de protéines structurales. Ils sont mous, spongieux et se désagrègent sous l'eau. Il faut un soin protéiné réparateur d'urgence."),
                ("Cas 3 : Il s'étire de 20-30 % et reprend sa longueur initiale :", "Félicitations : votre équilibre protéines / eau est parfait !")
            ]
        },
        "card2": {
            "title": "Le tableau réflexe : symptôme → action",
            "accent": "gold",
            "paragraphs": [
                ("Symptôme : Cheveux rêches, durs, effet fil de fer :", "Cause : Trop de protéines ou eau dure. Action : Bain d'huile d'olive tiède + masque au miel et gel de gombo. Zéro œuf pendant 6 semaines."),
                ("Symptôme : Cheveux mous, sans ressort, collants au toucher :", "Cause : Fatigue hygrale (trop d'eau, manque de kératine). Action : Masque à l'œuf entier + rinçage tiède + eau de riz fermentée."),
                ("Symptôme : Cheveux secs mais souples qui cassent aux pointes :", "Cause : Manque d'hydratation quotidienne et de scellage. Action : Spray aloé vera + une noisette de karité chaque soir avant le coucher.")
            ]
        },
        "callout": "L'hydratation apporte la souplesse ; les protéines apportent la résistance. Ne confondez jamais les deux."
    },

    # SLIDE 18 : FICHE DIAGNOSTIC & ARBRE DE DÉCISION
    {
        "type": "two_card",
        "tracker": "Partie 2 · Chapitre 9 — Synthèse personnalisée",
        "title": "Votre fiche de diagnostic : l'arbre de décision rapide",
        "subtitle": "Quatre questions simples pour définir votre routine idéale dès ce soir.",
        "card1": {
            "title": "L'arbre de décision en 4 étapes",
            "accent": "terra",
            "paragraphs": [
                ("1. Vos cheveux sont-ils défrisés ou colorés chimiquement ?", "Si OUI → Vous êtes d'office en porosité haute fragilisée. Priorité : rinçages acides et scellage doux au karité."),
                ("2. Combien de temps mettez-vous à les mouiller à fond sous la douche ?", "Moins d'une minute → Porosité moyenne ou haute. Plus de 2 minutes → Porosité basse (chaleur douce indispensable)."),
                ("3. Le cheveu s'étire-t-il comme un élastique mou ou casse-t-il net ?", "Élastique mou → Soin protéiné mensuel nécessaire. Casse net → Hydratation pure au miel et gombo."),
                ("4. Votre chevelure est-elle fine ou très dense ?", "Fine → Huiles fluides (coco, jojoba, ricin très dilué). Très dense (4C) → Beurre de karité généreux, gel de gombo.")
            ]
        },
        "card2": {
            "title": "Les 3 profils types les plus fréquents au Bénin",
            "accent": "green",
            "paragraphs": [
                ("Profil A — Le 4C naturel très dense (kink) :", "Routine : Gel de gombo pour tout démêlage + beurre de karité brut en scellage après chaque vaporisation d'eau. Nattes sans tension."),
                ("Profil B — Le cheveu en transition ou défrisé :", "Routine : Pré-poo obligatoire à l'huile de coco pour protéger la jonction fragile naturel/défrisé + soin protéiné doux à l'œuf chaque mois."),
                ("Profil C — Le cheveu fin et cassant aux tempes :", "Routine : Massage bi-hebdomadaire à l'huile de ricin diluée à 50 % + bannir les tresses avec rajouts lourds.")
            ]
        },
        "callout": "Remplissez mentalement ces 4 étapes. Vous avez désormais votre carte d'identité capillaire personnalisée."
    },

    # SLIDE 19 : LA PAGE DES MESURES EXACTES
    {
        "type": "image_card",
        "tracker": "Partie 2 · Chapitre 10 — Métrologie capillaire",
        "title": "La page des mesures exactes : fini le « un peu d'huile »",
        "subtitle": "La précision est le secret qui sépare une recette qui marche d'une recette qui poisse.",
        "image": "photo_mesures.png",
        "card": {
            "title": "Les 4 repères universels de votre cuisine",
            "accent": "gold",
            "paragraphs": [
                ("La cuillère à café rase (c. à c.) = 5 ml :", "Équivaut à environ 4 g de beurre de karité ou 5 g d'huile liquide. C'est la dose de base pour les cheveux courts ou le massage du cuir chevelu."),
                ("La cuillère à soupe rase (c. à s.) = 15 ml :", "Équivaut exactement à 3 cuillères à café. C'est la mesure reine pour les bains d'huile tièdes et les masques profonds."),
                ("Le verre à eau ordinaire = 250 ml :", "C'est la base liquide de toutes nos préparations aqueuses : rinçage au vinaigre, gel de gombo, infusion de bissap ou eau de riz."),
                ("La noisette (3 ml) et la noix (10 ml) :", "Une noisette de karité se prélève en effleurant le pot avec le bout de deux doigts. Une noix correspond à une cuillère bombée.")
            ]
        },
        "callout": "Si vous n'avez pas de doseur : un bouchon de bouteille d'huile ordinaire plein à ras bord contient exactement 5 à 7 ml (une cuillère à café)."
    },

    # SLIDE 20 : TABLEAU DES DOSES PAR LONGUEUR
    {
        "type": "table",
        "tracker": "Partie 2 · Chapitre 10 — Dosages précis",
        "title": "Tableau maître des quantités selon votre longueur",
        "subtitle": "Des dosages calibrés au millimètre pour ne jamais gaspiller ni saturer la fibre.",
        "headers": ["Type de soin", "Courts (< 10 cm)", "Mi-longs (10 à 25 cm)", "Longs (> 25 cm)", "Fréquence recommandée"],
        "rows": [
            ["Pré-poo (bain protecteur)", "1 c. à café", "2 c. à café", "1 c. à soupe", "Avant chaque lavage"],
            ["Bain d'huile tiède profond", "2 c. à café", "1 c. à soupe", "2 c. à soupe", "1 à 2 fois par mois"],
            ["Masque hydratant (miel/yaourt)", "2 c. à soupe", "4 c. à soupe", "6 c. à soupe", "1 fois par semaine"],
            ["Soin protéiné (œuf + huile)", "1 œuf + 1 c. à c. huile", "1 œuf + 1 c. à s. huile", "2 œufs + 2 c. à s. huile", "1 fois par mois maximum"],
            ["Scellage au beurre de karité", "1 noisette (3 ml)", "1 noix (10 ml)", "2 noix (20 ml)", "2 à 3 fois par semaine"],
            ["Gel de gombo démêlant", "1 c. à soupe", "2 à 3 c. à soupe", "4 c. à soupe", "À chaque démêlage"],
            ["Massage du cuir chevelu", "½ c. à café", "1 c. à café", "1 c. à café", "2 fois par semaine"],
            ["Rinçage acide au vinaigre", "1 c. à s. / 1 verre", "1 c. à s. / 1 verre", "2 c. à s. / 1 verre", "Après chaque savon noir"]
        ],
        "callout": "Le cheveu texturé est comme une éponge : une fois qu'il a bu sa dose, tout produit supplémentaire reste en surface, attire la poussière et étouffe le crâne."
    },

    # SLIDE 21 : LES 3 RÈGLES D'OR DE LA CUISINE CAPILLAIRE
    {
        "type": "three_card",
        "tracker": "Partie 2 · Chapitre 10 — Règles de préparation",
        "title": "Les trois règles d'or de la cosmétique en cuisine",
        "subtitle": "La nature est puissante, mais elle exige une hygiène irréprochable.",
        "col1": {
            "title": "Règle 1 : Zéro conservateur",
            "accent": "terra",
            "body": [
                "Toute préparation contenant de l'eau (gel de gombo, infusion d'hibiscus, masque au miel/yaourt) fermente et développe des bactéries en 24h à l'air libre sous notre climat chaud.",
                "Conservez toujours au réfrigérateur entre 3 et 5 jours maximum.",
                "Si la préparation sent l'aigre, change de couleur ou devient filante de façon anormale : jetez immédiatement !"
            ]
        },
        "col2": {
            "title": "Règle 2 : Le test de tolérance",
            "accent": "gold",
            "body": [
                "Naturel ne signifie pas sans danger allergique.",
                "Avant d'appliquer une huile végétale nouvelle, une huile essentielle ou un masque à l'œuf sur toute votre tête :",
                "Déposez 1 goutte au creux du coude ou derrière l'oreille.",
                "Attendez 24 heures : si aucune rougeur, démangeaison ou sensation de brûlure n'apparaît, vous pouvez y aller les yeux fermés."
            ]
        },
        "col3": {
            "title": "Règle 3 : Le principe de sobriété",
            "accent": "green",
            "body": [
                "Ne mélangez jamais plus de 3 ingrédients actifs dans une même recette maison.",
                "Mélanger dix poudres et six huiles ensemble annule souvent les effets de chacune et rend impossible l'identification de ce qui a fonctionné ou provoqué une allergie.",
                "Un bon masque, c'est : 1 base hydratante (eau/gombo/miel) + 1 actif assouplissant (yaourt/œuf) + 1 filet d'huile protectrice."
            ]
        },
        "callout": "La fraîcheur et la propreté des ustensiles garantissent l'efficacité de vos soins de cuisine."
    },

    # SLIDE 22 : FAMILLE 1 — HUILE DE COCO
    {
        "type": "two_card",
        "tracker": "Famille 1 · Les huiles de base qui pénètrent",
        "title": "L'Huile de Coco vierge (Cocos nucifera)",
        "subtitle": "Badge : ● ÉTAYÉ  ·  La reine incontestée de la pénétration intracellulaire.",
        "card1": {
            "title": "Ce qu'elle fait et POURQUOI ça marche",
            "accent": "indigo",
            "paragraphs": [
                ("Le secret de l'acide laurique :", "L'huile de coco possède une structure linéaire et un poids moléculaire très faible. C'est l'une des rares huiles au monde capable de traverser la cuticule pour pénétrer à l'intérieur du cortex."),
                ("La réduction de la perte de protéines (-40 %) :", "L'étude de référence Rele & Mohile (2003) a prouvé qu'une application d'huile de coco avant lavage réduit la perte de protéines de la fibre de près de 40 %, sur cheveu sain comme sur cheveu abîmé."),
                ("L'effet bouclier anti-gonflement :", "En tapissant le cortex, elle empêche l'eau du lavage de gonfler brutalement la fibre (fatigue hygrale) et protège les cuticules.")
            ]
        },
        "card2": {
            "title": "Application, Quantités & Vigilance",
            "accent": "gold",
            "paragraphs": [
                ("Quantités exactes :", "Cheveux courts : 1 c. à café · Mi-longs : 2 c. à café · Longs : 1 c. à soupe bombée. Toujours sur CHEVEUX SECS avant le lavage."),
                ("Temps de pose & Fréquence :", "30 minutes sous charlotte (ou toute la nuit sur pointes sèches). À réaliser avant chaque lavage hebdomadaire."),
                ("Attention : Précautions majeures :", "1. L'huile fige sous 24 °C (par temps d'harmattan ou au frais) : tiédir le bol dans de l'eau chaude, jamais au feu direct.\n2. Éviter d'en tartiner le cuir chevelu s'il est déjà gras ou sujet aux pellicules."),
                ("Coût au marché :", "50 à 80 FCFA par application (flacon artisanal à 1 000 FCFA).")
            ]
        },
        "callout": "À RETENIR : L'huile de coco s'applique AVANT le shampoing sur cheveux secs, jamais après sur cheveux mouillés sous peine de cartonner."
    },

    # SLIDE 23 : FAMILLE 1 — HUILE D'OLIVE VIERGE
    {
        "type": "two_card",
        "tracker": "Famille 1 · Les huiles de base qui assouplissent",
        "title": "L'Huile d'Olive vierge (Olea europaea)",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  L'émolliente royale des textures rêches et déshydratées.",
        "card1": {
            "title": "Ce qu'elle fait et POURQUOI ça marche",
            "accent": "green",
            "paragraphs": [
                ("La richesse en acide oléique et squalène :", "L'huile d'olive est une huile mi-lourde très nourrissante. Elle contient du squalène végétal qui imite parfaitement le sébum humain."),
                ("Assouplissement instantané de la cuticule :", "Elle n'entre pas aussi profondément que le coco, mais elle lubrifie les tuiles de la cuticule, élimine l'effet « paille » et facilite grandement le glissement du peigne à dents larges."),
                ("Action anti-oxydante puissante :", "Riche en vitamine E et polyphénols, elle protège la kératine contre l'oxydation induite par les rayons ultraviolets intenses d'Afrique.")
            ]
        },
        "card2": {
            "title": "Application, Quantités & Vigilance",
            "accent": "terra",
            "paragraphs": [
                ("Quantités exactes :", "Cheveux courts : 1 c. à café · Mi-longs : 1 c. à soupe · Longs : 2 c. à soupe. Parfaite en bain d'huile tiède combinée au miel."),
                ("Temps de pose & Fréquence :", "20 à 30 minutes sous serviette tiède. 1 fois par semaine pour cheveux très secs, 1 fois par mois en entretien normal."),
                ("Attention : Précautions majeures :", "1. Choisir une huile vierge extra pressée à froid (la vraie huile picote légèrement la gorge ; si elle est fade, elle est coupée à l'huile de palme raffinée).\n2. Bien rincer pour éviter d'alourdir les boucles fines."),
                ("Coût au marché :", "100 à 150 FCFA par soin (bouteille importée ou locale).")
            ]
        },
        "callout": "À RETENIR : L'alliée n°1 des cheveux 4C très secs en saison d'harmattan. À chauffer très légèrement au bain-marie avant pose."
    },

    # SLIDE 24 : FAMILLE 1 — SÉSAME, TOURNESOL & ARACHIDE
    {
        "type": "three_card",
        "tracker": "Famille 1 · Huiles de base locales fluides",
        "title": "Sésame, Tournesol & Arachide locale",
        "subtitle": "Trois alternatives fluides, économiques et légères pour les porosités basses.",
        "col1": {
            "title": "Huile de Sésame (○ TRADITION)",
            "accent": "gold",
            "body": [
                "Propriétés : Très pénétrante et légère, elle contient de la sésamine et agit comme un filtre solaire naturel doux contre les UV.",
                "Action : Stimule la microcirculation du cuir chevelu sans l'asphyxier.",
                "Quantité : 1 c. à café en huile de coiffage légère quotidienne.",
                "Idéale pour : Cheveux fins, vanilles d'enfants, cuirs chevelus sensibles."
            ]
        },
        "col2": {
            "title": "Huile de Tournesol (◐ PROMETTEUR)",
            "accent": "indigo",
            "body": [
                "Propriétés : Championne des acides gras polyinsaturés (acide linoléique oméga-6).",
                "Action : Pénètre la cuticule sans laisser de film gras lourd. Apporte une brillance soyeuse immédiate.",
                "Quantité : 1 à 2 c. à café mélangées dans votre vaporisateur d'eau.",
                "Idéale pour : Les cheveux à porosité basse qui fuient le karité trop dense."
            ]
        },
        "col3": {
            "title": "Huile d'Arachide locale (○ TRADITION)",
            "accent": "terra",
            "body": [
                "Propriétés : Accessible dans le moindre village du Bénin à prix dérisoire.",
                "Action : Très émolliente, elle assouplit instantanément les croûtes de sécheresse du cuir chevelu.",
                "Quantité : 1 c. à soupe en pré-poo d'urgence si vous n'avez rien d'autre sous la main.",
                "Précaution : Vérifier absolument l'absence d'allergie aux arachides."
            ]
        },
        "callout": "Ces trois huiles prouvent qu'il n'est pas nécessaire d'acheter des produits exotiques : votre cuisine regorge de trésors lipidiques."
    },

    # SLIDE 25 : FAMILLE 2 — BEURRE DE KARITÉ BRUT
    {
        "type": "two_card",
        "tracker": "Famille 2 · Les beurres végétaux protecteurs",
        "title": "Le Beurre de Karité brut non raffiné (Butyrospermum parkii)",
        "subtitle": "Badge : ○ TRADITION  ·  Le roi absolu du scellage et de la protection contre l'harmattan.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "gold",
            "paragraphs": [
                ("La puissance des acides stéarique et oléique :", "Le karité brut est un beurre très dense, riche en insaponifiables (latex végétal, phytostérols, vitamines A et E)."),
                ("Le maître de l'occlusion imperméable :", "Le karité ne « nourrit » pas d'eau : il SCELLÉ l'eau ! Il forme une barrière hydrophobe étanche qui empêche l'humidité présente dans la fibre de s'évaporer sous le vent ou le soleil."),
                ("La protection mécanique contre les agressions :", "Il gaine la cuticule d'un film souple qui réduit les frottements destructeurs contre les cols de vêtements ou les oreillers en coton.")
            ]
        },
        "card2": {
            "title": "Application, Quantités & Vigilance",
            "accent": "terra",
            "paragraphs": [
                ("Quantités exactes :", "Cheveux courts : 1 noisette (3 ml) · Mi-longs : 1 noix (10 ml) · Longs : 2 noix (20 ml). Toujours fondu entre les paumes par friction avant pose."),
                ("Attention : LA RÈGLE D'OR ABSOLUE :", "JAMAIS DE KARITÉ SUR CHEVEUX SECS ! Poser du karité sur un cheveu sec, c'est mettre un couvercle sur une casserole vide : vous enfermez la sécheresse à l'intérieur."),
                ("Comment le choisir au marché :", "Préférer le karité brut du Nord-Bénin (Djougou, Natitingou, Parakou), de couleur jaune ou ivoire, à l'odeur fumée caractéristique. Fuir le karité blanc décoloré et désodorisé chimiquement."),
                ("Coût :", "20 à 30 FCFA par utilisation (pot à 500 FCFA pour 4 mois).")
            ]
        },
        "callout": "À RETENIR : Toujours mouiller d'abord (eau ou aloé vera), puis sceller avec une noisette de karité. C'est le secret de la souplesse infinie du cheveu 4C."
    },

    # SLIDE 26 : FAMILLE 2 — BEURRES DE CACAO & MANGUE (KPAGNAN)
    {
        "type": "two_card",
        "tracker": "Famille 2 · Beurres locaux précieux",
        "title": "Beurres de Cacao & Mangue sauvage (Kpagnan)",
        "subtitle": "Badge : ○ TRADITION  ·  Deux merveilles locales pour réparer les pointes et adoucir.",
        "card1": {
            "title": "Beurre de Cacao pur (Theobroma cacao)",
            "accent": "terra",
            "paragraphs": [
                ("Propriétés d'armure protectrice :", "Plus dur que le karité, il fond exactement à la température du corps (35 °C). Il est exceptionnellement riche en polyphénols antioxydants."),
                ("Le pansement des pointes fourchues :", "Idéal en baume protecteur pour enrober les derniers centimètres des cheveux (les pointes), qui sont les plus vieux et les plus vulnérables."),
                ("Dose :", "Une petite noisette fondue entre les doigts, appliquée strictement sur les pointes avant de faire des vanilles.")
            ]
        },
        "card2": {
            "title": "Beurre de Mangue sauvage (Kpagnan / Pentadesma)",
            "accent": "green",
            "paragraphs": [
                ("Le secret des femmes du Bénin :", "Extrait des graines de mangue ou de l'arbre à beurre Pentadesma butyracea. Texture beaucoup plus fondante, soyeuse et non collante que le karité."),
                ("Assouplissement spectaculaire des racines 4C :", "Riche en acide isostéarique, il pénètre mieux que le karité et détend la fibre sans chaleur."),
                ("Dose :", "1 noix appliquée sur les repousses crépues très épaisses pour faciliter le tressage sans douleur.")
            ]
        },
        "callout": "Le kpagnan est le joyau secret des marchés béninois : plus fondant que le karité, il ne laisse aucun fini blanc sur les cheveux sombres."
    },

    # SLIDE 27 : FAMILLE 3 — HUILE DE RICIN LOCALE
    {
        "type": "two_card",
        "tracker": "Famille 3 · Huiles fortifiantes du cuir chevelu",
        "title": "L'Huile de Ricin locale (Ricinus communis)",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  La reine de l'épaississement qui exige une prudence stricte.",
        "card1": {
            "title": "Ce qu'elle fait et la vérité sur la pousse",
            "accent": "indigo",
            "paragraphs": [
                ("La vérité biologique sans filtre :", "L'huile de ricin NE FAIT PAS pousser les cheveux plus vite que le rythme génétique (environ 1 cm par mois). Tout produit promettant 5 cm en deux semaines est une illusion."),
                ("Pourquoi elle donne l'illusion de la pousse :", "Grâce à sa teneur unique en acide ricinoléique (90 %), elle est ultra-visqueuse. Elle s'accroche à la tige, comble les fissures microscopiques et donne immédiatement une sensation de densité et de corps exceptionnel."),
                ("Action sur la circulation du cuir chevelu :", "En massage doux, son épaisseur stimule mécaniquement le flux sanguin vers le bulbe pileux, favorisant l'ancrage de la racine.")
            ]
        },
        "card2": {
            "title": "Application, Quantités & Règle de dilution",
            "accent": "terra",
            "paragraphs": [
                ("Attention : LA RÈGLE D'OR DE DILUTION (50 %) :", "Ne JAMAIS appliquer l'huile de ricin pure sur toute la tête ! Sa viscosité colle les mèches entre elles et arrache les cheveux sains lors du démêlage."),
                ("La recette obligatoire :", "Toujours mélanger 1 part d'huile de ricin pour 2 parts d'huile fluide (coco, olive ou sésame)."),
                ("Quantité exacte :", "½ cuillère à café du mélange, prélevée sur le bout des doigts."),
                ("Zones cibles :", "En tapotant délicatement sur la lisière (edges) et les tempes fragilisées par les tresses. 2 fois par semaine maximum.")
            ]
        },
        "callout": "À RETENIR : Le ricin fortifie et épaissit, mais toujours dilué ! Pure, elle devient une colle qui casse vos mèches."
    },

    # SLIDE 28 : FAMILLE 3 — HUILES DE BAOBAB & MORINGA
    {
        "type": "two_card",
        "tracker": "Famille 3 · Trésors botaniques sahéliens",
        "title": "Les Huiles précieuses de Baobab & Moringa",
        "subtitle": "Deux élixirs africains d'exception pour réparer l'élasticité et purifier le crâne.",
        "card1": {
            "title": "L'Huile de Baobab (○ TRADITION)",
            "accent": "gold",
            "paragraphs": [
                ("L'arbre de vie africain :", "Pressée à froid des graines du fruit de baobab (pain de singe). Rare, fine et d'une absorption instantanée sans laisser de gras."),
                ("Le cocktail vitaminique A, D, E et F :", "Riche en acides gras linoléique et palmitique. Elle redonne une élasticité miraculeuse aux boucles ternes et fatiguées."),
                ("Usage idéal :", "3 à 5 gouttes chauffées dans les paumes en finition de coiffure pour lustrer les vanilles ou sceller les pointes fines sans les alourdir.")
            ]
        },
        "card2": {
            "title": "L'Huile de Moringa locale (◐ PROMETTEUR)",
            "accent": "green",
            "paragraphs": [
                ("La richesse en acide béhénique :", "L'huile de graines de moringa est appelée historiquement « huile de Ben ». Elle possède des propriétés antibactériennes et purifiantes majeures."),
                ("Protection contre la poussière de ville :", "Elle crée un bouclier invisible contre la pollution urbaine de Cotonou et les fumées de pot d'échappement qui oxydent la kératine."),
                ("Usage idéal :", "1 cuillère à café en massage du cuir chevelu en cas de démangeaisons ou de pellicules grasses.")
            ]
        },
        "callout": "Produites artisanalement au Nord du Bénin, ces deux huiles rivalisent avec les sérums les plus chers du marché mondial."
    },

    # SLIDE 29 : FAMILLE 3 — NIGELLE, PALMISTE & OLÉINE DE KARITÉ
    {
        "type": "three_card",
        "tracker": "Famille 3 · Actifs traditionnels de purification",
        "title": "Nigelle, Huile de Palmiste (Tchobo) & Oléine",
        "subtitle": "La pharmacopée béninoise ancestrale au service du cuir chevelu assaini.",
        "col1": {
            "title": "Huile de Nigelle (◐ PROMETTEUR)",
            "accent": "indigo",
            "body": [
                "Actif phare : La thymoquinone, anti-inflammatoire et antifongique de référence.",
                "Action : Élimine les démangeaisons insupportables sous les nattes et apaise les cuirs chevelus rougis.",
                "Dose : 5 gouttes diluées dans 1 c. à soupe d'huile d'olive en massage 1 fois par semaine."
            ]
        },
        "col2": {
            "title": "Huile de Palmiste / Tchobo (○ TRADITION)",
            "accent": "terra",
            "body": [
                "Origine : Extraite par torréfaction des amandes de noix de palme (Manyanga au Cameroun, Tchobo au Bénin).",
                "Action : Huile noire à odeur toastée, utilisée depuis des siècles pour assainir le crâne, traiter les mycoses et fortifier les cheveux d'enfants.",
                "Dose : ½ c. à café sur les raies une heure avant le lavage."
            ]
        },
        "col3": {
            "title": "Oléine de Karité (○ TRADITION)",
            "accent": "gold",
            "body": [
                "Origine : Fraction liquide obtenue par pression à froid douce du karité.",
                "Action : Conserve tous les bienfaits protecteurs du karité brut tout en restant 100 % liquide et fluide à température ambiante.",
                "Usage : Parfaite pour composer vos sprays hydratants quotidiens sans jamais boucher l'embout pulvérisateur."
            ]
        },
        "callout": "Le Tchobo traditionnel béninois est un antiseptique naturel formidable qui assainit le cuir chevelu pour moins de 200 FCFA."
    },

    # SLIDE 30 : FAMILLE 4 — GEL DE GOMBO FRAIS
    {
        "type": "two_card",
        "tracker": "Famille 4 · Les gels & mucilages démêlants",
        "title": "Le Gel de Gombo frais (Abelmoschus esculentus)",
        "subtitle": "Badge : ○ TRADITION  ·  Le démêlant naturel n°1 d'Afrique : glisse, douceur et zéro casse.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "green",
            "paragraphs": [
                ("La magie des polysaccharides mucilagineux :", "Le gombo contient une concentration extraordinaire de mucilages complexes (polymères de rhamnose, galactose et acide galacturonique)."),
                ("Une glisse supérieure aux soins industriels :", "Au contact de l'eau, ces molécules forment un gel visqueux ultra-glissant qui enrobe chaque fibre capillaire d'un coussin protecteur."),
                ("La fin de la casse au démêlage :", "Les nœuds de fée et les mèches emmêlées glissent les unes contre les autres et se défont sous les doigts sans aucune résistance mécanique."),
                ("Hydratation non grasse :", "Apporte une eau gélifiée qui repulpe les boucles sans laisser aucun résidu gras ni pellicule blanche.")
            ]
        },
        "card2": {
            "title": "Recette minute, Utilisation & Conservation",
            "accent": "terra",
            "paragraphs": [
                ("La recette express à froid (la meilleure) :", "Coupez 5 ou 6 gombos frais en rondelles dans 1 grand verre d'eau (250 ml). Laissez reposer au réfrigérateur toute la nuit. Filtrez le lendemain matin à travers un collant propre ou une passoire fine."),
                ("Mode d'emploi :", "Appliquez généreusement sur cheveux mouillés, section par section. Démêlez au doigt puis au peigne large en partant des pointes."),
                ("Attention : Conservation stricte :", "3 à 5 jours au réfrigérateur. Si vous en préparez d'avance, congelez le gel dans un bac à glaçons : 2 glaçons décongelés par jour de soin !"),
                ("Coût :", "100 FCFA pour une tête complète.")
            ]
        },
        "callout": "À RETENIR : Le gel de gombo est le plus grand cadeau de la cuisine africaine à nos cheveux 4C. Il transforme la séance de démêlage en un moment de pur plaisir."
    },

    # SLIDE 31 : FAMILLE 4 — GEL DE GRAINES DE LIN
    {
        "type": "two_card",
        "tracker": "Famille 4 · Définition et tenue végétale",
        "title": "Le Gel de Graines de Lin (Linum usitatissimum)",
        "subtitle": "Badge : ○ TRADITION  ·  Le gel coiffant naturel qui définit les boucles sans cartonner.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "indigo",
            "paragraphs": [
                ("Gaine de polysaccharides lissants :", "Les graines de lin libèrent à chaud un mucilage riche en oméga-3 végétaux et en polymères filmogènes naturels."),
                ("Définition nette des boucles et twists :", "En séchant sur la chevelure humide, le gel se rétracte légèrement et maintient le dessin de la boucle (curl definition) ou la tenue des vanilles pendant 4 à 6 jours."),
                ("Zéro résidu blanc, zéro assèchement :", "Contrairement aux gels du commerce bourrés d'alcool dénaturé et de PVP qui assèchent et s'effritent en pellicules blanches, le gel de lin laisse le cheveu brillant, souple et hydraté.")
            ]
        },
        "card2": {
            "title": "Recette, Dosage & Astuce de tenue",
            "accent": "gold",
            "paragraphs": [
                ("La recette inratable en 8 minutes :", "Mettez 2 cuillères à soupe de graines de lin dans 1 grand verre d'eau (250 ml). Portez à ébullition douce pendant 7 à 8 minutes en remuant. Dès que l'écume blanche monte et que le liquide a la consistance d'un blanc d'œuf : coupez le feu et filtrez immédiatement à chaud à travers un bas en nylon."),
                ("Dosage :", "1 cuillère à soupe pour cheveux courts · 2 à 4 cuillères pour cheveux longs, mèche par mèche sur cheveux mouillés."),
                ("Conservation :", "1 à 2 semaines au réfrigérateur avec 3 gouttes d'huile essentielle de romarin.")
            ]
        },
        "callout": "À RETENIR : Les graines filtrées peuvent être recongelées et réutilisées une seconde fois pour une nouvelle fournée de gel !"
    },

    # SLIDE 32 : FAMILLE 4 — ALOÉ VERA FRAIS
    {
        "type": "two_card",
        "tracker": "Famille 4 · L'hydratation enzymatique apaisante",
        "title": "L'Aloé Vera frais du jardin (Aloe barbadensis)",
        "subtitle": "Badge : ○ TRADITION  ·  98 % d'eau pure structurée pour apaiser le crâne en feu.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "green",
            "paragraphs": [
                ("L'eau vivante végétale :", "Le mucilage transparent de la feuille d'aloé contient 98 % d'eau liée à des polysaccharides (acémannane), 20 minéraux, 18 acides aminés et des vitamines B et C."),
                ("pH acide naturel régulateur (pH 4,5) :", "Son acidité physiologique referme instantanément les écailles et restaure le film hydrolipidique protecteur du cuir chevelu."),
                ("Anti-inflammatoire et antiprurigineux :", "Apaise immédiatement les démangeaisons, tiraillements et échauffements provoqués par la pose de tresses ou le soleil d'Afrique.")
            ]
        },
        "card2": {
            "title": "Préparation impérative & Recette de spray",
            "accent": "terra",
            "paragraphs": [
                ("Attention : LA PRÉCAUTION DE L'ALOÏNE (JAUNE) :", "Coupez la base de la feuille et laissez-la tremper debout dans un verre d'eau pendant 15 minutes. Un liquide jaune amer et toxique (l'aloïne, très irritante) s'écoule. Jetez ce liquide et ne gardez que le gel cristal transparent au centre !"),
                ("La recette du spray quotidien magique :", "Mixez 2 c. à soupe de gel cristal avec 1 verre d'eau de source et 1 c. à café d'huile de coco ou de sésame. Filtrez au collant."),
                ("Utilisation sous tresses :", "Vaporisez entre les raies 2 à 3 fois par semaine pour garder le cuir chevelu frais et sans pellicules.")
            ]
        },
        "callout": "À RETENIR : Utilisez toujours la feuille fraîche de votre cour ou du marché. Les gels industriels en tube contiennent souvent 90 % d'eau ordinaire épaissie aux polymères."
    },

    # SLIDE 33 : FAMILLE 4 — BISSAP & FEUILLES DE JUTE (EWEDU)
    {
        "type": "two_card",
        "tracker": "Famille 4 · Botanique culinaire locale",
        "title": "Infusion de Bissap & Feuilles de Jute (Ewedu)",
        "subtitle": "Deux ingrédients du marché de Dantokpa aux vertus capillaires méconnues.",
        "card1": {
            "title": "L'Infusion de Fleurs de Bissap (◐ PROMETTEUR)",
            "accent": "terra",
            "paragraphs": [
                ("Richesse en acides de fruits et vitamine C :", "Les calices d'Hibiscus sabdariffa sont saturés d'acides citrique et malique qui resserrent les écailles comme un miroir."),
                ("Stimulation de la pousse :", "Favorise la microcirculation sanguine au niveau du bulbe et lutte contre l'affinement prématuré de la chevelure."),
                ("Recette de dernière eau de rinçage :", "Faites infuser 1 poignée de fleurs séchées dans 500 ml d'eau bouillante pendant 15 minutes. Laissez refroidir, filtrez. Utilisez en dernier rinçage sur cheveux sombres pour une brillance spectaculaire.")
            ]
        },
        "card2": {
            "title": "Les Feuilles de Jute / Ewedu / Crin-crin (○ TRADITION)",
            "accent": "green",
            "paragraphs": [
                ("Le secret démêlant pour enfants :", "Les feuilles de Corchorus olitorius (appelées crin-crin au Bénin, ewedu au Nigéria) produisent un mucilage extrêmement glissant."),
                ("Alternative sans aucun coût au gombo :", "Écrasez une poignée de feuilles fraîches dans un peu d'eau tiède pour extraire le suc gluant."),
                ("Application :", "Idéal pour démêler la chevelure fragile des petites filles sans douleur et sans larmes avant de réaliser des nattes collées.")
            ]
        },
        "callout": "La cuisine africaine regorge d'actifs de classe mondiale : nos grands-mères avaient tout compris bien avant les laboratoires de cosmétique moderne."
    },

    # SLIDE 34 : FAMILLE 5 — LE SOIN PROTÉINÉ À L'ŒUF
    {
        "type": "two_card",
        "tracker": "Famille 5 · Protéines & Reconstruction",
        "title": "Le Soin Protéiné à l'Œuf entier",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  Le plâtre d'urgence des chevelures élastiques et cassantes.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "indigo",
            "paragraphs": [
                ("L'apport d'ovalbumine et de lécithine :", "Le blanc d'œuf apporte des protéines pures solubles ; le jaune apporte des lipides émulsifiants et de la biotine (vitamine B8)."),
                ("Le comblement temporaire des fissures :", "Les molécules de protéines de l'œuf se déposent sur les zones abîmées de la cuticule. Elles forment un pansement temporaire qui redonne du corps et de la résistance à la tige."),
                ("L'effet gainant immédiat :", "Dès le premier soin, le cheveu semble deux fois plus épais et cesse de s'étirer comme du chewing-gum.")
            ]
        },
        "card2": {
            "title": "Recette, Fréquence & Règle de température",
            "accent": "terra",
            "paragraphs": [
                ("La recette équilibrée :", "1 œuf entier battu énergiquement + 1 c. à soupe d'huile d'olive + 1 c. à café de miel pur. Bien homogénéiser."),
                ("Attention : RÈGLE DE RINÇAGE VITALE (EAU TIÈDE OU FROIDE) :", "Ne rincez JAMAIS un masque à l'œuf avec de l'eau chaude ! À partir de 45 °C, l'œuf cuit instantanément dans vos cheveux : vous vous retrouverez avec des morceaux d'omelette collés impossibles à enlever sans arracher les mèches."),
                ("Fréquence stricte :", "1 fois par mois maximum (ou tous les 2 mois sur cheveux sains). Un excès de protéines durcit le cheveu et le casse net."),
                ("Coût :", "100 à 120 FCFA.")
            ]
        },
        "callout": "À RETENIR : L'œuf est un reconstructeur d'urgence, pas un soin de confort. À réserver aux lendemains de détresse ou après défrisage."
    },

    # SLIDE 35 : FAMILLE 5 — YAOURT NATURE & LAIT CAILLÉ
    {
        "type": "two_card",
        "tracker": "Famille 5 · Acide lactique & Nettoyage doux",
        "title": "Le Yaourt Nature & Lait caillé local",
        "subtitle": "Badge : ○ TRADITION  ·  Le lissage cuticulaire doux et l'assainissement du cuir chevelu.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "green",
            "paragraphs": [
                ("La puissance de l'acide lactique (AHA naturel) :", "L'acide lactique présent dans les produits laitiers fermentés dissout en douceur les cellules mortes et les résidus de sébum qui bouchent les pores du cuir chevelu."),
                ("Fermeture mécanique des cuticules :", "Son pH naturellement acide (pH 4 à 4,5) referme les écailles soulevées et élimine la rugosité au toucher."),
                ("Protéines de lactosérum douces :", "Contrairement à l'œuf qui peut durcir la fibre, les protéines de lait sont plus douces et conviennent parfaitement aux cheveux à porosité basse.")
            ]
        },
        "card2": {
            "title": "Recette du masque fondant & Utilisation",
            "accent": "gold",
            "paragraphs": [
                ("La recette clarifiante et hydratante :", "4 cuillères à soupe de yaourt nature entier (non sucré) ou de lait caillé frais + 1 cuillère à soupe de miel pur + 1 cuillère à café d'huile de coco."),
                ("Temps de pose :", "20 minutes sous charlotte, puis rinçage tiède soigné."),
                ("Indication reine :", "Idéal pour assainir un cuir chevelu qui démange après avoir porté des tresses pendant un mois."),
                ("Attention : Précaution :", "Bien rincer à grande eau tiède pour éviter toute odeur acide résiduelle en séchant.")
            ]
        },
        "callout": "Le yaourt nature est le meilleur soin de transition après la dépose de tresses pour décoller la poussière accumulée à la racine."
    },

    # SLIDE 36 : FAMILLE 5 — EAU DE RIZ FERMENTÉE
    {
        "type": "two_card",
        "tracker": "Famille 5 · La cure asiatique adaptée au 4C",
        "title": "L'Eau de Riz fermentée (La méthode Yao)",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  Une cure de force à manier avec discernement.",
        "card1": {
            "title": "Ce qu'elle fait et POURQUOI ça marche",
            "accent": "indigo",
            "paragraphs": [
                ("Le secret de l'Inositol :", "L'eau de riz fermentée est gorgée d'inositol, un glucide cyclique capable de pénétrer le cheveu abîmé et d'y rester même après rinçage pour le protéger des frottements."),
                ("Acides aminés et vitamines du groupe B :", "Le processus de fermentation abaisse le pH de l'eau de riz et multiplie sa concentration en antioxydants et minéraux fortifiants."),
                ("Le mythe des cheveux géants :", "Les femmes Yao du village de Huangluo ont des cheveux de 2 mètres grâce à la génétique ET à ce soin. Cela ne fera pas pousser vos cheveux de 20 cm, mais cela stoppe net la casse des longueurs.")
            ]
        },
        "card2": {
            "title": "Protocole de fermentation & Posologie",
            "accent": "terra",
            "paragraphs": [
                ("La préparation propre :", "Rincez ½ verre de riz blanc local pour enlever les impuretés. Placez le riz dans un bocal propre avec 2 grands verres d'eau (500 ml). Laissez fermenter à l'abri de la lumière pendant 24 heures (la préparation commence à sentir légèrement aigre). Filtrez."),
                ("Mode d'application :", "Versez en eau de rinçage après le shampoing. Laissez poser 15 minutes sous bonnet, puis rincez abondamment à l'eau claire."),
                ("Attention : LA RÈGLE VITALE :", "1 FOIS PAR MOIS MAXIMUM ! Utilisée trop souvent sur cheveu 4C, l'eau de riz provoque une surcharge en amidon et protéines : le cheveu devient rigide et casse."),
                ("Ne jamais utiliser chez les enfants de moins de 10 ans.")
            ]
        },
        "callout": "À RETENIR : L'eau de riz est un traitement de renforcement ponctuel pour cheveux mous et dévitalisés. Ne tombez jamais dans l'excès quotidien."
    },

    # SLIDE 37 : FAMILLE 6 — MIEL PUR DU BÉNIN
    {
        "type": "two_card",
        "tracker": "Famille 6 · Les humectants suprêmes",
        "title": "Le Miel pur sauvage du Bénin",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  L'aimant à eau naturel qui transforme la texture du cheveu.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "gold",
            "paragraphs": [
                ("La propriété humectante inégalée :", "Le miel est composé à 80 % de sucres naturels (fructose, glucose). Sa structure hygroscopique capte littéralement les molécules d'eau de l'atmosphère pour les fixer au cœur de la kératine."),
                ("L'adoucissement des cuticules rêches :", "Riche en enzymes et oligo-éléments, il assouplit les mèches rigides et apporte une brillance dorée soyeuse incomparable."),
                ("Propriétés antiseptiques douces :", "Contient de faibles quantités de peroxyde d'hydrogène enzymatique naturel qui assainissent les micro-lésions du cuir chevelu sans irriter.")
            ]
        },
        "card2": {
            "title": "Dosage, Recette de masque & Précaution",
            "accent": "green",
            "paragraphs": [
                ("Dosage parfait :", "1 cuillère à café pour un masque court · 1 cuillère à soupe pour cheveux mi-longs à longs. Toujours dilué dans un corps gras ou aqueux."),
                ("La recette du masque d'or hebdomadaire :", "1 c. à soupe de miel pur + 1 c. à soupe d'huile d'olive + 2 c. à soupe de yaourt ou de gel de gombo. Poser 20 minutes sous serviette tiède."),
                ("Attention : Précaution importante :", "Exiger un vrai miel pur local (Bembèrèkè, Djougou). Les faux miels vendus en bord de route coupés au sirop de sucre brûlé n'ont aucun pouvoir humectant et collent les cheveux."),
                ("En période d'harmattan très sec : toujours sceller au karité après un soin au miel !")
            ]
        },
        "callout": "À RETENIR : Le miel est l'ingrédient magique pour redonner vie aux cheveux cartonnés par le soleil et l'eau dure."
    },

    # SLIDE 38 : FAMILLE 6 — BANANE MÛRE & AVOCAT FRAIS
    {
        "type": "two_card",
        "tracker": "Famille 6 · Cocktails nutritifs d'urgence",
        "title": "Banane très mûre & Avocat écrasé",
        "subtitle": "Badge : ○ TRADITION  ·  Le masque de secours nutritionnel quand les pointes crient famine.",
        "card1": {
            "title": "Ce qu'ils apportent à la fibre",
            "accent": "terra",
            "paragraphs": [
                ("La banane mûre (potassium et silice) :", "La banane tigrée ou noire regorge de potassium, d'huiles naturelles et de silice végétale. Elle renforce l'élasticité et adoucit les cheveux les plus rêches."),
                ("L'avocat frais (cocktail lipidique complet) :", "L'avocat est saturé d'acides gras mono-insaturés (acide oléique), de phytostérols et de vitamines B6 et E."),
                ("L'effet masque doudou d'urgence :", "Cette combinaison sauve les chevelures brûlées par le soleil de midi ou asséchées après un mois de mer ou de plage à Grand-Popo.")
            ]
        },
        "card2": {
            "title": "Attention : LE PIÈGE DU MIXAGE (RÈGLE CRUCIALE)",
            "accent": "indigo",
            "paragraphs": [
                ("LE CAUCHEMAR DES MORCEAUX DE BANANE :", "Si vous écrasez la banane à la fourchette, des millions de micro-morceaux blanchâtres vont s'incruster dans vos boucles 4C. En séchant, ils durcissent comme de la colle et vous obligent à arracher vos cheveux au peigne pour les enlever."),
                ("La seule méthode autorisée :", "1. Mixer la banane et l'avocat au blender électrique avec 2 cuillères à soupe d'eau ou de gel de gombo jusqu'à obtenir une crème liquide sans aucun grain.\n2. Filtrer obligatoirement à travers un bas en nylon / collant propre !"),
                ("Dose :", "½ banane + ¼ d'avocat + 1 c. à café de miel. Poser 30 minutes, puis rincer abondamment.")
            ]
        },
        "callout": "Si vous n'avez pas de blender et de filtre, NE FAITES PAS de masque à la banane ! Optez pour le miel et l'huile d'olive."
    },

    # SLIDE 39 : FAMILLE 7 — SAVON NOIR AFRICAIN BÉNINOIS
    {
        "type": "two_card",
        "tracker": "Famille 7 · Les nettoyants ancestraux",
        "title": "Le Savon Noir africain traditionnel béninois",
        "subtitle": "Badge : ○ TRADITION  ·  La détoxification pure du cuir chevelu sans aucun sulfate industriel.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "indigo",
            "paragraphs": [
                ("La saponification potassique ancestrale :", "Fabriqué à base de cendres de peaux de bananes plantain, cabosses de cacao et huile de palmiste ou karité. C'est un savon naturellement riche en glycérine."),
                ("Purification en profondeur :", "Dissout les accumulations d'huiles oxydées, la sueur et la poussière accumulées sous les tresses sans sulfates agressifs (SLS)."),
                ("Le revers de la médaille : son pH alcalin (pH 9-10) :", "Le savon noir a un pH basique. Il ouvre grand les écailles de la cuticule. C'est formidable pour nettoyer, mais désastreux si on ne referme pas les écailles ensuite !")
            ]
        },
        "card2": {
            "title": "Attention : LES 2 RÈGLES DE SÉCURITÉ ABSOLUES",
            "accent": "terra",
            "paragraphs": [
                ("RÈGLE 1 : NE JAMAIS FROTTER LE MORCEAU PUR SUR LA TÊTE :", "Prenez 1 petite cuillère à café de savon noir émietté et dissolvez-la dans 1 grand verre d'eau tiède (250 ml). Utilisez uniquement cette eau mousseuse sur vos racines !"),
                ("RÈGLE 2 : LE RINÇAGE ACIDE EST OBLIGATOIRE :", "Après avoir rincé le savon noir à l'eau claire, appliquez immédiatement un rinçage au vinaigre de cidre (1 c. à soupe par verre d'eau). Le vinaigre neutralise le pH alcalin et referme les écailles en 30 secondes."),
                ("Fréquence :", "1 fois tous les 15 jours (ou 1 fois par mois)."),
                ("Coût :", "200 FCFA la boule pour 6 mois d'utilisation.")
            ]
        },
        "callout": "À RETENIR : Savon noir dilué + Rinçage acide au vinaigre = Le duo nettoyant le plus pur, sain et économique au monde."
    },

    # SLIDE 40 : FAMILLE 7 — ARGILES LOCALES (KAOLIN & RHASSOUL)
    {
        "type": "two_card",
        "tracker": "Famille 7 · La clarification minérale",
        "title": "Les Argiles minérales : Kaolin & Terre de barre",
        "subtitle": "Badge : ○ TRADITION  ·  Le lavage détoxifiant qui respecte le sébum naturel.",
        "card1": {
            "title": "L'action buvard électrostatique",
            "accent": "green",
            "paragraphs": [
                ("La charge négative des argiles :", "Les argiles possèdent des feuillets minéraux chargés négativement. Elles attirent comme un aimant les toxines, impuretés et excès de sébum chargés positivement."),
                ("Nettoyage sans décapage lipidique :", "Contrairement aux tensioactifs qui décapent tout, l'argile respecte le film lipidique naturel de la fibre. Les boucles restent douces et définies dès la sortie du bain."),
                ("Le Kaolin béninois (argile blanche) :", "C'est l'argile la plus douce et la plus neutre. Idéale pour les cuirs chevelus secs et sensibles.")
            ]
        },
        "card2": {
            "title": "Recette de la crème lavante minérale",
            "accent": "gold",
            "paragraphs": [
                ("La recette onctueuse :", "3 cuillères à soupe de poudre de kaolin + 1 verre d'eau tiède (ou infusion de bissap) + 1 cuillère à café d'huile de coco."),
                ("Attention : Règle d'or de manipulation :", "N'utilisez jamais d'ustensile ou de cuillère en métal pour manipuler l'argile (le métal décharge les propriétés ioniques de l'argile). Utilisez du bois, du verre ou du plastique !"),
                ("Temps de pose :", "10 minutes sur le cuir chevelu. Rincez abondamment avant que l'argile ne sèche complètement et ne devienne dure comme de la pierre.")
            ]
        },
        "callout": "Une clarification à l'argile une fois par mois remet les compteurs à zéro et redonne toute leur brillance aux cheveux saturés d'huiles."
    },

    # SLIDE 41 : FAMILLE 8 — LE VINAIGRE DE CIDRE
    {
        "type": "two_card",
        "tracker": "Famille 8 · Le régulateur de pH souverain",
        "title": "Le Vinaigre de Cidre de pomme (pH 3,5)",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  Le flacon le plus indispensable de toute votre salle de bain.",
        "card1": {
            "title": "Ce qu'il fait et POURQUOI ça marche",
            "accent": "terra",
            "paragraphs": [
                ("L'acidité physiologique parfaite (pH 3 à 3,5) :", "Le cheveu et le cuir chevelu ont un pH naturellement acide (entre 4,5 et 5,5). Le savon, l'eau du robinet et la transpiration élèvent ce pH et ouvrent les écailles."),
                ("Le resserrement instantané des écailles :", "L'acide acétique contenu dans le vinaigre de cidre contracte la cuticule. Les écailles se plaquent hermétiquement les unes sur les autres."),
                ("L'élimination totale du calcaire de forage :", "Le vinaigre dissout les ions calcium et magnésium déposés par l'eau dure de Cotonou et fait briller le cheveu comme un miroir."),
                ("Action antipelliculaire :", "Empêche la prolifération du champignon Malassezia responsable des pellicules.")
            ]
        },
        "card2": {
            "title": "Dosage, Application & Démystification de l'odeur",
            "accent": "indigo",
            "paragraphs": [
                ("LA PROPORTION EXACTE :", "1 cuillère à soupe de vinaigre de cidre pour 1 grand verre d'eau tiède (250 ml). Ne JAMAIS l'utiliser pur sous peine de brûler le cuir chevelu !"),
                ("Mode d'emploi :", "Versez lentement en dernier rinçage sur vos longueurs après avoir rincé vos masques. Ne rincez pas à l'eau du robinet ensuite (vous redéposeriez du calcaire) !"),
                ("La question de l'odeur :", "Rassurez-vous : l'odeur de vinaigre s'évapore totalement et disparaît dès que les cheveux sont secs. Vous ne sentirez pas la salade !"),
                ("Coût :", "30 FCFA par rinçage (bouteille à 800 FCFA).")
            ]
        },
        "callout": "À RETENIR : Si vous ne deviez garder qu'un seul produit de ce chapitre avec le karité, ce serait le vinaigre de cidre. Il change vos cheveux dès la première minute."
    },

    # SLIDE 42 : FAMILLE 9 — POUDRES DE MORINGA & NEEM
    {
        "type": "two_card",
        "tracker": "Famille 9 · Poudres végétales purifiantes",
        "title": "Poudres de Moringa & Neem local",
        "subtitle": "Badge : ◐ PROMETTEUR  ·  La santé de la racine par les feuilles médicinales.",
        "card1": {
            "title": "La Poudre de Feuilles de Moringa",
            "accent": "green",
            "paragraphs": [
                ("L'arbre aux miracles du Bénin :", "Les feuilles séchées et broyées de Moringa oleifera sont l'aliment végétal le plus concentré en nutriments au monde (vitamines A, B, fer, zinc, acides aminés soufrés)."),
                ("Action en masque racine :", "Nourrit directement la circulation sanguine péricapillaire et fortifie la kératine naissante à la racine."),
                ("Recette :", "1 cuillère à soupe de poudre de moringa mélangée à 3 cuillères à soupe d'eau tiède et 1 cuillère à café d'huile de coco. Poser 15 minutes avant le lavage.")
            ]
        },
        "card2": {
            "title": "La Poudre de Feuilles de Neem (Azadirachta indica)",
            "accent": "terra",
            "paragraphs": [
                ("L'antifongique naturel le plus puissant d'Afrique :", "Le neem (margousier) contient de l'azadirachtine et de la nimbidine, deux molécules destructrices de champignons et bactéries."),
                ("L'éradication des pellicules et gratouilles :", "Élimine les pellicules tenaces, calme les démangeaisons intolérables et assainit les racines étouffées."),
                ("Posologie :", "1 cuillère à café dans votre shampoing doux ou votre masque clarifiant. Utiliser tous les 15 jours jusqu'à disparition complète des pellicules.")
            ]
        },
        "callout": "Ces deux poudres se trouvent sur tous les marchés traditionnels ou se fabriquent gratuitement en pilant des feuilles de sa cour séchées à l'ombre."
    },

    # SLIDE 43 : FAMILLE 10 — HUILES ESSENTIELLES (DILUTION STRICTE)
    {
        "type": "two_card",
        "tracker": "Famille 10 · Les essences concentrées",
        "title": "Huiles Essentielles : Romarin, Menthe & Tea Tree",
        "subtitle": "Badge : ● ÉTAYÉ / ◐ PROMETTEUR  ·  Des actifs surpuissants à doser à la goutte près.",
        "card1": {
            "title": "Les trois essences reines de la chevelure",
            "accent": "indigo",
            "paragraphs": [
                ("HE de Romarin à cinéole (◐ PROMETTEUR) :", "L'étude Panahi et al. (2015) a comparé l'huile de romarin au minoxidil 2 % pendant 6 mois : résultats comparables sur la densité capillaire avec moins de démangeaisons."),
                ("HE de Menthe poivrée (◐ PROMETTEUR) :", "Le menthol dilate les micro-vaisseaux sanguins du cuir chevelu et procure une sensation de fraîcheur vivifiante immédiate."),
                ("HE de Tea Tree / Arbre à thé (● ÉTAYÉ) :", "L'antifongique le plus documenté au monde contre les pellicules et la dermatite séborrhéique.")
            ]
        },
        "card2": {
            "title": "Attention : RÈGLE DE DILUTION ABSOLUE AU MILLIMÈTRE",
            "accent": "terra",
            "paragraphs": [
                ("JAMAIS PURE SUR LA PEAU :", "Une seule goutte d'huile essentielle pure sur le crâne peut provoquer une brûlure chimique sévère, un eczéma ou une chute de cheveux irréversible."),
                ("La règle de dilution à 1 % (la seule sûre) :", "3 à 6 gouttes d'huile essentielle MAXIMUM pour 2 grandes cuillères à soupe (30 ml) d'huile végétale support (coco ou olive)."),
                ("Interdictions formelles :", "• Femmes enceintes et allaitantes (interdiction absolue).\n• Enfants de moins de 7 ans.\n• Toujours faire le test au creux du coude 24h avant !")
            ]
        },
        "callout": "Une fiole de 10 ml d'huile essentielle dure plus d'une année. Comptez vos gouttes : la puissance est dans la retenue."
    },

    # SLIDE 44 : TABLEAU MAÎTRE COMPLET DES 25 INGRÉDIENTS
    {
        "type": "table",
        "tracker": "Partie 2 · Chapitre 11 — Synthèse générale",
        "title": "Le Tableau Maître des 25 ingrédients de cuisine",
        "subtitle": "La double page de référence à garder en mémoire pour chaque soin.",
        "headers": ["Ingrédient", "Ce qu'il fait (POURQUOI)", "Quantité repère", "Fréquence", "Précaution clé"],
        "rows": [
            ["Huile de coco", "Pénètre le cortex (-40 % perte protéines)", "1 c. à c. à 1 c. à s.", "Avant chaque lavage", "Fige sous 24 °C ; sur cheveux secs"],
            ["Beurre de karité", "Scelle l'eau dans la fibre, anti-harmattan", "1 noisette à 2 noix", "2 à 3× / semaine", "Toujours sur cheveux humides"],
            ["Huile d'olive", "Assouplit la cuticule, élimine le rêche", "1 à 2 c. à soupe", "1× / semaine", "Choisir vierge pressée à froid"],
            ["Huile de ricin", "Gaine et épaissit la tige (illusion pousse)", "½ c. à c. DILUÉE", "1 à 2× / semaine", "Toujours diluer 1:2 dans huile fluide"],
            ["Gel de gombo", "Démêlant n°1 : mucilage glissant magique", "1 à 4 c. à soupe", "À chaque démêlage", "Garder 4 jours max au frigo"],
            ["Graines de lin", "Définit les boucles et twists sans cartonner", "2 c. à s. / 1 verre d'eau", "1 à 2× / semaine", "Filtrer à chaud au collant"],
            ["Aloé vera frais", "Hydratation 98 % d'eau pure, apaise le crâne", "2 c. à s. gel cristal", "2 à 3× / semaine", "Éliminer le suc jaune (aloïne)"],
            ["Miel pur local", "Humectant suprême : capte l'eau ambiante", "1 c. à c. dans masques", "1× / semaine", "Toujours sceller au karité ensuite"],
            ["Œuf entier", "Protéines d'urgence : répare les fissures", "1 œuf + 1 c. s. huile", "1× / mois max", "Rincer à l'eau TIÈDE uniquement !"],
            ["Yaourt nature", "Acide lactique lissant, clarifie le crâne", "4 c. à s. + 1 c. c. miel", "1× tous les 15 jours", "Bien rincer (odeur résiduelle)"],
            ["Savon noir local", "Nettoie à fond sans sulfates industriels", "1 c. à c. dans 1 verre d'eau", "1× tous les 15 jours", "Toujours DILUÉ + rinçage vinaigre"],
            ["Vinaigre de cidre", "pH 3,5 : referme écailles, dissout le calcaire", "1 c. à s. / 1 verre d'eau", "À chaque shampoing", "Ne jamais utiliser pur ; ne pas rincer"]
        ],
        "callout": "Consultez cette table pour composer votre routine en 10 secondes : 1 nettoyant + 1 hydratant + 1 scellant."
    },

    # SLIDE 45 : LES 8 FAUX AMIS CAPITAUX
    {
        "type": "four_boxes",
        "tracker": "Partie 2 · Chapitre 11 — Dangers & Erreurs graves",
        "title": "Les 8 faux amis et erreurs dangereuses à bannir",
        "subtitle": "Ce qui circule partout sur Internet et abîme pourtant irrémédiablement vos cheveux.",
        "box1": ("1. Le Bicarbonate & 2. Le Citron pur", "Agression chimique brutale", "• Bicarbonate de soude (pH 9) : Décape la cuticule, soulève violemment les écailles et rend le cheveu cassant comme du verre.\n• Jus de citron pur : pH trop agressif et photosensibilisant sous le soleil d'Afrique. Brûle le cheveu."),
        "box2": ("3. HE pures & 4. Henné métallique", "Brûlures et réactions chimiques", "• Huiles essentielles pures : Brûlures chimiques au 2nd degré sur le crâne et chute massive.\n• Henné contenant des sels métalliques sur cheveux défrisés ou teints : Réaction thermique explosive qui désagrège la fibre."),
        "box3": ("5. Gros sel & 6. Colles à perruques", "Arrachage mécanique et étouffement", "• Friction au gros sel : Abrasion mécanique sauvage du cuir chevelu qui détruit les follicules naissants.\n• Colles à perruque posées sur la lisière : Asphyxie totale du bulbe et alopécie de traction irréversible."),
        "box4": ("7. Pots avariés & 8. Peigne sur 4C sec", "Infections et arrachage pur", "• Préparations maison gardées 3 semaines à température ambiante : Nids à staphylocoques et moisissures.\n• Démêler un afro 4C sec au peigne fin : Arrachage mécanique garanti de 500 cheveux sains à chaque passage.")
    }
]
