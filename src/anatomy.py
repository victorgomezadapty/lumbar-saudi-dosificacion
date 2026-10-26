"""Original schematic anatomy drawings (inline SVG) for the site. Illustrative, not to scale."""
import math

# Muscle colours (categorical, distinct on the dark surface); bones stay neutral.
MUSCLE = {"multifidus": "#34b78a", "erector": "#e3a23b", "psoas": "#8fb3ff", "transversus": "#e88aa6"}
# Pictogram-only regions, coloured apart from the spine figure so each colour keeps one meaning.
RECTUS, LATERAL = "#f0a6c0", "#c3a3ff"
BONE_FILL, BONE_LINE, DISC = "#26332d", "#a7b5ad", "#7fdcb4"


def _rot(x, y, cx, cy, deg):
    a = math.radians(deg)
    dx, dy = x - cx, y - cy
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def _poly(points):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)


def _smooth(pts, move=True):
    """Catmull-Rom spline through pts as cubic Bezier segments; starts with M unless move=False."""
    out = [f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"] if move else []
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        out.append(f"C {c1[0]:.1f} {c1[1]:.1f}, {c2[0]:.1f} {c2[1]:.1f}, {p2[0]:.1f} {p2[1]:.1f}")
    return " ".join(out)


def spine(t):
    """Lateral view of the lumbar spine (anterior to the right) with four muscle groups.

    t: dict with an_* keys (title, caption, item names and descriptions) for one language.
    """
    levels = [(238, 76, -7), (250, 131, -3), (256, 186, 0), (252, 241, 4), (240, 296, 10)]
    bodies, discs, posts, labels = [], [], [], []
    for i, (x, y, tilt) in enumerate(levels):
        corners = [_rot(px, py, x, y, tilt) for px, py in [(x - 37, y - 20), (x + 37, y - 20), (x + 37, y + 20), (x - 37, y + 20)]]
        bodies.append(f'<polygon points="{_poly(corners)}"/>')
        labels.append(f'<text x="{x:.0f}" y="{y + 5:.0f}">L{i + 1}</text>')
        # Posterior elements: pedicle and an obliquely downward spinous process.
        proc = [_rot(px, py, x, y, tilt) for px, py in [(x - 37, y - 9), (x - 70, y - 11), (x - 104, y + 6), (x - 100, y + 20), (x - 70, y + 10), (x - 37, y + 9)]]
        posts.append(f'<polygon points="{_poly(proc)}"/>')
        if i < len(levels) - 1:
            nx, ny, nt = levels[i + 1]
            mx, my, mt = (x + nx) / 2, (y + ny) / 2, (tilt + nt) / 2
            disc = [_rot(px, py, mx, my, mt) for px, py in [(mx - 33, my - 5), (mx + 33, my - 5), (mx + 33, my + 5), (mx - 33, my + 5)]]
            discs.append(f'<polygon points="{_poly(disc)}"/>')
    # L5/S1 disc and sacrum.
    discs.append(f'<polygon points="{_poly([(206, 318), (272, 326), (270, 336), (204, 328)])}"/>')
    sacrum = _poly([(200, 334), (276, 343), (262, 384), (236, 426), (214, 428), (196, 392)])
    tips = [_rot(x - 102, y + 13, x, y, tilt) for x, y, tilt in levels]      # spinous process tips
    laminae = [_rot(x - 44, y, x, y, tilt) for x, y, tilt in levels]         # base of the posterior arch

    def band(inner, outer):
        """Closed smooth band between two point lists running top to bottom."""
        back = list(reversed(outer))
        return f'<path d="{_smooth(inner)} L {back[0][0]:.1f} {back[0][1]:.1f} {_smooth(back, move=False)} Z"/>'

    # Multifidus: deep mass filling the gutter between the arches and the spinous processes, down to the sacrum.
    mf_in = [(laminae[0][0], laminae[0][1] - 26)] + laminae + [(200, 350), (210, 410)]
    mf_out = [(tips[0][0] + 6, tips[0][1] - 30)] + [(tx + 4, ty) for tx, ty in tips] + [(164, 350), (196, 418)]
    fibres = "".join(f'<path class="fib" d="M{a[0]:.0f} {a[1] - 14:.0f} L {b[0] + 6:.0f} {b[1] + 10:.0f}"/>' for a, b in zip(laminae, tips))
    multifidus = band(mf_in, mf_out) + fibres
    # Erector spinae: longer, more superficial band posterior to the spinous processes.
    er_in = [(tips[0][0] - 2, 36)] + [(tx - 4, ty) for tx, ty in tips] + [(158, 352), (194, 426)]
    er_out = [(tips[0][0] - 38, 36)] + [(tx - 40, ty) for tx, ty in tips] + [(122, 352), (172, 434)]
    erector = band(er_in, er_out)
    # Psoas major: anterior to the vertebral bodies, running down and forward towards the hip.
    ps_in = [(x + 20, y - 18) for x, y, _ in levels[:1]] + [(x + 20, y) for x, y, _ in levels] + [(306, 380), (330, 436)]
    ps_out = [(x + 40, y - 18) for x, y, _ in levels[:1]] + [(x + 42 + 7 * i, y) for i, (x, y, _) in enumerate(levels)] + [(344, 376), (362, 430)]
    psoas = band(ps_in, ps_out)
    transversus = '<path d="M392 120 C 420 190, 424 290, 398 380 L 384 376 C 406 292, 404 194, 378 126 Z"/>'

    def group(key, shapes):
        return f'<g class="an-m" data-k="{key}" style="--c:{MUSCLE[key]}">{shapes}</g>'

    svg = (
        '<svg class="an-svg" viewBox="40 20 400 420" role="img" aria-labelledby="an-title">'
        f'<title id="an-title">{t["an_title"]}</title>'
        # faint body outline: back on the left, abdomen on the right
        '<path class="an-skin" d="M78 26 C 60 140, 64 260, 112 360 C 140 420, 170 436, 200 440 M436 70 C 452 170, 450 300, 420 400"/>'
        + group("erector", erector)
        + group("multifidus", multifidus)
        + group("psoas", psoas)
        + f'<g class="an-b" data-k="bones">{"".join(bodies)}{"".join(posts)}<polygon points="{sacrum}"/></g>'
        + f'<g class="an-d" data-k="discs">{"".join(discs)}</g>'
        + group("transversus", transversus)
        + f'<g class="an-l" aria-hidden="true">{"".join(labels)}<text x="232" y="392">S</text></g>'
        + '</svg>'
    )

    items = [("bones", BONE_LINE, "an_bones"), ("discs", DISC, "an_discs"), ("multifidus", MUSCLE["multifidus"], "an_mf"),
             ("erector", MUSCLE["erector"], "an_es"), ("psoas", MUSCLE["psoas"], "an_ps"), ("transversus", MUSCLE["transversus"], "an_ta")]
    legend = "".join(
        f'<button type="button" class="an-chip" data-k="{k}" aria-pressed="false" style="--c:{c}"><i></i>{t[key + "_n"]}</button>'
        for k, c, key in items)
    notes = "".join(f'<p class="an-note" data-k="{k}" hidden><b>{t[key + "_n"]}.</b> {t[key + "_d"]}</p>' for k, _, key in items)
    return (
        '<div class="anat card reveal">'
        f'<div><span class="tag">{t["an_tag"]}</span><h3 style="margin-top:12px">{t["an_h"]}</h3><p class="muted">{t["an_lead"]}</p>'
        f'<div class="an-legend" role="group" aria-label="{t["an_h"]}">{legend}</div>'
        f'<div class="an-detail" aria-live="polite"><p class="an-note" data-k="" >{t["an_hint"]}</p>{notes}</div>'
        f'<p class="small soft">{t["an_cap"]}</p></div>'
        f'<figure class="an-fig">{svg}</figure>'
        '</div>'
    )


def _figure(body, highlight, color, title):
    return (f'<figure class="pic"><svg viewBox="16 36 220 84" role="img" aria-label="{title}">'
            '<line class="pic-floor" x1="10" y1="112" x2="230" y2="112"/>'
            f'<g class="pic-body">{body}</g><g class="pic-hi" style="--c:{color}">{highlight}</g></svg>'
            f'<figcaption><b>{title}</b></figcaption></figure>')


def big3(t):
    """Stick-figure pictograms of McGill's curl-up, side bridge and bird dog with the main target region."""
    curl = _figure(
        '<circle cx="44" cy="84" r="11"/><path d="M54 90 L120 104"/><path d="M120 104 L162 72 L196 108"/>'
        '<path d="M120 104 L190 108"/><path d="M62 94 L92 108"/>',
        '<path d="M66 94 L112 103"/>', RECTUS, t["b3_curl"])
    side = _figure(
        '<circle cx="40" cy="58" r="11"/><path d="M50 66 L206 104"/><path d="M58 70 L58 106 L80 106"/>',
        '<path d="M96 77 L150 90"/>', LATERAL, t["b3_side"])
    bird = _figure(
        '<circle cx="190" cy="52" r="11"/><path d="M176 62 L104 66"/><path d="M168 64 L168 108"/>'
        '<path d="M104 66 L104 108 L80 108"/><path d="M176 60 L224 46"/><path d="M104 66 L40 58"/>',
        '<path d="M112 64 L164 62"/>', MUSCLE["erector"], t["b3_bird"])
    return f'<div class="big3">{curl}{side}{bird}</div><p class="small soft">{t["b3_note"]}</p>'


def bodymap():
    """Posterior body map for the plan (Spanish only): the three modules' regions."""
    col = {"lumbar": MUSCLE["multifidus"], "isquios": MUSCLE["erector"], "aquiles": MUSCLE["psoas"]}
    leg = "M84 316 L126 322 L123 420 Q121 446 117 474 L113 500 Q111 510 99 510 L93 510 Q88 474 90 444 L86 420 Z"
    leg_r = "M176 316 L134 322 L137 420 Q139 446 143 474 L147 500 Q149 510 161 510 L167 510 Q172 474 170 444 L174 420 Z"
    body = (
        '<circle cx="130" cy="40" r="25"/><rect x="118" y="62" width="24" height="26" rx="6"/>'
        '<path d="M70 98 Q130 84 190 98 L200 170 Q186 232 178 262 L82 262 Q74 232 60 170 Z"/>'
        '<path d="M80 258 L180 258 Q194 300 176 320 L132 326 L128 326 L84 320 Q66 300 80 258 Z"/>'
        '<path d="M70 100 Q46 112 44 170 L38 262 Q36 278 46 280 Q56 278 55 262 L62 176 Z"/>'
        '<path d="M190 100 Q214 112 216 170 L222 262 Q224 278 214 280 Q204 278 205 262 L198 176 Z"/>'
        f'<path d="{leg}"/><path d="{leg_r}"/>'
    )
    hi = (
        f'<g style="--c:{col["lumbar"]}"><rect x="102" y="198" width="56" height="58" rx="16"/>'
        '<path class="bm-line" d="M130 204 V250 M118 214 H142 M118 228 H142 M118 242 H142"/></g>'
        f'<g style="--c:{col["isquios"]}"><path d="M92 332 Q106 326 121 332 L117 404 Q104 412 92 402 Z"/>'
        '<path d="M168 332 Q154 326 139 332 L143 404 Q156 412 168 402 Z"/></g>'
        f'<g style="--c:{col["aquiles"]}"><ellipse cx="104" cy="440" rx="11" ry="22"/><rect x="101" y="462" width="6" height="40" rx="3"/>'
        '<ellipse cx="156" cy="440" rx="11" ry="22"/><rect x="153" y="462" width="6" height="40" rx="3"/></g>'
    )
    labels = (
        '<path class="bm-lead" d="M158 226 H232"/><text x="236" y="222">Región lumbar</text><text class="sub" x="236" y="238">Módulo 3 · lumbalgia crónica</text>'
        '<path class="bm-lead" d="M168 366 H232"/><text x="236" y="362">Isquiosurales</text><text class="sub" x="236" y="378">Módulo 2 · lesión muscular</text>'
        '<path class="bm-lead" d="M160 480 H232"/><text x="236" y="476">Tendón de Aquiles</text><text class="sub" x="236" y="492">Módulo 1 · tendinopatía</text>'
    )
    return (
        '<figure class="bodymap reveal"><svg viewBox="20 8 480 512" role="img" aria-labelledby="bm-t">'
        '<title id="bm-t">Vista posterior del cuerpo con las tres regiones del plan</title>'
        f'<g class="bm-body">{body}</g><g class="bm-hi">{hi}</g><g class="bm-txt">{labels}</g></svg>'
        '<figcaption class="small soft">Vista posterior, esquema ilustrativo, no a escala. Un mismo motor de reglas para las tres regiones.</figcaption></figure>'
    )
