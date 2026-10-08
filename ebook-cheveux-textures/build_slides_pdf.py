# -*- coding: utf-8 -*-
"""
Générateur de PDF au format Slides Paysage (16:9 widescreen)
Correspondant exactement aux 75 slides de la version PowerPoint.
Sortie : MA-COURONNE-MES-REGLES-Complet-Slides.pdf
"""

import os
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pypdfium2 as pdfium

from slides_data_intro import SLIDES_INTRO
from slides_data_diag_ingr import SLIDES_DIAG_INGR
from slides_data_routines import SLIDES_ROUTINES
from slides_data_tresses_outils import SLIDES_TRESSES_OUTILS

HERE = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(HERE, "extrait", "images")
OUT_PDF = os.path.join(HERE, "MA-COURONNE-MES-REGLES-Complet-Slides.pdf")

# Dimensions 16:9 en points (960 x 540 pt)
W, H = 960, 540

DEJA = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DejaVu", f"{DEJA}/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuB", f"{DEJA}/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerifB", f"{DEJA}/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSerif", f"{DEJA}/DejaVuSerif.ttf"))

# Couleurs
C_DARK_BG   = HexColor("#1B2740")
C_LIGHT_BG  = HexColor("#FBF9F5")
C_CARD_BG   = HexColor("#FFFFFF")
C_BORDER    = HexColor("#E2D7C4")
C_TEXT_DARK = HexColor("#1C1B19")
C_TEXT_MUTED= HexColor("#6E6A62")
C_TEXT_LIGHT= HexColor("#FAF6F0")

C_GOLD      = HexColor("#B8862B")
C_GOLD_L    = HexColor("#D9A13B")
C_TERRA     = HexColor("#A85236")
C_GREEN     = HexColor("#55663A")
C_INDIGO    = HexColor("#2B3E63")

ACCENTS = {
    "indigo": C_INDIGO,
    "gold": C_GOLD,
    "terra": C_TERRA,
    "green": C_GREEN
}

def draw_header(c, tracker, title, subtitle=None):
    # Tracker
    c.setFont("DejaVuB", 9)
    c.setFillColor(C_TERRA)
    c.drawString(55, H - 38, tracker.upper())

    # Titre
    c.setFont("DejaVuSerifB", 18)
    c.setFillColor(C_INDIGO)
    c.drawString(55, H - 62, title)

    # Sous-titre
    if subtitle:
        c.setFont("DejaVu", 10.5)
        c.setFillColor(C_TEXT_MUTED)
        c.drawString(55, H - 80, subtitle)

def draw_footer(c, slide_num, total_slides):
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.8)
    c.line(55, 30, W - 55, 30)

    c.setFont("DejaVu", 8)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(55, 18, "Ma couronne, mes règles — Le guide complet des cheveux texturés en Afrique  ·  Édition Bénin 2026")

    c.setFont("DejaVuB", 8)
    c.setFillColor(C_GOLD)
    c.drawRightString(W - 55, 18, f"{slide_num} / {total_slides}")

def draw_callout(c, text, label="À RETENIR"):
    clean_text = text.strip()
    for prefix in ["À RETENIR —", "À RETENIR :", "À RETENIR", "A RETENIR —", "A RETENIR :"]:
        if clean_text.startswith(prefix):
            clean_text = clean_text[len(prefix):].strip()
            if clean_text.startswith("—") or clean_text.startswith(":"):
                clean_text = clean_text[1:].strip()

    bx, by, bw, bh = 55, 42, W - 110, 52
    c.setFillColor(C_DARK_BG)
    c.roundRect(bx, by, bw, bh, 6, stroke=0, fill=1)

    c.setFont("DejaVuB", 9.5)
    c.setFillColor(C_GOLD_L)
    lbl = f"{label} — "
    c.drawString(bx + 18, by + bh - 22, lbl)
    lw = c.stringWidth(lbl, "DejaVuB", 9.5)

    c.setFont("DejaVu", 9.5)
    c.setFillColor(C_TEXT_LIGHT)
    words = clean_text.split()
    line = ""
    y = by + bh - 22
    first = True
    for w in words:
        test = (line + " " + w).strip()
        max_w = bw - 36 - (lw if first else 0)
        if c.stringWidth(test, "DejaVu", 9.5) > max_w:
            x = bx + 18 + (lw if first else 0)
            c.drawString(x, y, line)
            line = w
            y -= 14
            first = False
        else:
            line = test
    if line:
        x = bx + 18 + (lw if first else 0)
        c.drawString(x, y, line)

def draw_card(c, x, y, w, h, card_data, accent):
    c.setFillColor(C_CARD_BG)
    c.setStrokeColor(C_BORDER)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 6, stroke=1, fill=1)

    # Accent bar
    c.setFillColor(accent)
    c.rect(x + 10, y + h - 5, w - 20, 4, stroke=0, fill=1)

    # Card title
    c.setFont("DejaVuSerifB", 13)
    c.setFillColor(accent)
    c.drawString(x + 16, y + h - 25, card_data["title"])

    # Items
    cur_y = y + h - 45
    if "paragraphs" in card_data:
        for item in card_data["paragraphs"]:
            if cur_y < y + 15:
                break
            if isinstance(item, tuple) and len(item) == 2:
                p_tit, p_body = item
                c.setFont("DejaVuB", 9)
                c.setFillColor(accent)
                c.drawString(x + 16, cur_y, p_tit)
                cur_y -= 12

                c.setFont("DejaVu", 8.8)
                c.setFillColor(C_TEXT_DARK)
                words = p_body.split()
                line = ""
                for w_word in words:
                    test = (line + " " + w_word).strip()
                    if c.stringWidth(test, "DejaVu", 8.8) > w - 32:
                        c.drawString(x + 16, cur_y, line)
                        line = w_word
                        cur_y -= 11.5
                        if cur_y < y + 15:
                            break
                    else:
                        line = test
                if line and cur_y >= y + 15:
                    c.drawString(x + 16, cur_y, line)
                    cur_y -= 14
            else:
                c.setFont("DejaVu", 8.8)
                c.setFillColor(C_TEXT_DARK)
                c.drawString(x + 16, cur_y, f"• {item}")
                cur_y -= 14
    elif "body" in card_data:
        for it in card_data["body"]:
            if cur_y < y + 15:
                break
            c.setFont("DejaVu", 8.8)
            c.setFillColor(C_TEXT_DARK)
            words = it.split()
            line = "• "
            for w_word in words:
                test = (line + " " + w_word).strip()
                if c.stringWidth(test, "DejaVu", 8.8) > w - 32:
                    c.drawString(x + 16, cur_y, line)
                    line = "  " + w_word
                    cur_y -= 11.5
                    if cur_y < y + 15:
                        break
                else:
                    line = test
            if line and cur_y >= y + 15:
                c.drawString(x + 16, cur_y, line)
                cur_y -= 13

def render_slides_pdf():
    all_slides = []
    all_slides.extend(SLIDES_INTRO)
    all_slides.extend(SLIDES_DIAG_INGR)
    all_slides.extend(SLIDES_ROUTINES)
    all_slides.extend(SLIDES_TRESSES_OUTILS)

    total_slides = len(all_slides)
    canv = canvas.Canvas(OUT_PDF, pagesize=(W, H))

    for idx, s in enumerate(all_slides):
        slide_num = idx + 1
        stype = s.get("type", "two_card")

        if stype == "cover":
            # Fond sombre
            canv.setFillColor(C_DARK_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)

            # Cadre doré
            canv.setStrokeColor(C_GOLD)
            canv.setLineWidth(1.2)
            canv.rect(25, 25, W - 50, H - 50, stroke=1, fill=0)

            # Header
            canv.setFont("DejaVuB", 9)
            canv.setFillColor(C_GOLD_L)
            canv.drawString(55, H - 65, "GUIDE PRATIQUE COMPLET  ·  CHEVEUX TEXTURÉS  ·  BÉNIN & AFRIQUE")

            # Titre
            canv.setFont("DejaVuSerifB", 34)
            canv.setFillColor(C_TEXT_LIGHT)
            canv.drawString(55, H - 105, "Ma couronne,")
            canv.drawString(55, H - 145, "mes règles")

            # Sous-titre
            canv.setFont("DejaVu", 11)
            canv.setFillColor(HexColor("#D2C8B8"))
            words = s["tagline"].split()
            line = ""; yy = H - 180
            for w_w in words:
                test = (line + " " + w_w).strip()
                if canv.stringWidth(test, "DejaVu", 11) > 480:
                    canv.drawString(55, yy, line); yy -= 16; line = w_w
                else:
                    line = test
            if line:
                canv.drawString(55, yy, line)

            # 4 Promesses en cartouches
            prom = [
                ("POURQUOI ÇA MARCHE ?", "Ce que chaque ingrédient fait à la fibre, expliqué simplement."),
                ("COMBIEN EXACTEMENT ?", "Cuillères, verres, noix : des quantités précises selon la longueur."),
                ("À QUELLE FRÉQUENCE ?", "Chaque geste a son rythme : semaine, mois ou saison."),
                ("LE KIT ANTI-PARESSE", "Le minimum vital qui marche quand vous n'avez ni le temps ni l'envie.")
            ]
            for p_i, (pt, pd) in enumerate(prom):
                pr = p_i // 2; pc = p_i % 2
                px = 55 + pc * 260
                py = H - 310 - pr * 90
                canv.setFillColor(HexColor("#243352"))
                canv.setStrokeColor(C_GOLD)
                canv.setLineWidth(0.6)
                canv.roundRect(px, py, 250, 78, 4, stroke=1, fill=1)

                canv.setFont("DejaVuB", 9)
                canv.setFillColor(C_GOLD_L)
                canv.drawString(px + 12, py + 56, pt)

                canv.setFont("DejaVu", 8)
                canv.setFillColor(C_TEXT_LIGHT)
                words = pd.split()
                line = ""; yy = py + 40
                for w_w in words:
                    test = (line + " " + w_w).strip()
                    if canv.stringWidth(test, "DejaVu", 8) > 226:
                        canv.drawString(px + 12, yy, line); yy -= 11; line = w_w
                    else:
                        line = test
                if line:
                    canv.drawString(px + 12, yy, line)

            # Image de droite
            img_p = os.path.join(IMG_DIR, s.get("image", "cover_crop.png"))
            if os.path.exists(img_p):
                canv.drawImage(img_p, W - 365, 85, width=310, height=390)
                canv.setStrokeColor(C_GOLD); canv.setLineWidth(1.2)
                canv.rect(W - 365, 85, 310, 390, stroke=1, fill=0)

            # Bas
            canv.setFont("DejaVu", 9)
            canv.setFillColor(C_GOLD)
            canv.drawString(55, 45, f"{s['author']}  ·  {s['date']}  ·  Document de travail complet")

        elif stype == "divider":
            canv.setFillColor(C_DARK_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)

            canv.setStrokeColor(C_GOLD)
            canv.setLineWidth(1.2)
            canv.rect(40, 40, W - 80, H - 80, stroke=1, fill=0)

            canv.setFont("DejaVuB", 11)
            canv.setFillColor(C_GOLD_L)
            canv.drawString(80, H - 110, s["part_num"].upper())

            canv.setFont("DejaVuSerifB", 30)
            canv.setFillColor(C_TEXT_LIGHT)
            canv.drawString(80, H - 160, s["title"])

            canv.setStrokeColor(C_GOLD_L)
            canv.setLineWidth(1.5)
            canv.line(80, H - 180, 320, H - 180)

            canv.setFont("DejaVuSerif", 15)
            canv.setFillColor(C_GOLD_L)
            words = s["quote"].split()
            line = ""; yy = H - 225
            for w_w in words:
                test = (line + " " + w_w).strip()
                if canv.stringWidth(test, "DejaVuSerif", 15) > W - 180:
                    canv.drawString(80, yy, line); yy -= 22; line = w_w
                else:
                    line = test
            if line:
                canv.drawString(80, yy, line)

            canv.setFont("DejaVu", 11)
            canv.setFillColor(HexColor("#D2C8B8"))
            canv.drawString(80, H - 350, s["subtitle"])

        elif stype == "two_card":
            canv.setFillColor(C_LIGHT_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)
            draw_header(canv, s["tracker"], s["title"], s.get("subtitle"))

            card_h = 310 if "callout" in s else 380
            c1 = s["card1"]; acc1 = ACCENTS.get(c1.get("accent", "indigo"), C_INDIGO)
            draw_card(canv, 55, H - 95 - card_h, 415, card_h, c1, acc1)

            c2 = s["card2"]; acc2 = ACCENTS.get(c2.get("accent", "terra"), C_TERRA)
            draw_card(canv, 490, H - 95 - card_h, 415, card_h, c2, acc2)

            if "callout" in s:
                draw_callout(canv, s["callout"])

            draw_footer(canv, slide_num, total_slides)

        elif stype == "three_card":
            canv.setFillColor(C_LIGHT_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)
            draw_header(canv, s["tracker"], s["title"], s.get("subtitle"))

            card_h = 310 if "callout" in s else 380
            cw = 270; gap = 20
            cols = [s["col1"], s["col2"], s["col3"]]
            for c_i, col_d in enumerate(cols):
                cx = 55 + c_i * (cw + gap)
                acc = ACCENTS.get(col_d.get("accent", "indigo"), C_INDIGO)
                draw_card(canv, cx, H - 95 - card_h, cw, card_h, col_d, acc)

            if "callout" in s:
                draw_callout(canv, s["callout"])

            draw_footer(canv, slide_num, total_slides)

        elif stype == "four_boxes":
            canv.setFillColor(C_LIGHT_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)
            draw_header(canv, s["tracker"], s["title"], s.get("subtitle"))

            boxes = [s["box1"], s["box2"], s["box3"], s["box4"]]
            bw = 415; bh = 180
            coords = [(55, H - 285), (490, H - 285), (55, 45), (490, 45)]
            b_colors = [C_TERRA, C_INDIGO, C_GREEN, C_GOLD]

            for b_i, (bt, bs, bx_txt) in enumerate(boxes):
                bx, by = coords[b_i]
                col = b_colors[b_i % 4]

                canv.setFillColor(C_CARD_BG)
                canv.setStrokeColor(C_BORDER)
                canv.setLineWidth(0.8)
                canv.roundRect(bx, by, bw, bh, 6, stroke=1, fill=1)

                canv.setFillColor(col)
                canv.rect(bx + 10, by + bh - 5, bw - 20, 3, stroke=0, fill=1)

                canv.setFont("DejaVuSerifB", 12)
                canv.setFillColor(col)
                canv.drawString(bx + 14, by + bh - 24, bt)

                canv.setFont("DejaVuB", 8)
                canv.setFillColor(C_TEXT_MUTED)
                canv.drawString(bx + 14, by + bh - 38, bs.upper())

                canv.setFont("DejaVu", 8.5)
                canv.setFillColor(C_TEXT_DARK)
                words = bx_txt.split()
                line = ""; yy = by + bh - 54
                for w_w in words:
                    test = (line + " " + w_w).strip()
                    if canv.stringWidth(test, "DejaVu", 8.5) > bw - 28:
                        canv.drawString(bx + 14, yy, line); yy -= 11.5; line = w_w
                        if yy < by + 10: break
                    else:
                        line = test
                if line and yy >= by + 10:
                    canv.drawString(bx + 14, yy, line)

            draw_footer(canv, slide_num, total_slides)

        elif stype == "table":
            canv.setFillColor(C_LIGHT_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)
            draw_header(canv, s["tracker"], s["title"], s.get("subtitle"))

            headers = s["headers"]
            rows = s["rows"]
            tx, ty = 55, H - 100
            tw = W - 110
            n_cols = len(headers)
            col_w = tw / float(n_cols)
            row_h = 24 if len(rows) > 7 else 32

            # Header
            canv.setFillColor(C_DARK_BG)
            canv.roundRect(tx, ty - row_h, tw, row_h, 4, stroke=0, fill=1)
            canv.setFont("DejaVuB", 8.8)
            canv.setFillColor(C_GOLD_L)
            for ch_i, h_t in enumerate(headers):
                canv.drawString(tx + ch_i * col_w + 8, ty - row_h + 8, h_t)

            cur_ty = ty - row_h
            for r_i, r_data in enumerate(rows):
                cur_ty -= row_h
                canv.setFillColor(C_CARD_BG if r_i % 2 == 0 else HexColor("#F5EEE0"))
                canv.rect(tx, cur_ty, tw, row_h, stroke=0, fill=1)
                canv.setStrokeColor(C_BORDER); canv.setLineWidth(0.4)
                canv.line(tx, cur_ty, tx + tw, cur_ty)

                for c_idx, val in enumerate(r_data):
                    if c_idx == 0:
                        canv.setFont("DejaVuB", 8.5)
                        canv.setFillColor(C_INDIGO)
                    else:
                        canv.setFont("DejaVu", 8.2)
                        canv.setFillColor(C_TEXT_DARK)
                    val_str = str(val)[:45]
                    canv.drawString(tx + c_idx * col_w + 8, cur_ty + 7, val_str)

            if "callout" in s:
                draw_callout(canv, s["callout"])

            draw_footer(canv, slide_num, total_slides)

        elif stype == "image_card":
            canv.setFillColor(C_LIGHT_BG)
            canv.rect(0, 0, W, H, stroke=0, fill=1)
            draw_header(canv, s["tracker"], s["title"], s.get("subtitle"))

            img_p = os.path.join(IMG_DIR, s.get("image", "photo_mesures.png"))
            card_h = 310 if "callout" in s else 380
            if os.path.exists(img_p):
                canv.drawImage(img_p, 55, H - 95 - card_h, width=320, height=card_h)
                canv.setStrokeColor(C_BORDER); canv.setLineWidth(1)
                canv.rect(55, H - 95 - card_h, 320, card_h, stroke=1, fill=0)

            c_d = s["card"]
            acc = ACCENTS.get(c_d.get("accent", "gold"), C_GOLD)
            draw_card(canv, 395, H - 95 - card_h, 510, card_h, c_d, acc)

            if "callout" in s:
                draw_callout(canv, s["callout"])

            draw_footer(canv, slide_num, total_slides)

        canv.showPage()

    canv.save()
    print(f"PDF généré avec succès : {OUT_PDF} ({total_slides} pages)")

if __name__ == "__main__":
    render_slides_pdf()
