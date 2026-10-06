# -*- coding: utf-8 -*-
"""Contenu — pages d'ouverture, mesures, tableau maître, faux amis."""

META = dict(
    titre="Ma couronne, mes règles",
    sous_titre="Le guide des cheveux texturés en Afrique : comprendre ses cheveux et en prendre soin avec ce qu'on a dans sa cuisine",
    extrait="EXTRAIT — Version de travail pour relecture",
    date="Octobre 2026 · Document de travail v1",
    autrice="[NOM DE L'AUTRICE À COMPLÉTER]",
    mention=("Ma couronne, mes règles — Extrait (12 fiches ingrédients + Kit anti-paresse). "
             "Document de travail destiné à la relecture et à la correction, avant mise en page définitive. "
             "© 2026, [autrice]. Tous droits réservés. Reproduction interdite sans autorisation écrite."),
    images=("Illustrations et photographies : visuels d'intention (générés pour la maquette), "
            "à remplacer par les photographies originales prises au Bénin."),
)

# ---------------------------------------------------------------- ÉDITO
EDITO_TITRE = "Pourquoi ce guide existe"
EDITO = [
    "Vous avez déjà essayé. Vous avez acheté le petit pot qui coûte 8 000 FCFA, vous l'avez utilisé trois fois, "
    "et vos cheveux ont continué de casser. Ce guide existe pour vous sortir de là.",
    "Il part d'un constat simple : nos cheveux ne demandent pas plus d'argent, ils demandent plus de "
    "<b>compréhension</b>. Un cheveu texturé en spirale sèche par nature, parce que le sébum du crâne ne descend "
    "pas le long de la tige. Ce n'est pas un défaut : c'est une architecture. Quand on sait comment elle "
    "fonctionne, on arrête de se battre contre ses cheveux et on se met à travailler avec eux.",
    "Ce guide est donc construit autour de trois questions que les autres documents laissent sans réponse :",
]
EDITO_3Q = [
    ("POURQUOI ?", "Ce que chaque ingrédient fait réellement au cheveu : le mécanisme, expliqué simplement. "
                   "Pas « c'est bon pour les cheveux », mais « voilà ce qu'il fait, et voilà pourquoi »."),
    ("COMBIEN ?", "Des quantités exactes, mesurées avec ce que vous avez chez vous : la cuillère à café, "
                  "la cuillère à soupe, le verre d'eau, la noix de karité — et des quantités différentes selon "
                  "la longueur de vos cheveux. Jamais « un peu d'huile »."),
    ("À QUELLE FRÉQUENCE ?", "Le bon rythme pour chaque geste : une fois par semaine, une fois par mois, "
                             "ou jamais deux fois de suite. C'est la fréquence qui change tout, pas la quantité de produits."),
]
EDITO_FIN = (
    "Un mot, maintenant, sur ce que ce guide ne fera pas. Il ne fera pas pousser vos cheveux plus vite : "
    "le cheveu pousse de 0,8 à 1,25 cm par mois, c'est la biologie, et aucune huile au monde ne change cela. "
    "Il ne remplacera pas un médecin si votre cuir chevelu est malade. Et il ne travaillera pas à votre place : "
    "la régularité de dix minutes vaut toujours mieux qu'une séance héroïque de trois heures tous les six mois. "
    "Mais il vous donnera ce que personne ne vous a donné : les gestes justes, dans le bon ordre, à la bonne fréquence, "
    "pour le type de cheveux qui est le vôtre."
)

COMMENT_TITRE = "Comment lire ce guide"
COMMENT_INTRO = ("Chaque affirmation de ce guide porte un badge de preuve. Nous n'avons pas la même honnêteté "
                 "partout, parce que la science n'a pas le même niveau de preuve partout — et vous avez le droit de le savoir.")
BADGES = [
    ("etaye", "ÉTAYÉ", "Des études existent sur l'être humain (essais cliniques, mesures de laboratoire). On peut compter dessus."),
    ("prometteur", "PROMETTEUR", "Quelques études seulement, ou des études limitées (petits groupes, résultats non confirmés). Piste sérieuse, pas certitude."),
    ("tradition", "TRADITION", "Un usage très ancien et très répandu en Afrique, qui n'a pas été étudié. On l'utilise avec plaisir, mais on ne prétend pas que c'est prouvé."),
]
PICTOS = [
    ("quantite", "QUANTITÉ", "ce qu'il faut prendre, exactement"),
    ("frequence", "FRÉQUENCE", "à quel rythme le refaire"),
    ("duree", "TEMPS", "temps de pose ou de préparation"),
    ("alerte", "ATTENTION", "précaution, contre-indication"),
]
AVERTISSEMENT = (
    "<b>Avertissement.</b> Ce guide est un document d'information et d'éducation à la santé. Il ne remplace pas "
    "l'avis d'un médecin, d'un dermatologue ou d'un professionnel de santé. Certaines situations ne se soignent pas "
    "à la maison : chute de cheveux soudaine et en plaques, douleur du cuir chevelu, plaies, croûtes qui s'étendent, "
    "boutons, pus, brûlure après un défrisage ou un soin, lisière qui ne repousse pas après six mois sans tension. "
    "Dans ces cas, consultez. Les quantités et fréquences indiquées ici ont été établies pour des cheveux sains : "
    "en cas de grossesse, d'allaitement, d'allergie connue ou de maladie du cuir chevelu, demandez un avis avant d'appliquer."
)

# ---------------------------------------------------------------- MESURES
MESURES_TITRE = "La page des mesures"
MESURES_INTRO = ("Tout le guide est écrit avec quatre repères seulement. Si vous n'avez pas de cuillères-doseuses, "
                 "découpez les gabarits en bas de cette page : ils sont à taille réelle.")
MESURES_EQUIV = [
    ("1 cuillère à café (rase)", "5 ml", "≈ 5 g d'huile · ≈ 4 g de beurre", "≈ une noisette"),
    ("1 cuillère à soupe (rase)", "15 ml = 3 c. à café", "≈ 14 g d'huile · ≈ 12 g de beurre", "≈ une grosse noix"),
    ("1 verre d'eau ordinaire", "250 ml", "—", "1 tasse à thé moyenne"),
    ("1 bouchon de bouteille d'huile", "5 à 7 ml", "≈ 1,2 c. à café", "à défaut de cuillère"),
    ("1 noisette de beurre", "≈ 3 ml", "≈ 2 g", "effleurer le pot avec 2 doigts"),
    ("1 noix de beurre", "≈ 7 ml", "≈ 5 g", "une cuillère à café bombée"),
    ("1 c. à café d'huile essentielle", "≈ 100 gouttes", "—", "ne jamais l'utiliser pure"),
]
MESURES_QTE = [
    ("Pré-poo à l'huile", "1 c. à café", "2 c. à café", "1 c. à soupe"),
    ("Bain d'huile chaud", "2 c. à café", "1 c. à soupe", "2 c. à soupes"),
    ("Masque hydratant", "2 c. à soupes", "4 c. à soupes", "6 c. à soupes"),
    ("Soin protéiné", "1 œuf + 1 c. à soupe d'huile", "1 œuf + 2 c. à soupes", "2 œufs + 2 c. à soupes"),
    ("Sans-rinçage (leave-in)", "½ c. à café", "1 c. à café", "2 c. à café"),
    ("Beurre de scellage", "1 noisette", "1 noix", "2 noix"),
    ("Gel de gombo ou de lin", "1 c. à soupe", "2 c. à soupes", "4 c. à soupes"),
    ("Massage du crâne", "½ c. à café", "1 c. à café", "1 c. à café"),
    ("Rinçage acide au vinaigre", "1 c. à soupe / 1 verre d'eau", "idem", "2 c. à soupes / 1 verre"),
]
MESURES_REGLES = [
    "<b>Trois ingrédients, pas plus</b>, pour votre première recette. On n'ajoute un ingrédient qu'après avoir compris l'effet des trois premiers.",
    "<b>Une dose = une application.</b> Si vous préparez pour plusieurs personnes, multipliez — sinon, ne préparez pas « pour la semaine ».",
    "<b>Sans conservateur, ça s'abîme.</b> Tout ce que vous préparez à la maison (masques, gels, infusions) se garde au réfrigérateur, et pas plus de 3 à 5 jours pour les préparations à base d'eau ou de mucilage.",
    "<b>Testez avant d'appliquer.</b> Une goutte sur le pli du coude ou derrière l'oreille, 24 à 48 h avant : c'est la règle pour tout ingrédient nouveau, et une obligation pour les huiles essentielles et les œufs.",
]

# ---------------------------------------------------------------- TABLEAU MAÎTRE
MASTER_TITRE = "Le tableau maître"
MASTER_INTRO = ("Les 12 ingrédients de cet extrait, en une page. Photocopiez-la, collez-la au mur de la salle de bain : "
                "c'est votre aide-mémoire quotidien.")
MASTER_HEAD = ["Ingrédient", "Ce qu'il fait (et pourquoi)", "Pour quels cheveux", "Quantité", "Fréquence", "La précaution qui compte"]
MASTER_ROWS = [
    ("Huile de coco<br/><font size=7>● ÉTAYÉ</font>",
     "Seule huile courante qui pénètre la fibre : réduit la perte de protéines au lavage (étude 2003, jusqu'à −40 %).",
     "Tous types · porosité haute · cheveux abîmés",
     "1 c. à café à 1 c. à soupe",
     "Avant chaque shampooing",
     "Devient solide sous 24 °C : tiédir, jamais au feu."),
    ("Beurre de karité<br/><font size=7>○ TRADITION</font>",
     "Occlusif : ne nourrit pas, retient l'eau déjà dans le cheveu et le protège du vent et du soleil.",
     "Types 4 · cheveux très secs · porosité haute",
     "1 noisette à 2 noix",
     "1 à 2 fois / semaine",
     "Toujours sur cheveu humide ; sinon il scelle la sécheresse."),
    ("Huile de ricin<br/><font size=7>◐ PROMETTEUR</font>",
     "Très épaisse, gaine la tige : effet cheveu plus épais. Ne fait pas pousser plus vite.",
     "Cheveux fins · racines fragiles",
     "½ c. à café, diluée dans 2 × d'huile fluide",
     "1 fois / semaine maximum",
     "Jamais pure : elle colle et arrache au démêlage."),
    ("Huile d'olive<br/><font size=7>◐ PROMETTEUR</font>",
     "Adoucit la cuticule et facilite le démêlage ; plus lourde que la coco.",
     "Cheveux secs et rêches · porosité basse",
     "1 c. à café à 2 c. à soupes",
     "1 fois / semaine",
     "Alourdit : éviter si le crâne est gras."),
    ("Gombo<br/><font size=7>○ TRADITION</font>",
     "Le mucilage gaine la tige et fait glisser les mèches : démêlant naturel, sans graisser.",
     "Tous types · roi du 4C · enfants",
     "1 à 4 c. à soupes de gel",
     "1 à 2 fois / semaine",
     "Se garde 3 à 5 jours au frigo, pas plus."),
    ("Graines de lin<br/><font size=7>○ TRADITION</font>",
     "Gel de polysaccharides : démêle et fixe la boucle sans effet carton.",
     "Types 3 et 4 · vanilles · twists",
     "2 c. à soupes de graines / 1 verre d'eau",
     "1 à 2 fois / semaine",
     "Se conserve 1 à 2 semaines au frigo uniquement."),
    ("Aloé vera<br/><font size=7>○ TRADITION</font>",
     "98 % d'eau + polysaccharides apaisants : réhydrate le cuir chevelu, calme les démangeaisons.",
     "Crâne irrité ou sec · sous tresses",
     "1 c. à soupe de gel frais",
     "2 à 3 fois / semaine (crâne)",
     "Gel frais de la feuille ; 5 à 7 jours au frigo."),
    ("Miel<br/><font size=7>◐ PROMETTEUR</font>",
     "Humectant : attire et retient l'eau. Adoucit et assouplit la cuticule.",
     "Cheveux secs et rêches · tous types",
     "1 c. à café pour 2 c. à soupes de masque",
     "Dans les masques, 1 fois / semaine",
     "Miel pur et local ; par temps très sec, toujours sceller ensuite."),
    ("Œuf<br/><font size=7>◐ PROMETTEUR</font>",
     "Protéines déposées sur les zones abîmées : effet « cheveu plus épais » temporaire.",
     "Cheveux cassants · après défrisage ou coloration",
     "1 œuf + 1 c. à soupe d'huile + 1 c. à café de miel",
     "1 fois / mois (2 si très abîmé)",
     "Rincer à l'eau tiède, jamais chaude : l'œuf cuirait."),
    ("Yaourt nature<br/><font size=7>○ TRADITION</font>",
     "Acide lactique : referme les écailles, dissout les résidus, nettoie le crâne en douceur.",
     "Pellicules grasses · crâne qui gratte · cheveu terne",
     "4 c. à soupes + 1 c. à soupe de miel",
     "1 fois / 2 semaines",
     "Rincer soigneusement (odeur) ; pas sur un crâne à vif."),
    ("Savon noir<br/><font size=7>○ TRADITION</font>",
     "Nettoie fort et dégraisse ; pH élevé (9-10) qui ouvre les écailles.",
     "Crâne gras · résidus de produits",
     "1 c. à café diluée dans 1 verre d'eau tiède",
     "1 fois / semaine à / 2 semaines",
     "Jamais pur, et toujours suivi d'un rinçage acide."),
    ("Vinaigre de cidre<br/><font size=7>◐ PROMETTEUR</font>",
     "pH acide : referme les écailles et dissout les dépôts de calcaire de l'eau dure.",
     "Eau dure · cheveux ternes · après savon noir",
     "1 c. à soupe pour 1 verre d'eau",
     "1 fois / semaine à 1 fois / mois",
     "Ne pas laisser poser ; jamais sur un crâne à vif."),
]

# ---------------------------------------------------------------- FAUX AMIS
FAUX_AMIS_TITRE = "Les 8 faux amis"
FAUX_AMIS_INTRO = ("Ces huit-là circulent partout, souvent avec de bonnes intentions. Ce sont les erreurs qui font "
                   "le plus de dégâts et coûtent le plus cher, en argent comme en cheveux.")
FAUX_AMIS = [
    ("Le bicarbonate de soude dans le shampooing",
     "Son pH est très élevé : il soulève les écailles, laisse le cheveu rêche et cassant, et abîme le cuir chevelu. "
     "« Shampooing naturel » ne veut pas dire « shampooing doux »."),
    ("Le citron pur sur le cuir chevelu ou dans les longueurs",
     "Beaucoup trop acide non dilué, et photosensibilisant : le soleil du Bénin transforme le citron en brûlure. "
     "Bénéfice réel : nul. Risque : élevé."),
    ("Les huiles essentielles pures sur le crâne",
     "Une huile essentielle non diluée peut brûler le cuir chevelu et laisser une plaque douloureuse pendant des semaines. "
     "Toujours 2 à 6 gouttes pour 2 cuillères à soupe d'huile — pas une goutte de plus."),
    ("Le henné sur des cheveux fraîchement colorés ou défrisés",
     "Les deux réagissent : démangeaisons, sensation d'étirement, chute par cassure. Respectez 4 à 6 semaines entre les deux, "
     "et faites toujours un test sur une mèche."),
    ("Le sel ou le gros sel « pour faire pousser »",
     "Aucun effet sur la pousse, et une irritation garantie. Le sel dessèche et abîme la fibre."),
    ("Les colles à perruque posées sur la peau du crâne",
     "Allergies fréquentes, souvent graves, et une lisière qui souffre. Préférez les bandeaux et les perruques à ajustement, "
     "et changez régulièrement de zone d'appui."),
    ("Les préparations maison gardées des semaines",
     "Sans conservateur, une préparation à base d'eau devient un bouillon de bactéries et de moisissures : ça sent aigre, "
     "ça gratte, ça provoque des boutons. Le frigo, 3 à 5 jours, puis on jette."),
    ("Le peigne chaud et les lissages très chauds sur cheveux secs",
     "L'eau est le premier bouclier du cheveu : une chaleur forte sur cheveu sec casse la cuticule définitivement. "
     "Ce n'est pas réparable, seulement coupé."),
]
