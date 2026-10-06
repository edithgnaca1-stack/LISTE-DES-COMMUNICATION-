# -*- coding: utf-8 -*-
"""
Ma couronne, mes règles — Extrait (12 fiches ingrédients + Kit anti-paresse)
Générateur de PDF (ReportLab / Platypus).
Sortie : MA-COURONNE-MES-REGLES-extrait-v1.pdf
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, Color
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                               Table, TableStyle, Image, KeepTogether, Flowable, PageBreak,
                               CondPageBreak, NextPageTemplate)

from c_intro import *
from c_fiches import FICHES, BONUS, COMBINE
from c_kit import *

# ------------------------------------------------------------------ ressources
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "images")
OUT = os.path.join(HERE, "MA-COURONNE-MES-REGLES-extrait-v1.pdf")

DEJA = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Body", f"{DEJA}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("BodyB", f"{DEJA}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Btn", f"{DEJA}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("Head", f"{DEJA}/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("HeadB", f"{DEJA}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="BodyB", italic="Body", boldItalic="BodyB")
pdfmetrics.registerFontFamily("Head", normal="Head", bold="HeadB", italic="Head", boldItalic="HeadB")

# ------------------------------------------------------------------ palette
INDIGO = HexColor("#2B3E63")
INDIGO_D = HexColor("#1B2740")
OR = HexColor("#B8862B")
OR_L = HexColor("#D9A13B")
KARITE = HexColor("#F1E4CE")
KARITE_L = HexColor("#FBF5EA")
SABLE = HexColor("#FDFAF4")
TERRA = HexColor("#A85236")
GOMBO = HexColor("#55663A")
ENCRE = HexColor("#1C1B19")
GRIS = HexColor("#6E6A62")
BORD = HexColor("#E2D7C4")
VERT_F = HexColor("#E9F4EA"); VERT_T = HexColor("#1F5C2E")
AMB_F = HexColor("#FDF3E0"); AMB_T = HexColor("#8A5A00")
OLI_F = HexColor("#EEF2E4"); OLI_T = HexColor("#4F6132")
BLEU_F = HexColor("#EDF1F7")

PREUVES = {
    "etaye": ("● ÉTAYÉ", "études humaines disponibles", VERT_F, VERT_T),
    "prometteur": ("◐ PROMETTEUR", "quelques études, à confirmer", AMB_F, AMB_T),
    "tradition": ("○ TRADITION", "usage ancien, non étudié", OLI_F, OLI_T),
}

# ------------------------------------------------------------------ styles
def st(name, **kw):
    base = dict(fontName="Body", fontSize=8.4, leading=10.6, textColor=ENCRE, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(name, **base)

S_BODY = st("body", spaceAfter=3)
S_BODY_J = st("bodyj", alignment=TA_JUSTIFY, spaceAfter=3)
S_SMALL = st("small", fontSize=7.2, leading=9.2, textColor=GRIS)
S_SMALL_N = st("smalln", fontSize=7.6, leading=9.6)
S_H2 = st("h2", fontName="HeadB", fontSize=19, leading=21, textColor=INDIGO, spaceAfter=2)
S_H3 = st("h3", fontName="HeadB", fontSize=12.5, leading=14.5, textColor=INDIGO, spaceAfter=2)
S_SUB = st("sub", fontSize=7.4, leading=9.4, textColor=GRIS)
S_LAB = st("lab", fontName="BodyB", fontSize=6.4, leading=8, textColor=TERRA)
S_BOX = st("box", fontName="BodyB", fontSize=8.2, leading=10, textColor=INDIGO, spaceAfter=2)
S_TBLH = st("tblh", fontName="BodyB", fontSize=7, leading=8.6, textColor=HexColor("#4A3A22"))
S_TBLC = st("tblc", fontSize=7.1, leading=8.8)
S_TBLCB = st("tblcb", fontName="BodyB", fontSize=7.1, leading=8.8)
S_CHIP = st("chip", fontSize=7.2, leading=9, textColor=INDIGO)
S_RET = st("ret", fontSize=8.6, leading=10.8, textColor=KARITE_L)
S_LEDE = st("lede", fontSize=9.6, leading=12.6, textColor=HexColor("#3A3630"))
S_BULL = st("bull", fontSize=8.1, leading=10.2, leftIndent=9, bulletIndent=0)
S_BULLS = st("bulls", fontSize=7.4, leading=9.4, leftIndent=9, bulletIndent=0)
S_NUM = st("num", fontSize=8.1, leading=10.4, leftIndent=10, bulletIndent=0)

def hx(c):
    """couleur reportlab -> '#rrggbb' pour le balisage des paragraphes"""
    v = c.hexval()
    return "#" + v[2:] if v.startswith("0x") else v

def P(txt, style=S_BODY):
    return Paragraph(txt, style)

def bullets(items, style=S_BULL, mark="●", color=None):
    out = []
    for it in items:
        s = style
        if color:
            s = ParagraphStyle(f"{style.name}_{color}", parent=style, bulletColor=color)
        out.append(Paragraph(it, s, bulletText=mark))
    return out

def numbered(items, style=S_NUM):
    return [Paragraph(t, style, bulletText=f"{i+1}.") for i, t in enumerate(items)]

# ------------------------------------------------------------------ éléments
def rule(color=OR, thick=1.1, width=None, space=4):
    t = Table([[""]], colWidths=[width or 503], rowHeights=[0.6])
    t.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), thick, color),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return [Spacer(1, space), t, Spacer(1, space + 2)]

def filet(texte, color=OR):
    """petit intitulé de section, façon 'chapeau'"""
    t = Table([[Paragraph(f'<font color="#B8862B"><b>{texte.upper()}</b></font>', S_LAB), ""]],
              colWidths=[None, None])
    return Paragraph(f'<font color="#B8862B" size=6.6><b>{texte.upper()}</b></font>', S_LAB)

def encadre(titre, flows, coul=INDIGO, bg=white, width=251, titre_coul=None):
    inner = []
    if titre:
        tc = titre_coul or coul
        inner.append(Paragraph(f'<font color="{hx(tc)}"><b>{titre.upper()}</b></font>', S_BOX))
    inner += flows
    t = Table([[inner]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.5, BORD),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, coul),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t

def badge(preuve, size=7.0):
    lab, desc, bg, fg = PREUVES[preuve]
    return Paragraph(f'<font color="{hx(fg)}"><b>{lab}</b></font> '
                     f'<font color="#6E6A62" size={size-0.6}>{desc}</font>',
                     ParagraphStyle("bd", fontName="Body", fontSize=size, leading=size + 2.2,
                                    backColor=bg, borderColor=fg, borderWidth=0.5,
                                    borderPadding=3, textColor=fg))

def datatable(data, widths, head=True, fs=7.1, align="LEFT"):
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    style = [
        ("GRID", (0, 0), (-1, -1), 0.4, BORD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3.5), ("RIGHTPADDING", (0, 0), (-1, -1), 3.5),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if head:
        style += [("BACKGROUND", (0, 0), (-1, 0), KARITE),
                  ("LINEBELOW", (0, 0), (-1, 0), 0.7, OR)]
        for r in range(1, len(data)):
            if r % 2 == 0:
                style.append(("BACKGROUND", (0, r), (-1, r), KARITE_L))
    else:
        for r in range(len(data)):
            if r % 2 == 1:
                style.append(("BACKGROUND", (0, r), (-1, r), KARITE_L))
    t.setStyle(TableStyle(style))
    return t

def grid_boxes(items, ncols=2, width=251, bg=KARITE_L, coul=INDIGO):
    """petites cases libellé/valeur, présentées en grille"""
    cells = [[Paragraph(f'<b>{lab}</b>', ParagraphStyle("g1", fontName="BodyB", fontSize=6.6,
                                                       leading=8.2, textColor=TERRA)),
              Paragraph(val, ParagraphStyle("g2", fontSize=7.4, leading=9, textColor=INDIGO))]
             for lab, val in items]
    rows = []
    for i in range(0, len(cells), ncols):
        rows.append(cells[i:i + ncols])
    while rows and len(rows[-1]) < ncols:
        rows[-1].append([Paragraph(" ", S_SMALL), Paragraph(" ", S_SMALL)])
    t = Table(rows, colWidths=[width / ncols - 2] * ncols)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, BORD),
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t

def retiens(txt, width=251):
    t = Table([[Paragraph(f'<b>À RETENIR —</b> {txt}', S_RET)]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), INDIGO),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t

class Bookmark(Flowable):
    def __init__(self, key, title, level=0):
        Flowable.__init__(self); self.key = key; self.title = title; self.level = level
        self.width = 0; self.height = 0
    def draw(self):
        pass

def photo(path, width, height=None):
    img = Image(os.path.join(IMG, path))
    ratio = img.imageHeight / float(img.imageWidth)
    img.drawWidth = width
    img.drawHeight = height or width * ratio
    return img

# ------------------------------------------------------------------ document
TITRE_DOC = META["titre"]
PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 46, 46, 42, 40
FW = PAGE_W - ML - MR

class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
                                 leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB,
                                 title=f'{META["titre"]} — {META["extrait"]}',
                                 author=META["autrice"], subject="Guide des cheveux texturés en Afrique",
                                 creator="Ma couronne, mes règles — maquette", **kw)
        frame_std = Frame(ML, MB, FW, PAGE_H - MT - MB, id="std",
                          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[Frame(ML, MB, FW, PAGE_H - MT - MB, id="c")], onPage=self.cover),
            PageTemplate(id="std", frames=[frame_std], onPage=self.footer),
        ])
        self.toc = []

    def afterFlowable(self, flowable):
        if isinstance(flowable, Bookmark):
            self.canv.bookmarkPage(flowable.key)
            self.canv.addOutlineEntry(flowable.title, flowable.key, level=flowable.level, closed=False)
            self.toc.append((flowable.level, flowable.title, self.page))

    # ---------- couverture ----------
    def cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(HexColor("#F8F2E7")); canv.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        # bandeau haut
        canv.setFillColor(INDIGO); canv.rect(0, PAGE_H - 46, PAGE_W, 46, stroke=0, fill=1)
        canv.setFillColor(OR_L)
        canv.setFont("BodyB", 7.4)
        canv.drawCentredString(PAGE_W / 2, PAGE_H - 29, "GUIDE PRATIQUE  ·  CHEVEUX TEXTURÉS  ·  AFRIQUE  ·  BÉNIN")
        # frise de tresses dorée : bande latérale gauche + frise basse, hors du texte
        canv.setStrokeColor(OR); canv.setLineWidth(0.9)
        for x0 in (8, 20, 32):
            p = canv.beginPath(); p.moveTo(x0, 210)
            for k in range(1, 41):
                yy = 210 + k * 13
                p.lineTo(x0 + 6 * (1 if k % 2 else -1), yy)
            canv.drawPath(p, stroke=1, fill=0)
        for y0 in (216, 228):
            p = canv.beginPath(); p.moveTo(52, y0)
            for k in range(1, 76):
                xx = 52 + k * 7
                p.lineTo(xx, y0 + 6 * (1 if k % 2 else -1))
            canv.drawPath(p, stroke=1, fill=0)
        canv.setStrokeColor(OR); canv.setLineWidth(1.6)
        canv.line(46, PAGE_H - 66, PAGE_W - 46, PAGE_H - 66)
        # titre
        canv.setFillColor(INDIGO); canv.setFont("HeadB", 44)
        canv.drawString(46, PAGE_H - 135, "Ma couronne,")
        canv.drawString(46, PAGE_H - 182, "mes règles")
        canv.setFont("Head", 13.4); canv.setFillColor(HexColor("#3A3630"))
        canv.drawString(46, PAGE_H - 214, "Comprendre ses cheveux texturés et en prendre soin")
        canv.drawString(46, PAGE_H - 232, "avec ce qu'on a dans sa cuisine.")
        canv.setStrokeColor(BORD); canv.setLineWidth(0.8)
        canv.line(46, PAGE_H - 248, PAGE_W - 46, PAGE_H - 248)
        # image
        img = photo("cover_crop.png", 232)
        canv.drawImage(os.path.join(IMG, "cover_crop.png"), 46, 250, width=232,
                       height=img.drawHeight, mask=None)
        canv.setStrokeColor(BORD); canv.setLineWidth(0.8)
        canv.rect(46, 250, 232, img.drawHeight, stroke=1, fill=0)
        # les 4 promesses
        x = 300; y = 250 + img.drawHeight - 4
        promesses = [("POURQUOI ?", "Ce que chaque ingrédient fait vraiment au cheveu, expliqué simplement."),
                     ("COMBIEN ?", "Cuillères, verres, noix : des quantités exactes. Jamais « un peu d'huile »."),
                     ("À QUELLE FRÉQUENCE ?", "Chaque geste a son rythme : semaine, mois, saison."),
                     ("POUR QUELS CHEVEUX ?", "Types 2-3-4, porosité basse, moyenne ou haute.")]
        for t, d in promesses:
            canv.setFillColor(TERRA); canv.setFont("BodyB", 8)
            canv.drawString(x, y, t)
            canv.setFillColor(HexColor("#3A3630")); canv.setFont("Body", 8.4)
            words = d.split(); line = ""; yy = y - 13
            for w in words:
                test = (line + " " + w).strip()
                if canv.stringWidth(test, "Body", 8.4) > 244:
                    canv.drawString(x, yy, line); yy -= 11.4; line = w
                else:
                    line = test
            canv.drawString(x, yy, line)
            y = yy - 26
            canv.setStrokeColor(BORD); canv.setLineWidth(0.5)
            canv.line(x, y + 16, PAGE_W - 46, y + 16)
        # bandeau bas
        canv.setFillColor(INDIGO); canv.rect(0, 0, PAGE_W, 200, stroke=0, fill=1)
        canv.setFillColor(OR_L); canv.setFont("BodyB", 9)
        canv.drawString(46, 172, "EXTRAIT  ·  VERSION DE TRAVAIL POUR RELECTURE")
        canv.setFillColor(KARITE_L); canv.setFont("Body", 8.6)
        canv.drawString(46, 154, "12 fiches ingrédients  ·  le tableau maître  ·  les 8 faux amis")
        canv.drawString(46, 140, "le Kit anti-paresse  ·  la fiche des tresses protectrices  ·  les pages de travail")
        canv.setStrokeColor(OR_L); canv.setLineWidth(0.7)
        canv.line(46, 122, PAGE_W - 46, 122)
        canv.setFillColor(KARITE_L); canv.setFont("BodyB", 10)
        canv.drawString(46, 100, META["autrice"])
        canv.setFont("Body", 8.2); canv.setFillColor(HexColor("#C9BDAA"))
        canv.drawString(46, 86, META["date"])
        canv.drawString(46, 72, "© 2026. Reproduction interdite sans autorisation écrite.")
        canv.drawRightString(PAGE_W - 46, 72, "Page 1")
        canv.restoreState()

    # ---------- pied de page ----------
    def footer(self, canv, doc):
        canv.saveState()
        canv.setStrokeColor(BORD); canv.setLineWidth(0.6)
        canv.line(ML, MB - 14, PAGE_W - MR, MB - 14)
        canv.setFont("Body", 6.6); canv.setFillColor(GRIS)
        canv.drawString(ML, MB - 25, f'{TITRE_DOC} — extrait')
        canv.drawCentredString(PAGE_W / 2, MB - 25, "VERSION DE TRAVAIL · À CORRIGER")
        canv.drawRightString(PAGE_W - MR, MB - 25, f'page {doc.page}')
        canv.restoreState()

# ------------------------------------------------------------------ story
story = []
ADD = story.append
EXT = story.extend

# ============ 1. COUVERTURE (dessinée dans onPage)
ADD(Bookmark("cover", "Couverture"))
ADD(Spacer(1, 1))
ADD(Bookmark("sommaire", "Sommaire et mode d'emploi", 0))
ADD(NextPageTemplate("std"))
story.append(PageBreak())

# ============ 2. SOMMAIRE / MODE D'EMPLOI
EXT(rule())
ADD(P("Sommaire de cet extrait", S_H2))
ADD(P("Ce document est la <b>première partie</b> du guide complet « Ma couronne, mes règles ». Il contient tout ce "
      "qui se pratique : les fiches des 12 ingrédients essentiels, l'aide-mémoire à afficher, les gestes à éviter, "
      "et le programme pour passer à l'action. Il est fait pour être <b>corrigé</b> : une fiche de correction vous "
      "attend à la fin.", S_LEDE))
ADD(Spacer(1, 8))
SOMMAIRE = [
    ("Avant de commencer", "L'édito — pourquoi ce guide existe  ·  comment lire les badges de preuve  ·  avertissement"),
    ("1. La page des mesures", "Les 4 repères (c. à café, c. à soupe, verre, noix), les quantités selon la longueur des cheveux, et les 4 règles d'or du mélange"),
    ("2. Le tableau maître", "Les 12 ingrédients en une double page : ce qu'ils font, pour quels cheveux, combien, à quelle fréquence, et la précaution qui compte"),
    ("3. Les 12 fiches ingrédients", "Deux pages par famille d'ingrédients : pourquoi ça marche, la quantité exacte selon la longueur, la recette, les fréquences, les précautions, les 3 erreurs et la conservation"),
    ("4. L'eau de riz (bonus)", "Une cure prometteuse, trop souvent mal utilisée"),
    ("5. Les 8 faux amis", "Ce qui circule partout et abîme pourtant les cheveux : bicarbonate, citron pur, huiles essentielles pures, colles, henné…"),
    ("6. Le Kit anti-paresse", "Le défi 7 jours, le plan 30 jours à cocher, les 3 routines express, le filet de sécurité, les 5 règles d'or, les 9 signes que ça marche, le carnet de suivi"),
    ("7. Les tresses protectrices", "La fiche complète : durées, protocole avant-pendant-après, et la fiche à remettre à votre coiffeuse"),
    ("8. Vos pages de travail", "Les noms locaux à valider (fon, yoruba), votre fiche de correction, et le plan du guide complet"),
]
rows = [[Paragraph("<b>Section</b>", S_TBLH), Paragraph("<b>Ce qu'elle contient</b>", S_TBLH)]]
for a, b in SOMMAIRE:
    rows.append([Paragraph(f"<b>{a}</b>", S_TBLCB), Paragraph(b, S_TBLC)])
ADD(datatable(rows, [140, FW - 140]))
ADD(Spacer(1, 10))
EXT(rule())
ADD(encadre("Comment corriger ce document", [
    P("Vous n'avez pas à réécrire : il suffit de <b>citer la page et le numéro de fiche</b>.", S_BODY),
    P("Exemple : « page 12, fiche 3 — la dose de ricin me paraît trop faible »  ou  « page 4, "
      "remplacer “harmattan” par une formulation plus locale ».", S_SMALL_N),
    Spacer(1, 4),
    P("<b>Trois choses à vérifier en priorité</b> : les noms locaux des ingrédients (fon et yoruba), les prix en "
      "FCFA indiqués par application, et les quatre dosages marqués d'un astérisque dans les fiches.", S_BODY),
    Spacer(1, 4),
    P("À la fin du document : votre fiche de correction, à remplir à la main ou à recopier dans un message.", S_SMALL),
], coul=TERRA, width=FW))
ADD(Spacer(1, 8))
ADD(encadre("Ce que cet extrait est, et ce qu'il n'est pas", [
    P("<b>Il est</b> la partie pratique du guide : les recettes, les doses, les fréquences, les gestes interdits, "
      "le programme d'action.", S_BODY),
    P("<b>Il n'est pas</b> encore : l'introduction (la couronne, la fierté, l'histoire), le diagnostic des types "
      "de cheveux et de la porosité, le catalogue illustré des 12 coiffures protectrices, le chapitre "
      "« L'assiette cheveux », les 25 fiches complètes (il y en a 12 ici, plus un bonus) et les annexes.",
      S_BODY),
    P("Le plan complet est présenté à la page « Ce que contiendra le guide complet ».", S_SMALL),
], coul=INDIGO, width=FW))
story.append(PageBreak())

# ============ 3. ÉDITO
ADD(Bookmark("edito", "Avant de commencer", 0))
EXT(rule())
ADD(P("Avant de commencer", S_H2))
ADD(P(EDITO_TITRE, S_H3))
EXT([P(t, S_LEDE) for t in EDITO[:2]])
ADD(Spacer(1, 4))
gridrows = []
for t, d in EDITO_3Q:
    gridrows.append([Paragraph(f'<font color="#A85236"><b>{t}</b></font>', S_BOX), Paragraph(d, S_BODY)])
t = Table(gridrows, colWidths=[112, FW - 112])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                       ("LINEBELOW", (0, 0), (-1, -2), 0.5, BORD),
                       ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                       ("LEFTPADDING", (0, 0), (0, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]))
ADD(t)
ADD(Spacer(1, 6))
ADD(P(EDITO_FIN, S_BODY_J))
ADD(Spacer(1, 10))
EXT(rule())
ADD(P("Comment lire ce guide : trois badges de preuve", S_H3))
ADD(P(COMMENT_INTRO, S_BODY))
ADD(Spacer(1, 5))
brows = []
for key, lab, desc in BADGES:
    l, d, bg, fg = PREUVES[key]
    brows.append([badge(key, 7.4), Paragraph(desc, S_TBLC)])
for key, lab, pdesc in PICTOS:
    pass
ADD(datatable(brows, [150, FW - 150], head=False))
ADD(Spacer(1, 8))
ADD(encadre("Les quatre repères que vous retrouverez partout", [
    P("<b>QUANTITÉ</b> — ce qu'il faut prendre, exactement.", S_SMALL_N),
    P("<b>FRÉQUENCE</b> — à quel rythme le refaire (c'est souvent le plus important).", S_SMALL_N),
    P("<b>TEMPS</b> — temps de pose ou de préparation.", S_SMALL_N),
    P("<b>ATTENTION</b> — précaution ou contre-indication.", S_SMALL_N),
], coul=GOMBO, width=FW))
ADD(Spacer(1, 8))
ADD(encadre("Avertissement", [P(AVERTISSEMENT, S_SMALL_N)], coul=TERRA, bg=HexColor("#FDF6F3"), width=FW))
story.append(PageBreak())

# ============ 4. MESURES
ADD(Bookmark("mesures", "La page des mesures", 0))
EXT(rule())
ADD(P(MESURES_TITRE, S_H2))
ADD(P(MESURES_INTRO, S_LEDE))
ADD(Spacer(1, 6))
ADD(P("1 · Les quatre repères", S_H3))
rows = [[Paragraph("<b>Repère</b>", S_TBLH), Paragraph("<b>Volume</b>", S_TBLH),
         Paragraph("<b>Poids indicatif</b>", S_TBLH), Paragraph("<b>Si vous n'avez pas d'ustensile</b>", S_TBLH)]]
for a, b, c, d in MESURES_EQUIV:
    rows.append([Paragraph(f"<b>{a}</b>", S_TBLCB), Paragraph(b, S_TBLC), Paragraph(c, S_TBLC), Paragraph(d, S_TBLC)])
ADD(datatable(rows, [116, 74, 132, FW - 322]))
ADD(Spacer(1, 10))
ADD(P("2 · Combien, selon la longueur de vos cheveux", S_H3))
rows = [[Paragraph("<b>Usage</b>", S_TBLH), Paragraph("<b>Cheveux courts<br/>(&lt; 10 cm)</b>", S_TBLH),
         Paragraph("<b>Mi-longs<br/>(10 à 25 cm)</b>", S_TBLH), Paragraph("<b>Longs<br/>(&gt; 25 cm)</b>", S_TBLH)]]
for a, b, c, d in MESURES_QTE:
    rows.append([Paragraph(f"<b>{a}</b>", S_TBLCB), Paragraph(b, S_TBLC), Paragraph(c, S_TBLC), Paragraph(d, S_TBLC)])
ADD(datatable(rows, [152, 117, 117, FW - 386]))
ADD(Spacer(1, 4))
ADD(P("Ce tableau est la colonne vertébrale du guide : chaque fiche ingrédient le reprend, ingrédient par ingrédient.", S_SMALL))
ADD(Spacer(1, 10))
left = [encadre("3 · Les 4 règles d'or du mélange", bullets(MESURES_REGLES, S_BULLS), coul=INDIGO, width=246)]
right = [encadre("Et si je n'ai rien mesuré ?", [
    P("Une cuillère de table ordinaire, bien rase, vaut à peu près une cuillère à soupe. "
      "Un bouchon de bouteille d'huile, rempli à ras bord, vaut une cuillère à café et demie. "
      "Une noix de beurre, c'est ce que vous ramassez avec deux doigts qui effleurent le pot.",
      S_BULLS),
    Spacer(1, 4),
    P("<b>La règle qui compte</b> : mieux vaut une dose légère, appliquée régulièrement, qu'une dose forte "
      "appliquée une fois. Le cheveu ne se gave pas : il s'habitue, ou il sature.", S_BULLS),
    Spacer(1, 4),
    P("<b>Note de l'autrice</b> — (encadré « je », à écrire par vous : votre expérience personnelle sur le "
      "dosage, en deux ou trois phrases.)", S_SMALL),
], coul=GOMBO, width=246)]
t = Table([[left, right]], colWidths=[250, 253])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (0, 0), 0),
                       ("RIGHTPADDING", (0, 0), (0, 0), 7), ("LEFTPADDING", (1, 0), (1, 0), 0),
                       ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
ADD(t)
story.append(PageBreak())

# ============ 5. TABLEAU MAÎTRE
ADD(Bookmark("maitre", "Le tableau maître", 0))
EXT(rule())
ADD(P(MASTER_TITRE, S_H2))
ADD(P(MASTER_INTRO, S_LEDE))
ADD(Spacer(1, 6))
rows = [[Paragraph(f"<b>{h}</b>", S_TBLH) for h in MASTER_HEAD]]
for r in MASTER_ROWS:
    rows.append([Paragraph(f"<b>{r[0]}</b>", S_TBLCB)] + [Paragraph(c, S_TBLC) for c in r[1:]])
W = [72, 130, 92, 74, 66, FW - 434]
ADD(datatable(rows, W, head=True, fs=6.8))
ADD(Spacer(1, 6))
ADD(P("Légende des badges : <b>● ÉTAYÉ</b> (études humaines)  ·  <b>◐ PROMETTEUR</b> (quelques études, à confirmer)  ·  "
      "<b>○ TRADITION</b> (usage ancien et répandu, non étudié). Les prix sont des estimations par application, à revérifier "
      "au marché.", S_SMALL))
ADD(Spacer(1, 10))
ADD(encadre("Comment utiliser cette page", [
    P("<b>1.</b> Choisissez trois ingrédients, pas plus, pour commencer : un nettoyant, un hydratant, un scellant.", S_BULLS),
    P("<b>2.</b> Cherchez votre ingrédient dans la colonne « Quantité » et respectez la dose écrite pour la longueur de vos cheveux.", S_BULLS),
    P("<b>3.</b> Notez la colonne « Fréquence » quelque part : c'est elle qui fait la différence entre un cheveu qui change et un cheveu qui stagne.", S_BULLS),
    P("<b>4.</b> Lisez toujours la dernière colonne avant la première utilisation.", S_BULLS),
], coul=OR, width=FW))
story.append(PageBreak())

# ============ 6. LES 12 FICHES
def fiche_page(f, col_w=246):
    """construit la liste de flowables d'une fiche (tableau 2 colonnes, sécable)"""
    head = []
    left = []
    right = []
    preuve = f["preuve"]
    lab, desc, pbg, pfg = PREUVES[preuve]
    head.append(Paragraph(f'<font color="#B8862B" size=6.6><b>FICHE {f["num"]}/12  ·  {f["famille"].upper()}</b></font>', S_LAB))
    head.append(Paragraph(f['<font color="#B8862B">TEXTE</font>'] if False else f'{f["nom"]}', S_H2))
    head.append(Paragraph(f'{f["sci"]}', S_SUB))
    head.append(Spacer(1, 5))
    infos = [("PREUVE", f'{lab} <font size=6.2 color="#6E6A62">— {desc}</font>'),
             ("COÛT PAR APPLICATION", f["cout"]), ("TEMPS", f["pose"]), ("FAMILLE", f["famille"])]
    head.append(grid_boxes(infos, ncols=2, width=503))
    head.append(Spacer(1, 7))

    left.append(encadre("Ce qu'il fait — et pourquoi", [P(f["pourquoi"], S_BODY)], coul=GOMBO, width=col_w))
    left.append(Spacer(1, 6))
    ltab = [[Paragraph("<b>Vos cheveux</b>", S_TBLH), Paragraph("<b>Quantité</b>", S_TBLH),
             Paragraph("<b>Repère</b>", S_TBLH)]]
    for a, b, c in f["qte"]:
        ltab.append([Paragraph(a, S_TBLC), Paragraph(f"<b>{b}</b>", S_TBLCB), Paragraph(c, S_TBLC)])
    left.append(encadre("Quantité exacte", [datatable(ltab, [92, 88, col_w - 92 - 88 - 14], fs=6.8),
                                            Spacer(1, 4), P(f["qte_note"], S_SMALL)], coul=OR, width=col_w))
    left.append(Spacer(1, 6))
    left.append(encadre(f["recette_titre"], numbered(f["recette"], S_NUM) + [Spacer(1, 4), P(f["recette_note"], S_SMALL)],
                        coul=INDIGO, width=col_w))
    bien, eviter, astuce = COMBINE[f["num"]]
    left.append(Spacer(1, 6))
    left.append(encadre("À combiner / à éviter", [
        P(f'<font color="{hx(GOMBO)}"><b>Bien :</b></font> {bien}', S_BULLS),
        P(f'<font color="{hx(TERRA)}"><b>À éviter :</b></font> {eviter}', S_BULLS),
    ], coul=OR, width=col_w))
    left.append(Spacer(1, 6))
    left.append(encadre("Astuce de terrain", [P(astuce, S_BULLS)], coul=GOMBO, bg=HexColor("#F6F8F0"), width=col_w))

    chips = Table([[Paragraph(f'<font color="#2B3E63">{c}</font>', S_CHIP)] for c in f["cible"]],
                  colWidths=[col_w / 2 - 3] * 2)
    ch = [[Paragraph(f'<font color="#2B3E63">{c}</font>', S_CHIP) for c in f["cible"][i:i + 2]]
          for i in range(0, len(f["cible"]), 2)]
    while len(ch[-1]) < 2:
        ch[-1].append(Paragraph(" ", S_CHIP))
    chips = Table(ch, colWidths=[col_w / 2 - 3] * 2)
    chips.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, BORD), ("INNERGRID", (0, 0), (-1, -1), 0.4, BORD),
                               ("BACKGROUND", (0, 0), (-1, -1), BLEU_F),
                               ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                               ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    right.append(encadre("Sur quels cheveux", [chips], coul=INDIGO, width=col_w))
    right.append(Spacer(1, 6))
    right.append(encadre("Comment faire, en 4 gestes", numbered(f["etapes"], S_NUM), coul=INDIGO, width=col_w))
    right.append(Spacer(1, 6))
    frows = [[Paragraph(f'<font color="#B8862B"><b>{t}</b></font>', S_TBLCB), Paragraph(s, S_TBLC)] for t, s in f["freq"]]
    right.append(encadre("Fréquence", [datatable(frows, [86, col_w - 86 - 14], head=False, fs=6.8)], coul=TERRA, width=col_w))
    right.append(Spacer(1, 6))
    right.append(encadre("Précautions", bullets(f["precautions"], S_BULLS, "▸"), coul=TERRA, width=col_w))
    right.append(Spacer(1, 6))
    right.append(encadre("Les 3 erreurs qui gâchent tout", numbered(f["erreurs"], S_NUM), coul=GOMBO, width=col_w))
    right.append(Spacer(1, 6))
    right.append(encadre("Conservation", [P(f["conservation"], S_BODY)], coul=INDIGO, width=col_w))
    right.append(Spacer(1, 6))
    right.append(retiens(f["retiens"], width=col_w))

    body = Table([[left, right]], colWidths=[col_w + 7, 503 - col_w - 7], splitInRow=1)
    body.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                              ("LEFTPADDING", (0, 0), (0, 0), 0), ("RIGHTPADDING", (0, 0), (0, 0), 7),
                              ("LEFTPADDING", (1, 0), (1, 0), 0), ("RIGHTPADDING", (1, 0), (1, 0), 0),
                              ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return head + [body, PageBreak()]

for f in FICHES:
    ADD(Bookmark(f"fiche{f['num']}", f"Fiche {f['num']} — {f['nom']}", 1))
    EXT(fiche_page(f))

# bonus
ADD(Bookmark("bonus", "Bonus — L'eau de riz fermentée", 1))
EXT(fiche_page(BONUS))

# ============ 7. FAUX AMIS
ADD(Bookmark("fauxamis", "Les 8 faux amis", 0))
EXT(rule())
ADD(P(FAUX_AMIS_TITRE, S_H2))
ADD(P(FAUX_AMIS_INTRO, S_LEDE))
ADD(Spacer(1, 8))
left_items = FAUX_AMIS[:4]
right_items = FAUX_AMIS[4:]
def faux_col(items, w):
    flows = []
    for i, (t, d) in enumerate(items):
        flows.append(encadre(f"{t}", [P(d, S_BULLS)], coul=TERRA, width=w))
        if i < len(items) - 1:
            flows.append(Spacer(1, 6))
    return flows
t = Table([[faux_col(left_items, 246), faux_col(right_items, 246)]], colWidths=[250, 253])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (0, 0), 0),
                       ("RIGHTPADDING", (0, 0), (0, 0), 7), ("LEFTPADDING", (1, 0), (1, 0), 0),
                       ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
ADD(t)
ADD(Spacer(1, 10))
ADD(encadre("Le réflexe qui remplace toutes les recettes", [
    P("Avant d'appliquer quoi que ce soit sur votre crâne, posez-vous une seule question : "
      "<b>« Est-ce que je mettrais ça sur mon visage, aux mêmes proportions ? »</b> Si la réponse est non, "
      "ne le mettez pas sur votre crâne. Le cuir chevelu est une peau, aussi fine et plus sensible que celle du visage.", S_BODY),
], coul=INDIGO, width=FW))
story.append(PageBreak())

# ============ 8. KIT ANTI-PARESSE
ADD(Bookmark("kit", "Le Kit anti-paresse", 0))
EXT(rule())
ADD(P(KIT_TITRE, S_H2))
ADD(P(KIT_INTRO, S_LEDE))
ADD(Spacer(1, 8))
ADD(P(DEFI_TITRE, S_H3))
rows = [[Paragraph("<b>Jour</b>", S_TBLH), Paragraph("<b>Votre seule action du jour</b>", S_TBLH),
         Paragraph("<b>Temps</b>", S_TBLH), Paragraph("<b>Fait</b>", S_TBLH)]]
for j, d, tm in DEFI:
    rows.append([Paragraph(f"<b>{j}</b>", S_TBLCB), Paragraph(d, S_TBLC), Paragraph(tm, S_TBLC),
                 Paragraph("☐", ParagraphStyle("cb", fontName="Body", fontSize=11, leading=12, alignment=TA_CENTER))])
ADD(datatable(rows, [42, FW - 42 - 50 - 46, 50, 46]))
ADD(Spacer(1, 5))
ADD(P(DEFI_FIN, S_BODY))
ADD(Spacer(1, 12))
ADD(P(PLAN_TITRE, S_H3))
ADD(P("Cochez chaque jour. Les lettres renvoient à la légende ci-dessous.", S_SMALL))
ADD(Spacer(1, 4))
S_CELL = ParagraphStyle("cellplan", fontName="Body", fontSize=7.6, leading=10, alignment=TA_CENTER)
S_CHK = ParagraphStyle("chk", fontName="Body", fontSize=11, leading=12, alignment=TA_CENTER, textColor=INDIGO)
NCOL = 5
plan_rows = []
for i in range(0, len(PLAN_JOURS), NCOL):
    chunk = PLAN_JOURS[i:i + NCOL]
    cells = []
    for j, c in chunk:
        col = {"L": TERRA, "H": INDIGO, "M": GOMBO, "S": OR, "●": ENCRE, "—": GRIS}.get(c, ENCRE)
        cells.append(Paragraph(f'<font size=6.6 color="#6E6A62"><b>{j}</b></font><br/>'
                               f'<font size=13 color="{hx(col)}"><b>{c}</b></font><br/>☐', S_CELL))
    plan_rows.append(cells)
t = Table(plan_rows, colWidths=[FW / NCOL] * NCOL, rowHeights=[38] * len(plan_rows))
t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, BORD),
                       ("BACKGROUND", (0, 0), (-1, -1), KARITE_L),
                       ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                       ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
ADD(t)
ADD(Spacer(1, 4))
leg = "     ".join([f"<b>{c}</b> = {d}" for c, d in PLAN_LEGENDE])
ADD(P(leg, S_SMALL))
ADD(Spacer(1, 4))
ADD(P(PLAN_NOTE, S_SMALL))
story.append(PageBreak())

# routines
ADD(Bookmark("routines", "Les trois routines express", 1))
EXT(rule())
ADD(P("Les trois routines toutes prêtes", S_H2))
ADD(P("Choisissez selon la semaine que vous vivez, pas selon votre idéal.", S_LEDE))
ADD(Spacer(1, 8))
for titre, sous, items in ROUTINES:
    ADD(encadre(f"{titre} — {sous}", numbered(items, S_NUM), coul=INDIGO, width=FW))
    ADD(Spacer(1, 7))
ADD(Spacer(1, 3))
ADD(encadre(FILET_TITRE, [P(FILET, S_BODY)], coul=OR, bg=KARITE_L, width=FW))
ADD(Spacer(1, 12))
ADD(P(REGLES_TITRE, S_H3))
rrows = []
for n, t1, t2 in REGLES:
    rrows.append([Paragraph(f'<font size=13 color="#B8862B"><b>{n}</b></font>', S_TBLC),
                  Paragraph(f"<b>{t1}</b><br/><font size=7 color='#6E6A62'>{t2}</font>", S_TBLC)])
ADD(datatable(rrows, [26, FW - 26], head=False))
story.append(PageBreak())

# signes + suivi
ADD(Bookmark("progres", "Les 9 signes et le carnet de suivi", 1))
EXT(rule())
ADD(P(SIGNES_TITRE, S_H2))
ADD(P("Un cheveu qui va mieux ne se voit pas tout de suite sur la longueur. Il se voit dans ces détails. "
      "Cochez ceux que vous remarquez : ce sont vos vrais résultats.", S_LEDE))
ADD(Spacer(1, 6))
rows = []
for i, s in enumerate(SIGNES):
    rows.append([Paragraph("☐", ParagraphStyle("c3", fontName="Body", fontSize=11, leading=13, alignment=TA_CENTER)),
                 Paragraph(s, S_TBLC)])
ADD(datatable(rows, [24, FW - 24], head=False))
ADD(Spacer(1, 12))
ADD(P(SUIVI_TITRE, S_H3))
ADD(P("Six lignes par mois, cinq minutes. C'est le seul document qui vous montrera, dans six mois, "
      "d'où vous partez.", S_SMALL))
ADD(Spacer(1, 5))
head = [Paragraph("<b>Mois / date</b>", S_TBLH)] + [Paragraph(f"<b>{c}</b>", S_TBLH) for c in SUIVI_CHAMPS]
rows = [head]
for m in ["Mois 1", "Mois 2", "Mois 3", "Mois 4", "Mois 5", "Mois 6"]:
    rows.append([Paragraph(f"<b>{m}</b>", S_TBLCB)] + [Paragraph(" ", S_TBLC) for _ in SUIVI_CHAMPS])
data = [[head] + [[Paragraph(f"<b>{m}</b>", S_TBLCB)] + [Paragraph(" ", S_TBLC) for _ in SUIVI_CHAMPS]
                  for m in ["Mois 1", "Mois 2", "Mois 3", "Mois 4", "Mois 5", "Mois 6"]]]
rows = [[Paragraph("<b>Mois / date</b>", S_TBLH)] + [Paragraph(f"<b>{c}</b>", S_TBLH) for c in SUIVI_CHAMPS]]
for m in ["Mois 1", "Mois 2", "Mois 3", "Mois 4", "Mois 5", "Mois 6"]:
    rows.append([Paragraph(f"<b>{m}</b>", S_TBLCB)] + [Paragraph("&nbsp;", S_TBLC) for _ in SUIVI_CHAMPS])
t = datatable(rows, [52] + [(FW - 52) / len(SUIVI_CHAMPS)] * len(SUIVI_CHAMPS))
t._argH[1:] = [26] * 6
ADD(t)
ADD(Spacer(1, 6))
ADD(P("Repères à photographier chaque mois : face, profil, derrière, crâne baissé. Même lumière, même endroit, "
      "cheveux propres et secs, idéalement le même jour du mois.", S_SMALL))
story.append(PageBreak())

# ============ 9. TRESSES
ADD(Bookmark("tresses", "Les tresses protectrices", 0))
EXT(rule())
ADD(P(TRESSES_TITRE, S_H2))
ADD(P(TRESSES_INTRO, S_LEDE))
ADD(Spacer(1, 8))
left = []
left.append(encadre("Les repères à ne jamais oublier", [
    datatable([[Paragraph(f"<b>{a}</b>", S_TBLCB), Paragraph(b, S_TBLC)] for a, b in TRESSES_ID],
              [110, 128], head=False, fs=6.9)], coul=TERRA, width=246))
left.append(Spacer(1, 7))
left.append(encadre("Signaux d'alarme : on retire tout de suite", bullets([
    "Douleur telle que vous ne pouvez pas lever les sourcils tranquillement.",
    "Petits boutons, croûtes ou suintements le long de la lisière dans les trois premiers jours.",
    "Une douleur qui vous empêche de dormir, ou une sensation de peau tirée en permanence.",
    "Une zone clairsemée qui apparaît entre deux retouches.",
    "Une lisière qui ne repousse pas après six mois sans tension : c'est le moment de consulter.",
], S_BULLS, "▸"), coul=TERRA, width=246))
left.append(Spacer(1, 7))
left.append(photo("photo_knotless.png", 246))
left.append(Spacer(1, 3))
left.append(P("Visuel d'intention — à remplacer par une photographie prise au Bénin.", S_SMALL))
right = []
right.append(encadre("Le protocole complet : avant, pendant, après",
                     [datatable([[Paragraph(f'<font color="#B8862B"><b>{a}</b></font><br/><font size=6.6>{b}</font>', S_TBLCB),
                                  Paragraph(c, S_TBLC)] for a, b, c in TRESSES_PROTO],
                                [62, 176], head=False, fs=6.9)], coul=INDIGO, width=246))
right.append(Spacer(1, 7))
right.append(encadre("Ce que ça coûte, ce que ça rapporte", [
    P("Comparez sur quatre mois : <b>quatre poses enchaînées</b>, déposées et reprises sans vraie pause (coût salon, "
      "tension répétée, lisière fragilisée), contre <b>deux poses tenues six semaines chacune</b>, séparées par trois "
      "semaines de repos pendant lesquelles vous prenez soin de votre lisière. Le second scénario coûte moins et "
      "protège davantage.", S_BULLS),
    Spacer(1, 3),
    P("Le calcul à faire une fois par an : coût annuel des tresses + coût des soins de réparation, contre coût "
      "annuel d'une routine simple à la maison.", S_SMALL),
], coul=GOMBO, width=246))
t = Table([[left, right]], colWidths=[250, 253])
t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (0, 0), 0),
                       ("RIGHTPADDING", (0, 0), (0, 0), 7), ("LEFTPADDING", (1, 0), (1, 0), 0),
                       ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
ADD(t)
story.append(PageBreak())

# fiche coiffeuse
ADD(Bookmark("coiffeuse", "Fiche à remettre à ma coiffeuse", 1))
EXT(rule())
ADD(P(COIFFEUSE_TITRE, S_H2))
ADD(P("Découpez cette page, remplissez la durée prévue, et remettez-la à la personne qui vous tresse. "
      "Ce n'est pas une exigence : c'est une demande polie, et elle vous protège toutes les deux.", S_LEDE))
ADD(Spacer(1, 10))
box = [Paragraph("Mes consignes pour cette pose", ParagraphStyle("t", fontName="HeadB", fontSize=13,
                                                                leading=15, textColor=INDIGO))]
box.append(Spacer(1, 6))
for c in COIFFEUSE:
    box.append(Paragraph("☐  " + c, ParagraphStyle("cl", fontName="Body", fontSize=9.2, leading=13,
                                                   leftIndent=2, textColor=ENCRE)))
box.append(Spacer(1, 10))
box.append(Paragraph("Signature / accord : ....................................................          "
                     "Date : ...... / ...... / 20......", S_SMALL))
t = Table([[box]], colWidths=[FW])
t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 1.2, INDIGO), ("BACKGROUND", (0, 0), (-1, -1), KARITE_L),
                       ("LEFTPADDING", (0, 0), (-1, -1), 14), ("RIGHTPADDING", (0, 0), (-1, -1), 14),
                       ("TOPPADDING", (0, 0), (-1, -1), 14), ("BOTTOMPADDING", (0, 0), (-1, -1), 14)]))
ADD(t)
ADD(Spacer(1, 12))
ADD(encadre("Pourquoi cette fiche est importante", [
    P("L'alopécie de traction est la forme de chute la plus <b>évitable</b> qui existe. Elle commence souvent "
      "sans douleur : une lisière qui s'éclaircit lentement, des tempes qui se dégarnissent, une nuque qui blanchit "
      "de peau. Au début, quand le follicule est encore intact, le cheveu repousse dès qu'on arrête de tirer. "
      "Tardivement, quand le follicule est cicatrisé, il ne repousse plus — aucun produit ne le réveillera.", S_BODY),
    P("C'est pour cela que la tension est le seul sujet sur lequel il ne faut jamais négocier, ni avec sa coiffeuse, "
      "ni avec soi-même, ni avec la fatigue d'une journée où « il faut que ce soit fini ».", S_BODY),
], coul=INDIGO, width=FW))
story.append(PageBreak())

# ============ 10. PAGES DE TRAVAIL
ADD(Bookmark("noms", "Vos pages de travail", 0))
EXT(rule())
ADD(P(NOMS_TITRE, S_H2))
ADD(P(NOMS_INTRO, S_LEDE))
ADD(Spacer(1, 8))
rows = [[Paragraph("<b>Ingrédient</b>", S_TBLH), Paragraph("<b>Nom en fon</b>", S_TBLH),
         Paragraph("<b>Nom en yoruba</b>", S_TBLH), Paragraph("<b>Autre langue / remarque</b>", S_TBLH)]]
for n in NOMS_ROWS:
    rows.append([Paragraph(f"<b>{n}</b>", S_TBLCB), Paragraph("&nbsp;", S_TBLC),
                 Paragraph("&nbsp;", S_TBLC), Paragraph("&nbsp;", S_TBLC)])
t = datatable(rows, [130, 110, 110, FW - 350])
t._argH[1:] = [22] * len(NOMS_ROWS)
ADD(t)
ADD(Spacer(1, 12))
ADD(P(CORRECTIONS_TITRE, S_H2))
ADD(P(CORRECTIONS_INTRO, S_LEDE))
ADD(Spacer(1, 6))
ADD(encadre("Les 8 points sur lesquels j'attends votre avis en priorité", [
    Paragraph(f"<b>{a}</b> — {b}", S_BULLS, bulletText="▸") for a, b in CORRECTIONS_A_VERIFIER
], coul=TERRA, width=FW))
ADD(Spacer(1, 8))
ADD(P("Mes remarques (citez la page et le numéro de fiche)", S_H3))
ADD(Spacer(1, 4))
rows = [[Paragraph("<b>Page / fiche</b>", S_TBLH), Paragraph("<b>Ma remarque (garder · corriger · ajouter · supprimer)</b>", S_TBLH)]]
for _ in range(12):
    rows.append([Paragraph("&nbsp;", S_TBLC), Paragraph("&nbsp;", S_TBLC)])
t = datatable(rows, [90, FW - 90])
t._argH[1:] = [26] * 12
ADD(t)
story.append(PageBreak())

# derniere page
ADD(Bookmark("avenir", "Ce que contiendra le guide complet", 1))
EXT(rule())
ADD(P(A_VENIR_TITRE, S_H2))
ADD(P("Le guide complet fera environ 148 pages très illustrées, en quatre parties et une boîte à outils. "
      "Les rubriques marquées « dans cet extrait » sont déjà écrites et vous les avez sous les yeux.", S_LEDE))
ADD(Spacer(1, 8))
for a, b in A_VENIR:
    ADD(encadre(a, [P(b, S_BODY)], coul=INDIGO, width=FW))
    ADD(Spacer(1, 6))
ADD(Spacer(1, 6))
ADD(encadre("Merci", [
    P("Merci d'avoir lu jusqu'ici. Ce document n'attend que vos corrections pour devenir le guide que vos lectrices "
      "garderont dans leur cuisine. Tout ce qui ne vous ressemble pas doit partir ; tout ce que vous savez et que "
      "je ne sais pas doit entrer.", S_BODY),
    P("Les trois prochaines étapes : <b>vos corrections</b> → <b>vos photos et vos noms locaux</b> → "
      "<b>la rédaction des parties 1 et 2 restantes</b>.", S_BODY),
], coul=OR, bg=KARITE_L, width=FW))

# ------------------------------------------------------------------ build
doc = Doc(OUT)
doc.build(story)
print("OK ->", OUT)
print("pages :", doc.page)
