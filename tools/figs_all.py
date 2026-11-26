"""Figures for Chapters 1 to 16 and 18 of Geometric Communication (2026-11-26).

Every figure is drawn from a formula, a definition or numbers printed in its chapter. Numbers on
the "Unresolved" list of CORRECTIONS-2026-11-26.md are not drawn, and nothing marked withdrawn
(the dihedral group D4 and what was derived from it) is drawn. Figure numbers reuse the number
of the bracketed placeholder a figure realises; a figure with no placeholder is numbered after
the chapter's last placeholder.
"""

import itertools
import math

from figkit import BORDER, BOX, CRITICAL, GRID, INK, INK2, INK3, SERIES, SURFACE, Axes, Canvas, legend, reg
from svgfig import bar_chart, grouped_bars

P1 = "manuscript/part_i/"
P2 = "manuscript/part_ii/"
P3 = "manuscript/part_iii/"
P4 = "manuscript/part_iv/"
P5 = "manuscript/part_v/"
P6 = "manuscript/part_vi/"
P7 = "manuscript/part_vii/"


def _circle(c, cx, cy, r, stroke, width=1.5, fill="none", opacity=1.0, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{fill}" fill-opacity="{opacity}" '
          f'stroke="{stroke}" stroke-width="{width}"{da}/>')


def _panel(c, x0, y0, w, h):
    c.add(f'<rect x="{x0:.2f}" y="{y0:.2f}" width="{w:.2f}" height="{h:.2f}" rx="4" fill="none" '
          f'stroke="{GRID}" stroke-width="1"/>')
    c.line(x0, y0 + h / 2, x0 + w, y0 + h / 2, GRID, 1)
    c.line(x0 + w / 2, y0, x0 + w / 2, y0 + h, GRID, 1)


# ------------------------------------------------------------------ chapter 1
def fig_1_4():
    pts = {"A": (0.85, 0.15), "B": (0.15, 0.85), "M": (0.50, 0.50)}
    score = {k: (a + f) / 2 for k, (a, f) in pts.items()}
    assert all(abs(v - 0.5) < 1e-12 for v in score.values())
    p = reg(P1 + "ch01_perplexity_trap.md", "1.1",
            "Schematic of Theorem 1.1 for two of the quality dimensions the chapter lists, semantic adequacy "
            "(horizontal) and fluency (vertical), and an illustrative scalar, the mean of the two. Each slanted line "
            "is a level set: every point on it receives the same score. Translations A, B and M lie on the line of "
            "score 0.5 and differ in which dimension is strong. With d dimensions the level set has dimension d - 1.",
            "## 1.5 What This Costs")
    c = Canvas(720, 400, "One score, a whole line of different translations")
    ax = Axes(c, 70, 50, 290, 290, (0, 1), (0, 1), [0, 0.5, 1], [0, 0.5, 1], "semantic adequacy", "fluency")
    for cv in (0.2, 0.35, 0.65, 0.8):
        a, b = ((0, 2 * cv), (2 * cv, 0)) if 2 * cv <= 1 else ((2 * cv - 1, 1), (1, 2 * cv - 1))
        c.line(ax.X(a[0]), ax.Y(a[1]), ax.X(b[0]), ax.Y(b[1]), INK3, 1, dash="4 4", opacity=0.7)
    c.line(ax.X(0), ax.Y(1), ax.X(1), ax.Y(0), SERIES[0], 2.5)
    c.text(ax.X(0.62), ax.Y(0.62) - 8, "score 0.5", 11, "start", INK2, italic=True)
    for i, (k, (a, f)) in enumerate(pts.items()):
        c.dot(ax.X(a), ax.Y(f), SERIES[1], 5.5, title=f"{k}: adequacy {a}, fluency {f}, score {score[k]}")
        c.text(ax.X(a) - 12, ax.Y(f) + 16, k, 13, "end", INK, "600")
    x0 = 420
    c.text(x0, 84, "Three translations, one score", 12.5, "start", INK, "600")
    rows = [("A", "adequate, not fluent", "(0.85, 0.15)"), ("B", "fluent, not adequate", "(0.15, 0.85)"),
            ("M", "mediocre on both", "(0.50, 0.50)")]
    for i, (k, what, co) in enumerate(rows):
        y = 110 + 22 * i
        c.text(x0, y, k, 12, "start", INK, "600")
        c.text(x0 + 20, y, what, 11.5, "start", INK2)
        c.text(x0 + 284, y, co, 11.5, "end", INK2)
    c.text(x0, 190, "score = (adequacy + fluency) / 2 = 0.5 for all three", 11.5, "start", INK2, italic=True)
    ya = 262
    c.text(x0, ya - 34, "what the scalar keeps", 11.5, "start", INK2)
    c.line(x0, ya, x0 + 270, ya, INK3, 1.5)
    for v in (0, 0.5, 1):
        c.line(x0 + 270 * v, ya - 4, x0 + 270 * v, ya + 4, INK3, 1.5)
        c.text(x0 + 270 * v, ya + 20, f"{v:g}", 11, "middle", INK2)
    c.dot(x0 + 135, ya, SERIES[1], 5.5)
    c.text(x0 + 135, ya - 12, "A, B and M", 11.5, "middle", INK)
    c.text(x0, 322, "dashed: level sets of other scores", 11, "start", INK3, italic=True)
    c.text(x0, 340, "(0.2, 0.35, 0.65, 0.8)", 11, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 2
def fig_2_3():
    def P(v, n, k):
        return 130 + 190 * v + 95 * n, 322 - 60 * n - 180 * k

    verts = list(itertools.product((0, 1), repeat=3))
    edges = [(a, b) for a in verts for b in verts if a < b and sum(x != y for x, y in zip(a, b)) == 1]
    assert len(verts) == 8 and len(edges) == 12
    b_, p_ = (1, 0, 1), (0, 0, 1)   # /b/ = [+voiced, -nasal, +compact], /p/ = the same with voiced flipped
    assert sum(x != y for x, y in zip(b_, p_)) == 1
    p = reg(P1 + "ch02_saussure.md", "2.1",
            "Three of Jakobson's binary features as the cube of sign patterns. Each vertex is one bundle of feature "
            "values and each edge flips one feature. The chapter's example is marked: /b/ is voiced, oral and compact, "
            "/p/ differs from it in voicing alone, and that single edge is the minimal pair bat and pat. The fourth "
            "feature of the example, grave, is held at plus, and the other vertices are left unlabelled because the "
            "chapter assigns no phonemes to them.",
            "### 2.2.2 Chomsky's Deep Structure: A Quotient Manifold")
    c = Canvas(720, 400, "A minimal pair is one edge of the feature cube")
    for a, b in edges:
        (x1, y1), (x2, y2) = P(*a), P(*b)
        if {a, b} == {b_, p_}:
            continue
        back = a[1] == 1 and b[1] == 1 or (a[1] != b[1] and a[0] == 0 and a[2] == 0)
        c.line(x1, y1, x2, y2, INK3, 1.5, opacity=0.5 if back else 0.9)
    (x1, y1), (x2, y2) = P(*p_), P(*b_)
    c.line(x1, y1, x2, y2, CRITICAL, 3.5)
    c.text((x1 + x2) / 2, y1 - 12, "flip voiced: pat / bat", 11.5, "middle", INK)
    for v in verts:
        x, y = P(*v)
        if v in (b_, p_):
            c.dot(x, y, SERIES[0], 7)
        else:
            _circle(c, x, y, 4.5, INK3, 1.5, SURFACE, 1.0)
    c.text(x1 - 14, y1 + 5, "/p/", 14, "end", INK, "600")
    c.text(x2 + 12, y2 + 22, "/b/", 14, "start", INK, "600")
    c.text(225, 350, "voiced:  −  →  +", 11.5, "middle", INK2)
    c.text(382, 306, "nasal:  −  →  +", 11.5, "start", INK2)
    c.text(118, 236, "compact", 11.5, "end", INK2)
    c.text(118, 252, "−  →  +  (up)", 11, "end", INK3)
    x0 = 486
    c.text(x0, 96, "vertex: one bundle of features", 11.5, "start", INK2)
    c.text(x0, 116, "edge: one feature flipped", 11.5, "start", INK2)
    c.text(x0, 156, "/b/ = [+voiced, −nasal, +compact]", 11.5, "start", INK)
    c.text(x0, 176, "/p/ = [−voiced, −nasal, +compact]", 11.5, "start", INK)
    c.text(x0, 216, "8 vertices, 12 edges", 11.5, "start", INK2)
    c.text(x0, 236, "group of flips: (Z/2Z)³", 11.5, "start", INK2)
    c.text(x0, 276, "grave held at + for both", 11, "start", INK3, italic=True)
    c.save(p)


def fig_2_4():
    p = reg(P1 + "ch02_saussure.md", "2.2",
            "Schematic of the quotient the section describes. Each vertical line is a fibre: the surface forms that "
            "syntactic transformations turn into one another. The projection sends every form in a fibre to one point "
            "of the quotient S/T, its deep structure. The active and passive sentences are the chapter's example of "
            "two forms in one fibre.",
            "### 2.2.3 Montague Grammar: Coordinate-Free Semantics")
    c = Canvas(720, 400, "Surface forms in one fibre share one deep structure")
    fx1, fx2, top, bot, base = 200, 560, 66, 268, 336
    for fx in (fx1, fx2):
        c.line(fx, top, fx, bot, SERIES[2], 2)
        c.arrow(fx, bot + 8, fx, base - 12, INK3, 1.5)
    c.text(fx1 - 12, (bot + base) / 2 + 4, "projection", 11, "end", INK2, italic=True)
    c.line(90, base, 690, base, INK3, 2)
    c.text(90, base + 24, "S/T: deep structures", 11.5, "start", INK2)
    c.text(90, 62, "S: surface forms", 11.5, "start", INK2)
    ys = (106, 176, 236)
    c.dot(fx1, ys[0], SERIES[0], 5.5)
    c.text(fx1 + 14, ys[0] + 4, "The king issued the decree.", 12, "start", INK)
    c.dot(fx1, ys[1], SERIES[0], 5.5)
    c.text(fx1 + 14, ys[1] + 4, "The decree was issued by the king.", 12, "start", INK)
    c.dot(fx1, ys[2], SERIES[0], 4)
    c.text(fx1 + 14, ys[2] + 4, "other forms (clefted, topicalised, ...)", 11.5, "start", INK2)
    c.arrow(fx1 - 14, ys[0] + 6, fx1 - 14, ys[1] - 6, INK2, 1.5)
    c.arrow(fx1 - 14, ys[1] - 6, fx1 - 14, ys[0] + 6, INK2, 1.5)
    c.text(fx1 - 24, (ys[0] + ys[1]) / 2 - 3, "passivization,", 11, "end", INK2)
    c.text(fx1 - 24, (ys[0] + ys[1]) / 2 + 12, "an element of T", 11, "end", INK2)
    for y in (116, 166, 216):
        c.dot(fx2, y, SERIES[1], 4)
    c.text(fx2 + 14, 170, "forms of another", 11.5, "start", INK2)
    c.text(fx2 + 14, 186, "sentence", 11.5, "start", INK2)
    c.dot(fx1, base, SERIES[0], 6)
    c.dot(fx2, base, SERIES[1], 6)
    c.text(fx1 + 12, base + 24, "one deep structure", 11.5, "start", INK)
    c.text(fx2, base + 24, "another", 11.5, "middle", INK)
    c.save(p)


# ------------------------------------------------------------------ chapter 3
def fig_3_1():
    pos = {"S": {"A": 0.14, "B": 0.30, "C": 0.90}, "P": {"A": 0.80, "B": 0.16, "C": 0.90},
           "C": {"A": 0.74, "B": 0.48, "C": 0.82}}
    d = lambda f, a, b: abs(pos[f][a] - pos[f][b])
    assert d("S", "A", "B") < d("S", "A", "C") and d("P", "A", "C") < d("P", "A", "B")
    assert d("C", "A", "C") < d("C", "A", "B") < d("P", "A", "B")
    p = reg(P1 + "ch03_communication_manifold.md", "3.1",
            "Schematic: the three apologies of the worked example placed on each factor of M = S × P × C. Positions "
            "are illustrative; only which pairs are near and which are far is taken from the text. A and C are far "
            "apart in signal and close in pragmatics and content; A and B are closer in signal and far apart in "
            "pragmatics. A score read off any one line cannot show both facts.",
            "### 3.1.4 Why Product Structure Matters")
    c = Canvas(720, 400, "Near on one factor, far on another: three apologies")
    rows = [("S", "signal", "A, B: English.  C: spoken Japanese with a bow."),
            ("P", "pragmatics", "A, C: genuine, face to face.  B: casual, two hours late."),
            ("C", "content", "A, C: lateness, fault acknowledged.  B: cause left vague.")]
    col = {"A": SERIES[0], "B": SERIES[1], "C": SERIES[2]}
    x0, w = 190, 480
    for i, (f, name, note) in enumerate(rows):
        y = 100 + 96 * i
        c.text(40, y - 2, f, 20, "start", INK, "600")
        c.text(66, y - 3, name, 12, "start", INK2)
        c.line(x0, y, x0 + w, y, INK3, 1.5)
        c.text(x0, y + 32, note, 11, "start", INK2)
        for k in "ABC":
            x = x0 + w * pos[f][k]
            c.dot(x, y, col[k], 6.5, title=f"apology {k} on {name}")
            c.text(x, y - 14, k, 12.5, "middle", INK, "600")
    legend(c, 40, 380, [("A spoken English, in person", col["A"]), ("B text message", col["B"]),
                        ("C spoken Japanese", col["C"])], 11)
    c.save(p)


# ------------------------------------------------------------------ chapter 4
def _geodesic(c, cx, cy, R, pt, q, stroke, width=1.5):
    """Poincare-disk geodesic between unit-disk points pt and q: the arc of the circle orthogonal to the boundary."""
    det = pt[0] * q[1] - pt[1] * q[0]
    X = lambda v: (cx + R * v[0], cy - R * v[1])
    (x1, y1), (x2, y2) = X(pt), X(q)
    if abs(det) < 1e-9:
        c.line(x1, y1, x2, y2, stroke, width)
        return
    a = (1 + pt[0] ** 2 + pt[1] ** 2) / 2
    b = (1 + q[0] ** 2 + q[1] ** 2) / 2
    ctr = ((a * q[1] - b * pt[1]) / det, (pt[0] * b - q[0] * a) / det)
    rad = math.sqrt(ctr[0] ** 2 + ctr[1] ** 2 - 1)
    assert abs(math.hypot(pt[0] - ctr[0], pt[1] - ctr[1]) - rad) < 1e-9   # the circle passes through both points
    ox, oy = X(ctr)
    sweep = 1 if (x1 - ox) * (y2 - oy) - (y1 - oy) * (x2 - ox) > 0 else 0
    c.add(f'<path d="M{x1:.2f},{y1:.2f} A{rad * R:.2f},{rad * R:.2f} 0 0 {sweep} {x2:.2f},{y2:.2f}" fill="none" '
          f'stroke="{stroke}" stroke-width="{width}" stroke-linecap="round"/>')


def fig_4_1():
    radius = lambda dist: math.tanh(dist / 2)          # Definition 4.5 at c = 1, distance from the origin
    circ = [radius(k) for k in range(1, 6)]
    assert abs(2 * math.atanh(circ[2]) - 3) < 1e-12
    assert [round(r, 2) for r in circ] == [0.46, 0.76, 0.91, 0.96, 0.99]
    step, depth = 0.8, 4
    p = reg(P2 + "ch04_three_geometries.md", "4.1",
            "The Poincare disk with c = 1. The grey circles lie at hyperbolic distances 1 to 5 from the centre, "
            "computed from Definition 4.5: equal steps of distance, and Euclidean radii 0.46, 0.76, 0.91, 0.96 and "
            "0.99 that crowd toward the boundary. A binary tree of depth 4 is placed with level k at hyperbolic "
            "distance 0.8 k (an illustrative spacing); its edges are geodesics, arcs that meet the boundary at right "
            "angles. The number of nodes doubles at each level and the disk still has room for them near the edge.",
            "### 4.1.4 Classification via Hyperbolic Prototypes")
    c = Canvas(720, 420, "Equal hyperbolic steps crowd toward the edge of the disk")
    cx, cy, R = 215, 228, 172
    _circle(c, cx, cy, R, INK2, 2)
    for k, r in enumerate(circ, 1):
        _circle(c, cx, cy, R * r, INK3, 1, dash="3 4")
    for k in (1, 2, 3):
        c.text(cx + 4, cy - R * circ[k - 1] - 3, str(k), 10.5, "start", INK2)
    node = lambda k, j: (0.0, 0.0) if k == 0 else (
        radius(step * k) * math.cos(2 * math.pi * (j + 0.5) / 2 ** k + math.pi / 2),
        radius(step * k) * math.sin(2 * math.pi * (j + 0.5) / 2 ** k + math.pi / 2))
    for k in range(depth):
        for j in range(2 ** k):
            for ch in (2 * j, 2 * j + 1):
                _geodesic(c, cx, cy, R, node(k, j), node(k + 1, ch), SERIES[0], 1.5)
    for k in range(depth + 1):
        for j in range(2 ** k):
            x, y = node(k, j)
            c.dot(cx + R * x, cy - R * y, SERIES[1] if k == 0 else SERIES[0], 4.5 if k == 0 else 3.2)
    x0 = 440
    c.text(x0, 84, "hyperbolic distance from centre", 11.5, "start", INK, "600")
    c.text(x0, 102, "and the Euclidean radius of its circle", 11.5, "start", INK, "600")
    for k, r in enumerate(circ, 1):
        y = 106 + 20 * k
        c.text(x0 + 30, y, str(k), 11.5, "end", INK2)
        c.line(x0 + 44, y - 4, x0 + 44 + 170 * r, y - 4, INK3, 2)
        c.text(x0 + 44 + 170 * r + 8, y, f"{r:.2f}", 11.5, "start", INK)
    c.text(x0, 258, "tree level and number of nodes", 11.5, "start", INK, "600")
    for k in range(depth + 1):
        c.text(x0 + 30, 280 + 20 * k, str(k), 11.5, "end", INK2)
        c.text(x0 + 44, 280 + 20 * k, f"{2 ** k} node" + ("" if k == 0 else "s"), 11.5, "start", INK2)
    c.text(16, 410, "radius of the circle at distance d: tanh(d / 2), from Definition 4.5 with c = 1", 10.5, "start",
           INK3, italic=True)
    c.save(p)


def fig_4_4():
    T, tau = 100, 10
    sig = [("a pure tone", "sin(2π t / T), T = 100", lambda t: math.sin(2 * math.pi * t / T), 100, 1.25),
           ("a decaying pulse", "exp(−0.02 t)", lambda t: math.exp(-0.02 * t), 300, 1.25),
           ("two tones", "periods 100 and 100·√2", lambda t: math.sin(2 * math.pi * t / T)
            + math.sin(2 * math.pi * t / (T * math.sqrt(2))), 4000, 2.3)]
    p = reg(P2 + "ch04_three_geometries.md", "4.2",
            "Time-delay embedding (Definition 4.12) of three signals, drawn in the plane of the first two delay "
            "coordinates, x(t) across and x(t + 10) up, with the delay of 10 samples the chapter uses. A pure tone "
            "traces one closed loop. A decaying exponential traces a segment with no loop. Two tones whose periods "
            "have an irrational ratio never close up and fill a band, the flat shadow of a torus.",
            "### 4.3.3 The Rips Complex and Persistent Homology")
    c = Canvas(720, 400, "The shape of the delay cloud records the kind of signal")
    for i, (name, formula, f, n, lim) in enumerate(sig):
        x0, y0, w = 36 + 228 * i, 56, 192
        _panel(c, x0, y0, w, w)
        X = lambda v: x0 + w / 2 + (w / 2) * v / lim
        Y = lambda v: y0 + w / 2 - (w / 2) * v / lim
        pts = [(X(f(t)), Y(f(t + tau))) for t in range(n + 1)]
        c.polyline(pts, SERIES[i], 2 if i < 2 else 0.8, title=name)
        if i == 0:   # closed after one period
            assert abs(f(0) - f(T)) < 1e-9 and abs(f(tau) - f(T + tau)) < 1e-9
        if i == 1:   # every point is a multiple of (1, exp(-0.02 tau)): a straight segment
            assert all(abs(f(t + tau) / f(t) - math.exp(-0.02 * tau)) < 1e-12 for t in range(0, n, 50))
        c.text(x0 + w / 2, y0 + w + 22, name, 12.5, "middle", INK, "600")
        c.text(x0 + w / 2, y0 + w + 40, formula, 11, "middle", INK2)
    c.text(36 + 96, 56 + 192 + 62, "x(t) across, x(t + 10) up, in every panel", 10.5, "middle", INK3, italic=True)
    c.text(704, 390, "first two of the three delay coordinates", 10.5, "end", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 5
def fig_5_2():
    hyp = lambda r: 2 * math.atanh(r)        # d(x, 0) of Section 5.2.2 at c = 1
    marks = [(0.5, 1.10), (0.9, 2.94), (0.99, 5.29)]
    for r, v in marks:
        assert abs(hyp(r) - v) < 0.005
    p = reg(P2 + "ch05_hyperbolic_embeddings.md", "5.1",
            "Hyperbolic distance from the origin against Euclidean radius on the Poincare ball with c = 1, from the "
            "formula of Section 5.2.2. Near the origin the curve follows the dashed line 2 r, the approximation the "
            "text gives. Toward the boundary it leaves the line and grows without bound: a point at radius 0.9 is at "
            "distance 2.94 and a point at radius 0.99 is at distance 5.29.",
            "## 5.3 The Distortion Theorem")
    c = Canvas(720, 400, "Distance from the origin grows without bound near the boundary")
    ax = Axes(c, 70, 52, 540, 280, (0, 1), (0, 6), [0, 0.25, 0.5, 0.75, 1], [0, 1, 2, 3, 4, 5, 6],
              "Euclidean radius of the point", "hyperbolic distance from the origin")
    c.line(ax.X(0), ax.Y(0), ax.X(1), ax.Y(2), INK3, 1.5, dash="5 5")
    rs = [i / 1000 for i in range(0, 996)]
    c.polyline([(ax.X(r), ax.Y(hyp(r))) for r in rs], SERIES[0], 2.5, title="2 artanh(r)")
    for r, v in marks:
        c.dot(ax.X(r), ax.Y(hyp(r)), SERIES[0], 4.5, title=f"radius {r}, distance {hyp(r):.2f}")
        c.text(ax.X(r) - 12, ax.Y(hyp(r)) - 6, f"radius {r:g}: distance {v:.2f}", 11, "end", INK)
    c.text(ax.X(1) - 6, ax.Y(0.85), "dashed: 2 r, the near-origin approximation", 11, "end", INK2, italic=True)
    c.text(ax.X(0.03), ax.Y(5.5), "distance = 2 artanh(r)", 11.5, "start", INK2, italic=True)
    c.save(p)


def fig_5_5():
    acc = [("HyperbolicMLR", 74.3), ("random forest", 72.8), ("logistic regression", 71.2), ("5 nearest neighbours", 69.4)]
    assert abs((acc[0][1] - acc[1][1]) - 1.5) < 1e-9
    p = reg(P2 + "ch05_hyperbolic_embeddings.md", "5.2",
            "Accuracy of four classifiers on the 28 coda types, as the chapter reports them, on one 80/20 stratified "
            "random split of the same 11 features. The vertical axis is accuracy in percent and starts at zero. The "
            "hyperbolic classifier leads the best Euclidean baseline by 1.5 points, a margin the chapter calls modest "
            "and warns against over-reading, since codas of one whale can fall on both sides of the split.",
            "### 5.5.4 What the Embedding Reveals")
    bar_chart(p, "Coda classification: the four methods lie within five points",
              [a for a, _ in acc], [v for _, v in acc], ylabel="accuracy (%)", ylim=(0, 100),
              yticks=[0, 25, 50, 75, 100], colors=[SERIES[0], SERIES[1], SERIES[1], SERIES[1]],
              note="as reported in Section 5.5.3; one random split, not grouped by whale or session")


# ------------------------------------------------------------------ chapter 6
def fig_6_2():
    T = 100
    acf = lambda tau: math.cos(2 * math.pi * tau / T)   # autocorrelation of a pure tone at lag tau
    assert abs(acf(25)) < 1e-12 and all(acf(t) > 0 for t in range(25))   # first zero crossing at T / 4
    cases = [(2, "delay 2: too small", "the cloud hugs the diagonal"),
             (25, "delay 25, a quarter period", "an open loop: a circle"),
             (50, "delay 50, half a period", "collapsed again, onto the anti-diagonal")]
    p = reg(P2 + "ch06_tda_signal.md", "6.1",
            "The effect of the delay on the reconstructed cloud of a pure tone of period 100 samples, with x(t) "
            "across and x(t + delay) up. A delay that is too small leaves the two coordinates nearly equal and the "
            "loop is squeezed onto the diagonal. At a quarter period, the first zero crossing of the autocorrelation, "
            "the loop is fully open, and for this signal a delay of half a period squeezes it again. The loop is the "
            "feature persistent homology is meant to find, so the delay sets how well it can be seen.",
            "## 6.2 Persistent Homology: Extracting Topology from Point Clouds")
    c = Canvas(720, 400, "The delay decides whether the loop of a tone is visible")
    for i, (tau, name, note) in enumerate(cases):
        x0, y0, w = 36 + 228 * i, 56, 192
        _panel(c, x0, y0, w, w)
        pts = [(x0 + w / 2 + (w / 2) * math.sin(2 * math.pi * t / T) / 1.25,
                y0 + w / 2 - (w / 2) * math.sin(2 * math.pi * (t + tau) / T) / 1.25) for t in range(T + 1)]
        c.polyline(pts, SERIES[0], 2)
        for t in range(0, T, 5):
            c.dot(pts[t][0], pts[t][1], SERIES[0], 2.6)
        c.text(x0 + w / 2, y0 + w + 22, name, 12.5, "middle", INK, "600")
        c.text(x0 + w / 2, y0 + w + 40, note, 11, "middle", INK2)
    c.text(16, 390, "signal sin(2π t / 100); x(t) across, x(t + delay) up", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_6_3():
    n = 12
    pts = [(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n)) for k in range(n)]
    chord = lambda k: 2 * math.sin(math.pi * k / n)
    birth = chord(1)
    # The loop is filled when a triangle of the complex encloses the centre: three arcs a + b + c = n, each a chord
    # within the scale. The smallest largest-arc is n / 3 = 4 steps, so the loop dies at the chord of 4 steps.
    kmin = min(max(a, b, n - a - b) for a in range(1, n) for b in range(1, n - a))
    death = chord(kmin)
    assert kmin == 4 and abs(death - math.sqrt(3)) < 1e-12 and abs(birth - 0.518) < 5e-4
    life = death - birth
    p = reg(P2 + "ch06_tda_signal.md", "6.2",
            f"The Vietoris-Rips filtration of twelve points on a circle of radius 1 (Definition 6.2). Below scale "
            f"{birth:.2f}, the spacing of neighbours, the points are twelve separate components; at {birth:.2f} "
            f"neighbours join, eleven components die and one loop is born. The loop lasts until scale {death:.2f}, "
            f"when triangles first cover the centre. In the persistence diagram, birth across and death up, the loop "
            f"stands far above the diagonal with lifetime {life:.2f}; the eleven components sit at birth 0.",
            "### 6.2.4 Homology Dimensions and Their Interpretation")
    c = Canvas(720, 400, "A ring of points gives one long-lived loop")
    for i, (eps, lab1, lab2) in enumerate([(0.40, "scale 0.40", "12 components"), (0.60, "scale 0.60", "one loop"),
                                           (1.80, "scale 1.80", "loop filled in")]):
        cx, cy, R = 80 + 138 * i, 178, 52
        S = lambda q: (cx + R * q[0], cy - R * q[1])
        if eps >= death:
            c.add('<polygon points="' + " ".join(f"{S(q)[0]:.1f},{S(q)[1]:.1f}" for q in pts)
                  + f'" fill="{SERIES[0]}" fill-opacity="0.22"/>')
        for a in range(n):
            for b in range(a + 1, n):
                if math.dist(pts[a], pts[b]) <= eps:
                    c.line(*S(pts[a]), *S(pts[b]), SERIES[0], 1.2, opacity=0.9 if eps < 1 else 0.45)
        for q in pts:
            c.dot(*S(q), INK, 3)
        c.text(cx, cy + R + 30, lab1, 12, "middle", INK, "600")
        c.text(cx, cy + R + 47, lab2, 11, "middle", INK2)
    ax = Axes(c, 480, 60, 210, 210, (0, 2), (0, 2), [0, 0.5, 1, 1.5, 2], [0, 0.5, 1, 1.5, 2], "birth scale", "death scale")
    c.line(ax.X(0), ax.Y(0), ax.X(2), ax.Y(2), INK3, 1.5, dash="4 4")
    c.text(ax.X(1.45), ax.Y(1.22), "diagonal", 10.5, "start", INK3, italic=True)
    c.dot(ax.X(0), ax.Y(birth), SERIES[1], 5, title=f"11 components, death {birth:.3f}")
    c.text(ax.X(0) + 11, ax.Y(birth) + 4, "× 11", 11, "start", INK)
    c.dot(ax.X(birth), ax.Y(death), SERIES[0], 6, title=f"loop, birth {birth:.3f}, death {death:.3f}")
    c.text(ax.X(birth) + 11, ax.Y(death) + 4, "the loop", 11, "start", INK)
    legend(c, 480, 42, [("H0 components", SERIES[1]), ("H1 loop", SERIES[0])], 11)
    c.text(16, 390, f"neighbour spacing 2 sin(π/12) = {birth:.3f}; side of the inscribed triangle √3 = {death:.3f}",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 7
def fig_7_11():
    w = {"rhythm": 1.0, "tempo": 0.7, "rubato": 0.4, "ornamentation": 0.2}
    omega = lambda diff: 0.0 if not diff else max(0.5, 0.5 + 0.5 * sum(w[f] for f in diff) / sum(w.values()))
    cases = [("no flip", []), ("ornamentation", ["ornamentation"]), ("rubato", ["rubato"]), ("tempo", ["tempo"]),
             ("rhythm", ["rhythm"]), ("all four", list(w))]
    vals = [round(omega(d), 3) for _, d in cases]
    assert vals == [0.0, 0.543, 0.587, 0.652, 0.717, 1.0]
    p = reg(P3 + "ch07_whale_communication.md", "7.1",
            "The graduated distance of Section 7.4.2 between the coda type a decoder gives before and after a "
            "perturbation, computed from the chapter's formula and weights (rhythm 1.0, tempo 0.7, rubato 0.4, "
            "ornamentation 0.2). The bars are the cases in which the two types differ in one feature only, and in all "
            "four. Any flip costs at least 0.5, and a flip of rhythm costs more than a flip of ornamentation. The "
            "Decoder Robustness Index is a weighted summary of these distances over all perturbations.",
            "### 7.4.3 The Transform Sensitivity Spectrum")
    bar_chart(p, "A flip of rhythm counts for more than a flip of ornamentation",
              [a for a, _ in cases], vals, ylabel="distance ω", ylim=(0, 1.12), yticks=[0, 0.25, 0.5, 0.75, 1.0],
              refline=0.5, reflabel="floor for any flip", reflabel_anchor="start",
              note="feature in which the two coda types differ; computed from the formula of Section 7.4.2")


def fig_7_8():
    ranks = list(range(1, 29))
    a_coda, a_lang = 1.44, 1.0
    f = lambda r, a: r ** (-a)
    assert f(28, a_coda) < f(28, a_lang)
    p = reg(P3 + "ch07_whale_communication.md", "7.2",
            "The power law the chapter fits to the rank-frequency distribution of the 28 coda types, exponent 1.44, "
            "beside the exponent near 1.0 that is typical of human language. Rank is across and frequency relative "
            "to the most frequent type is up, both on logarithmic scales, so each law is a straight line. Only the "
            "fitted laws are drawn; the chapter does not print the counts. It calls the fit descriptive and does not "
            "claim a true power law.",
            "### 7.5.4 Sequential Structure: Markov Chains on Coda Space")
    c = Canvas(720, 400, "The fitted coda law falls faster than the law of human language")
    ax = Axes(c, 70, 56, 560, 268, (1, 28), (0.005, 1), [1, 2, 5, 10, 20, 28], [0.01, 0.1, 1],
              "rank of the coda type", "frequency relative to rank 1", xlog=True, ylog=True)
    for j, (a, name) in enumerate([(a_coda, "coda types, fitted exponent 1.44"), (a_lang, "human language, about 1.0")]):
        pts = [(ax.X(r), ax.Y(f(r, a))) for r in ranks]
        c.polyline(pts, SERIES[j], 2, title=name)
        for r, (x, y) in zip(ranks, pts):
            c.dot(x, y, SERIES[j], 2.6, title=f"{name}: rank {r}, {f(r, a):.3f}")
    legend(c, 70, 42, [("coda types, fitted exponent 1.44", SERIES[0]), ("human language, about 1.0", SERIES[1])])
    c.text(16, 390, "curves r^(−α) for ranks 1 to 28; the fit is descriptive (Section 7.5.3)", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 8
def fig_8_3():
    paths = [("nearly straight", "a descending whistle, in the chapter's reading",
              [(0, 0), (1, 0.06), (2, -0.05), (3, 0.07), (4, 0.0), (5, 0.06), (6, -0.04), (7, 0.0)]),
             ("wandering", "a complex song, in the chapter's reading",
              [(0, 0.3), (1.4, 1.9), (0.3, 3.0), (2.5, 3.3), (3.3, 1.5), (2.1, 0.4), (4.1, 0.7), (4.6, 2.4)])]
    p = reg(P3 + "ch08_birdsong.md", "8.1",
            "Schematic of the geodesic deviation of Section 8.3.2. Each path is a sequence of eight covariance "
            "matrices, drawn as points in the flat log-Euclidean space where the distance is the straight-line "
            "length. The deviation is the length of the path minus the direct distance between its two ends (dashed). "
            "It is close to zero for a path that goes straight and large for one that wanders; the coordinates are "
            "illustrative and the lengths printed are computed from them.",
            "### 8.3.3 Connection to Geodesic Deviation in the Parent Theory")
    c = Canvas(720, 400, "Deviation: how much longer the path is than the direct route")
    u = 40
    for i, (name, reading, pts) in enumerate(paths):
        L = sum(math.dist(a, b) for a, b in zip(pts[:-1], pts[1:]))
        dgeo = math.dist(pts[0], pts[-1])
        dev = L - dgeo
        assert dev >= 0
        x0, yb = (40, 250) if i == 0 else (430, 250)
        S = lambda q: (x0 + u * q[0], yb - u * q[1] - (60 if i == 0 else 0))
        c.line(*S(pts[0]), *S(pts[-1]), INK3, 1.5, dash="5 5")
        c.polyline([S(q) for q in pts], SERIES[i], 2)
        for q in pts:
            c.dot(*S(q), SERIES[i], 4)
        c.text(S(pts[0])[0] - 4, S(pts[0])[1] + 22, "start", 10.5, "middle", INK2)
        c.text(S(pts[-1])[0] + 4, S(pts[-1])[1] + (22 if i == 0 else -12), "end", 10.5, "middle", INK2)
        c.text(x0, 300, name, 12.5, "start", INK, "600")
        c.text(x0, 318, reading, 11, "start", INK2)
        c.text(x0, 342, f"path {L:.2f},  direct {dgeo:.2f},  deviation {dev:.2f}", 11.5, "start", INK)
        if i == 0:
            assert dev < 0.05
        else:
            assert dev > 5
    c.text(16, 390, "schematic units; deviation = path length − direct distance, never negative", 10.5, "start", INK3,
           italic=True)
    c.save(p)


def fig_8_5():
    minutes = {"Audio loading + mel": 5, "EfficientNet-B3": 40, "EfficientNet-B0": 15, "Geometric features": 2.5,
               "LightGBM predict": 0.5, "Ensemble + I/O": 0.5}
    total = 63.5   # the chapter prints 63.5, the sum of its rows (corrected 2026-11-26; it printed 63)
    assert abs(sum(minutes.values()) - 63.5) < 1e-9
    share = lambda k: round(100 * minutes[k] / total, 1)
    assert round(share("Geometric features")) == 4   # "approximately 4% of the total inference budget"
    weights = [45, 25, 30]
    assert sum(weights) == 100
    p = reg(P3 + "ch08_birdsong.md", "8.2",
            "Share of the estimated inference time against ensemble weight for the three models of the BirdCLEF "
            "system, from the budget table of Section 8.6.1 and the weights of Section 8.1.3. Time shares are minutes "
            "out of the table's total of 63.5; the geometric bar is feature extraction, 2.5 minutes, and the "
            "LightGBM prediction adds a further half minute. As the chapter reports, the geometric features take "
            "about 4 percent of the time and carry 30 percent of the weight. The weights were tuned on a validation "
            "set; the chapter prints no accuracy for the separate models.",
            "### 8.6.2 What Geometry Buys Under Constraint")
    grouped_bars(p, "Geometric features: 4 percent of the time, 30 percent of the weight",
                 ["EfficientNet-B3", "EfficientNet-B0", "geometric features + LightGBM"],
                 [("share of inference time (%)", [share("EfficientNet-B3"), share("EfficientNet-B0"),
                                                   share("Geometric features")]),
                  ("ensemble weight (%)", [float(v) for v in weights])],
                 ylabel="percent", ylim=(0, 80), yticks=[0, 20, 40, 60, 80],
                 note="time estimates and weights as printed in Sections 8.6.1 and 8.1.3")


# ------------------------------------------------------------------ chapter 9
def fig_9_1():
    p = reg(P4 + "ch09_cuneiform.md", "9.1",
            "The sign taxonomy of Section 9.3 as a tree, for the two signs the chapter uses as examples. One sign "
            "form has several readings (the sign AN is read AN, DINGIR or Anu; the sign UD has at least five "
            "readings) and each reading enters many words. The brackets show the taxonomic distance of Section 9.3.3 "
            "that the embedding starts from: 1 between two readings of one sign, 2 between readings of different "
            "signs.",
            "### 9.3.3 From Taxonomy to Embedding")
    c = Canvas(720, 400, "One sign, several readings: the taxonomy is wide and shallow")
    root, ys, yr = (400, 66), 138, 218
    signs = [("sign AN", 240, [("AN", "heaven", 150), ("DINGIR", "god", 240), ("Anu", "a deity", 330)]),
             ("sign UD", 550, [("UD", "day", 420), ("UTU", "sun", 485), ("BABBAR", "white", 550), ("u4", "when", 615),
                               ("tam", "full", 680)])]
    c.box(root[0] - 70, root[1] - 18, 140, 36, "cuneiform signs")
    for name, sx, readings in signs:
        c.line(root[0], root[1] + 18, sx, ys - 18, INK3, 1.5)
        for rd, gloss, rx in readings:
            c.line(sx, ys + 18, rx, yr - 16, INK3, 1.5)
            c.box(rx - 29, yr - 16, 58, 32, rd, fill=SURFACE, stroke=SERIES[0])
            c.text(rx, yr + 32, gloss, 10.5, "middle", INK2, italic=True)
            for dx in (-10, 0, 10):
                c.line(rx, yr + 40, rx + dx, yr + 58, INK3, 1, dash="2 3")
        c.box(sx - 45, ys - 18, 90, 36, name, fill=BOX, stroke=SERIES[1])
    for y, a, b in [(ys, "sign forms", "about 600"), (yr, "readings", "about 1,500"), (yr + 54, "words", "")]:
        c.text(16, y, a, 11.5, "start", INK, "600")
        if b:
            c.text(16, y + 16, b, 10.5, "start", INK3)
    yb = 300
    for xa, xb, lab in [(150, 240, "distance 1"), (330, 420, "distance 2")]:
        c.line(xa, yb, xb, yb, CRITICAL, 2)
        c.line(xa, yb - 5, xa, yb + 5, CRITICAL, 2)
        c.line(xb, yb - 5, xb, yb + 5, CRITICAL, 2)
        c.text((xa + xb) / 2, yb + 18, lab, 11, "middle", INK)
    c.text(16, 366, "distance 0: the same sign form.  1: different readings of one sign.  2: readings of different signs.",
           11, "start", INK2)
    c.text(16, 390, "counts for the Old Assyrian corpus as given in Section 9.3.2; only some readings are shown", 10.5,
           "start", INK3, italic=True)
    c.save(p)


def fig_9_6():
    n_par = 384 * 32 + 1
    assert n_par == 12289
    alpha = 0.1
    p = reg(P4 + "ch09_cuneiform.md", "9.2",
            "Schematic of the hyperbolic attention bias of Section 9.4.1. The attention logits are the sum of the "
            "usual content term, T5's position bias and a third term, minus α times the Poincare distance between "
            "the embeddings of the two byte tokens. The sum goes through the softmax, so the bias multiplies the "
            "unnormalised weight of a pair at distance d by exp(−α d). The curve is that factor at the starting "
            "value α = 0.1: tokens close in the sign taxonomy keep their weight and distant ones are turned down.",
            "### 9.4.2 Why Additive Bias?")
    c = Canvas(720, 420, "The geometric bias is one more term added before the softmax")
    rows = [("Q Kᵀ / √d_k", "content logits", BORDER), ("B_pos", "T5 relative position bias", BORDER),
            ("B_geo(i, j) = −α · d(e_i, e_j)", "hyperbolic bias, added", CRITICAL)]
    for i, (a, b, st) in enumerate(rows):
        y = 56 + 54 * i
        c.box(24, y, 240, 44, a, b, stroke=st)
        c.arrow(264, y + 22, 306, 132, INK2, 1.5)
    _circle(c, 322, 132, 15, INK2, 1.5, BOX, 1.0)
    c.text(322, 137, "+", 16, "middle", INK, "600")
    c.arrow(337, 132, 372, 132, INK2, 1.5)
    c.box(374, 110, 100, 44, "softmax")
    c.arrow(474, 132, 508, 132, INK2, 1.5)
    c.box(510, 110, 186, 44, "attention weights", "first four encoder layers")
    c.text(24, 262, "what is added", 12, "start", INK, "600")
    c.text(24, 284, "384 byte embeddings × 32 dimensions", 11.5, "start", INK2)
    c.text(24, 302, f"+ 1 scale α  =  {n_par:,} parameters", 11.5, "start", INK2)
    c.text(24, 326, "α is learned, starting at 0.1", 11.5, "start", INK2)
    c.text(24, 350, "embeddings start from the sign taxonomy", 11.5, "start", INK2)
    c.text(24, 368, "and are updated in training", 11.5, "start", INK2)
    ax = Axes(c, 372, 250, 310, 112, (0, 10), (0, 1), [0, 2, 4, 6, 8, 10], [0, 0.5, 1],
              "Poincare distance d between the two tokens", "")
    c.text(372, 236, "factor on the unnormalised weight, exp(−α d), α = 0.1", 11, "start", INK2)
    c.polyline([(ax.X(d / 20), ax.Y(math.exp(-alpha * d / 20))) for d in range(0, 201)], SERIES[0], 2.5)
    for d in (5, 10):
        v = math.exp(-alpha * d)
        c.dot(ax.X(d), ax.Y(v), SERIES[0], 4, title=f"d = {d}: {v:.2f}")
        c.text(ax.X(d) + (8 if d < 10 else -8), ax.Y(v) - 9, f"{v:.2f}", 10.5, "start" if d < 10 else "end", INK)
    c.save(p)


# ------------------------------------------------------------------ chapter 10
def fig_10_2():
    # Transport a tangent vector around the octant triangle of the unit sphere: A (equator, longitude 0) to the
    # north pole N, to B (equator, longitude 90 degrees), back to A along the equator.
    A, N, B = (1, 0, 0), (0, 0, 1), (0, 1, 0)
    v0 = (0, 0, 1)        # at A, pointing north, along the first leg
    vN = (-1, 0, 0)       # at N: still along the direction of travel of leg 1
    vB = (-1, 0, 0)       # leg 2 leaves N toward +y; the vector stays perpendicular to the leg; at B it points east
    v1 = (0, 1, 0)        # leg 3 runs west along the equator; the vector stays anti-parallel to it; back at A: east
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    assert dot(vN, (0, 1, 0)) == 0 and dot(vB, B) == 0 and dot(v1, A) == 0 and dot(v0, A) == 0
    angle = math.degrees(math.acos(dot(v0, v1)))
    K, area = 1.0, 4 * math.pi / 8       # unit sphere, one eighth of its surface
    assert abs(angle - 90) < 1e-9 and abs(math.degrees(K * area) - 90) < 1e-9
    assert 3 * 90 - 180 == 90            # angle excess of the triangle
    p = reg(P4 + "ch10_translation.md", "10.1",
            "Holonomy in its standard example. A tangent vector is carried by parallel transport around a triangle on "
            "a sphere with three right angles: from the equator to the pole, down a second meridian a quarter turn "
            "away, and back along the equator, and it returns rotated by 90 degrees. The rotation equals the curvature "
            "times the enclosed area, here (1/R²) × (π/2) R² = π/2, the constant-curvature case of the relation of "
            "Section 10.2.3; on a flat surface the same trip returns the vector unchanged (Corollary 10.1). The "
            "chapter posits that a round trip of translations behaves in the same way.",
            "## 10.3 The Cuneiform Case Study")
    c = Canvas(720, 420, "Carried around a closed loop, a vector comes back turned")
    cx, cy, R = 215, 232, 160
    norm = lambda a: tuple(x / math.sqrt(dot(a, a)) for x in a)
    cross = lambda a, b: (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
    fwd = norm((1, 1, 0.55))
    right = norm(cross((0, 0, 1), fwd))
    up = cross(fwd, right)
    S = lambda q: (cx + R * dot(q, right), cy - R * dot(q, up))
    _circle(c, cx, cy, R, INK3, 1.5, BOX, 0.35)
    arc = lambda f: [S(f(i / 60)) for i in range(61)]
    h = math.pi / 2
    eq = [S((math.cos(t), math.sin(t), 0)) for t in [(-0.75 + 2.0 * i / 80) * math.pi for i in range(81)]
          if dot((math.cos(t), math.sin(t), 0), fwd) > 0]
    c.polyline(eq, INK3, 1)
    legs = [arc(lambda s: (math.cos(h * s), 0, math.sin(h * s))),
            arc(lambda s: (0, math.sin(h * s), math.cos(h * s))),
            arc(lambda s: (math.sin(h * (1 - s)), math.cos(h * (1 - s)), 0))]
    c.add('<polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for leg in legs for x, y in leg)
          + f'" fill="{SERIES[0]}" fill-opacity="0.16"/>')
    for leg in legs:
        c.polyline(leg, SERIES[0], 2.5)
        (xa, ya), (xb, yb) = leg[30], leg[33]
        c.arrow(xa, ya, xb, yb, SERIES[0], 2)

    def vec(pt, v, col, width=2.5, ln=0.34):
        x1, y1 = S(pt)
        x2, y2 = S(tuple(a + ln * b for a, b in zip(pt, v)))
        c.arrow(x1, y1, x2, y2, col, width)

    s2 = math.sqrt(0.5)
    vec((s2, 0, s2), (-s2, 0, s2), INK2, 1.8, 0.26)          # mid leg 1: along the leg
    vec(N, vN, INK2, 1.8, 0.26)
    vec((0, s2, s2), (-1, 0, 0), INK2, 1.8, 0.26)            # mid leg 2: perpendicular to the leg
    vec(B, vB, INK2, 1.8, 0.26)
    vec((s2, s2, 0), (-s2, s2, 0), INK2, 1.8, 0.26)          # mid leg 3: anti-parallel to the leg
    vec(A, v0, SERIES[1], 3)
    vec(A, v1, CRITICAL, 3)
    for pt, lab, dx, dy, anc in [(A, "start and end", 18, -14, "start"), (N, "pole", 0, None, "middle"),
                                 (B, "", 0, 0, "middle")]:
        x, y = S(pt)
        c.dot(x, y, INK, 3.5)
        if lab:
            c.text(x + dx, cy - R - 9 if dy is None else y + dy, lab, 11, anc, INK2)
    x0 = 430
    legend(c, x0, 86, [("vector at the start", SERIES[1])], 11.5)
    legend(c, x0, 108, [("the same vector after the loop", CRITICAL)], 11.5)
    c.text(x0, 150, "three right angles: excess 3 × 90° − 180° = 90°", 11.5, "start", INK2)
    c.text(x0, 184, "curvature K = 1 / R²", 11.5, "start", INK2)
    c.text(x0, 204, "enclosed area = (π / 2) R²", 11.5, "start", INK2)
    c.text(x0, 224, "rotation = K × area = π / 2 = 90°", 11.5, "start", INK, "600")
    c.text(x0, 268, "flat surface: K = 0, rotation 0", 11.5, "start", INK2)
    c.text(x0, 310, "grey arrows: the vector on its way round", 11, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 11
def fig_11_3():
    p = reg(P5 + "ch11_cross_lingual.md", "11.1",
            "The architecture of Sections 11.2.3 and 11.2.4 as a block diagram. The encoder gives a 384-dimensional "
            "vector h; one head projects it to the 64-dimensional bond space, another to the 32-dimensional label "
            "space. The bond space feeds the Hohfeldian classifier and, through a gradient reversal layer, an "
            "adversary that tries to predict the period of the text; the reversal trains the bond space to make "
            "that prediction fail. The label space is trained to predict the period directly, as a control.",
            "### 11.2.5 The Experimental Protocol")
    c = Canvas(720, 400, "Bond space: trained to classify relations and to hide the period")
    c.box(16, 178, 84, 44, "input text")
    c.box(124, 178, 104, 44, "encoder", "h, 384 dims")
    c.box(262, 108, 118, 44, "bond space", "z_bond, 64 dims", stroke=SERIES[0])
    c.box(262, 258, 118, 44, "label space", "z_label, 32 dims", stroke=SERIES[1])
    c.box(430, 62, 152, 44, "Hohfeldian classifier", "four relations")
    c.box(430, 154, 110, 44, "gradient", "reversal", stroke=CRITICAL)
    c.box(566, 154, 138, 44, "period adversary", "gradients negated")
    c.box(430, 258, 152, 44, "period classifier", "no reversal")
    c.arrow(100, 200, 122, 200)
    c.arrow(228, 192, 260, 136)
    c.arrow(228, 208, 260, 274)
    c.arrow(380, 122, 428, 88)
    c.arrow(380, 138, 428, 172)
    c.arrow(540, 176, 564, 176)
    c.arrow(380, 280, 428, 280)
    c.text(592, 88, "loss L_Hohfeld", 11.5, "start", INK2)
    c.text(592, 284, "loss L_time", 11.5, "start", INK2)
    c.text(635, 218, "loss L_adv", 11.5, "middle", INK2)
    c.text(16, 350, "total loss = L_Hohfeld + L_time + L_adv, with the gradient of L_adv negated before the bond head",
           11.5, "start", INK2)
    c.text(16, 388, "block diagram of the text of Sections 11.2.3 and 11.2.4; no result is drawn", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 12
def fig_12_5():
    bins = [("Biblical", -1000, -500), ("Second Temple", -500, 70), ("Tannaitic", 70, 200), ("Amoraic", 200, 500),
            ("Geonic", 500, 1000), ("Rishonim", 1000, 1500), ("Achronim", 1500, 1800)]
    assert all(a[2] == b[1] for a, b in zip(bins[:-1], bins[1:])) and len(bins) == 7
    assert round(100 / len(bins), 1) == 14.3      # chance for the seven-bin probe
    train_end = 1000
    p = reg(P5 + "ch12_temporal_invariance.md", "12.1",
            "The design of the temporal protocol of Section 12.1.2. The Sefaria corpus is cut into seven periods; "
            "in the forward test the model is trained on the five periods up to 1000 CE and tested on the two "
            "later ones; the backward test swaps the roles. A fresh probe then tries to name the period from the "
            "bond space, and with seven periods its chance level is 14.3 percent. The time axis is in calendar "
            "years, so the widths show how unequal the periods are.",
            "### 12.1.3 Results: Temporal Invariance Confirmed")
    c = Canvas(720, 400, "Seven periods: train on the early ones, test on the late ones")
    X = lambda yr: 50 + 630 * (yr + 1000) / 2800
    yb, hb = 150, 34
    for i, (name, a, b) in enumerate(bins):
        col = SERIES[0] if b <= train_end else SERIES[1]
        c.add(f'<rect x="{X(a) + 1:.2f}" y="{yb}" width="{X(b) - X(a) - 2:.2f}" height="{hb}" rx="3" fill="{col}" '
              f'fill-opacity="0.8"><title>{name}: {a} to {b}</title></rect>')
        mid = (X(a) + X(b)) / 2
        if name == "Tannaitic":
            c.line(mid, yb - 4, mid, yb - 22, INK3, 1)
            c.text(mid, yb - 28, name, 11, "middle", INK)
        else:
            c.text(mid, yb - 10, name, 11, "middle", INK)
    ticks = [(-1000, "1000 BCE"), (-500, "500 BCE"), (70, "70 CE"), (200, "200"), (500, "500"), (1000, "1000"),
             (1500, "1500"), (1800, "1800 CE")]
    for i, (yr, lab) in enumerate(ticks):
        low = i % 2 == 1
        c.line(X(yr), yb + hb, X(yr), yb + hb + (20 if low else 6), INK3, 1)
        anc = "start" if i == 0 else ("end" if i == len(ticks) - 1 else "middle")
        c.text(X(yr), yb + hb + (34 if low else 20), lab, 10.5, anc, INK2)
    yt = 262
    for a, b, lab, col in [(-1000, 1000, "forward test: train on these five", SERIES[0]),
                           (1000, 1800, "test on these two", SERIES[1])]:
        c.line(X(a) + 3, yt, X(b) - 3, yt, col, 2.5)
        c.line(X(a) + 3, yt - 6, X(a) + 3, yt + 6, col, 2.5)
        c.line(X(b) - 3, yt - 6, X(b) - 3, yt + 6, col, 2.5)
        c.text((X(a) + X(b)) / 2, yt + 22, lab, 11.5, "middle", INK)
    c.text(50, 326, "backward test: train on the two late periods, test on the five early ones", 11.5, "start", INK2)
    c.text(50, 348, "temporal probe on the bond space: seven periods, chance 1/7 = 14.3%", 11.5, "start", INK2)
    c.text(16, 390, "period boundaries as listed in Section 12.1.2", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_12_2():
    p = reg(P5 + "ch12_temporal_invariance.md", "12.2",
            "The extraction pipeline of Section 12.2 as a flow. Corpus text passes through a loader for its corpus "
            "and a common preprocessing step; Stage 1 assigns a Hohfeldian label by matching deontic vocabulary; a "
            "passage that matches no pattern is labelled NONE and left out. Stage 2 checks a subset with four "
            "language models and keeps a label when at least three agree with mean confidence above 0.7. The labels "
            "therefore rest first on keyword patterns, of which two English examples are shown.",
            "## 12.3 Linguistic Analysis: Surface Coordinates on the Moral Manifold")
    c = Canvas(720, 400, "Labels come from keyword patterns, then a four-model check")
    y, h, w = 150, 52, 118
    xs = [16, 156, 296, 436, 576]
    labs = [("corpus text", None), ("corpus loader", "one per corpus"), ("preprocessing", "common to all"),
            ("Stage 1", "pattern matching"), ("labelled", "passages")]
    for x, (a, b) in zip(xs, labs):
        c.box(x, y, w, h, a, b, stroke=SERIES[0] if a == "Stage 1" else BORDER)
    for x in xs[:-1]:
        c.arrow(x + w, y + h / 2, x + w + 20, y + h / 2)
    c.box(446, 58, 258, 52, "Stage 2, on a subset: four models",
          "keep if ≥ 3 agree, mean confidence > 0.7", stroke=SERIES[1])
    c.arrow(655, y, 655, 112)
    c.arrow(615, 110, 615, y - 2)
    c.box(420, 250, 150, 44, "no pattern: NONE", "left out of training", stroke=CRITICAL)
    c.arrow(495, y + h, 495, 248)
    c.text(16, 258, "English patterns (Section 12.2.4)", 11.5, "start", INK, "600")
    c.text(16, 280, "OBLIGATION:  must | shall | duty | required | obligated", 11, "start", INK2)
    c.text(16, 298, "RIGHT:  right to | entitled | deserve | owed", 11, "start", INK2)
    c.text(16, 316, "LIBERTY:  may | can | permitted | allowed | free to", 11, "start", INK2)
    c.text(16, 334, "NO-RIGHT:  no right | cannot demand | not entitled", 11, "start", INK2)
    c.text(16, 388, "flow of Section 12.2; Hebrew, Classical Chinese and Arabic have their own pattern lists", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 13
def fig_13_4():
    H = "OCLN"
    s = {"O": "C", "C": "O", "L": "N", "N": "L"}      # correlative exchange (Definition 13.7)
    n = {"O": "L", "L": "O", "C": "N", "N": "C"}      # negation (Definition 13.7)
    e = {x: x for x in H}
    comp = lambda f, g: {x: f[g[x]] for x in H}
    sn = comp(s, n)
    G = {"e": e, "s": s, "n": n, "sn": sn}
    assert comp(s, n) == comp(n, s)                               # the two involutions commute
    assert all(comp(g, g) == e for g in G.values())                # every element is its own inverse
    name = lambda f: next(k for k, g in G.items() if g == f)
    table = {(a, b): name(comp(G[a], G[b])) for a in G for b in G}   # closed: four elements, the Klein four-group
    assert sn == {"O": "N", "N": "O", "C": "L", "L": "C"}
    p = reg(P5 + "ch13_gauge_theory.md", "13.1",
            "The Hohfeldian square of Definition 13.7 with the two operations the chapter posits. The correlative "
            "exchange s runs along the horizontal edges (Duty with Claim, Liberty with No-Claim) and the negation n "
            "along the vertical ones (Duty with Liberty, Claim with No-Claim); their product sn joins the diagonals. "
            "The table is the multiplication of the four elements, computed from the definition: every element is "
            "its own inverse and the order of two operations does not matter. This is the Klein four-group, with "
            "no quarter-turn, and the semantic gates of Section 13.4 are triggers for n.",
            "### 13.3.2 The Dihedral Group $D_4$ (Withdrawn) (Withdrawn)")
    c = Canvas(720, 400, "Two commuting operations on four positions: the group V4")
    pos = {"O": (250, 120), "C": (450, 120), "L": (250, 300), "N": (450, 300)}
    full = {"O": "Duty", "C": "Claim", "L": "Liberty", "N": "No-Claim"}
    for a, b in (("O", "N"), ("C", "L")):
        c.line(*pos[a], *pos[b], SERIES[2], 1.5, dash="5 5")
    c.text(350, 190, "sn", 12, "middle", INK, italic=True)
    for a, b in (("O", "C"), ("L", "N")):
        c.line(*pos[a], *pos[b], SERIES[0], 3)
        c.text(350, pos[a][1] - 10, "s", 13, "middle", INK, "600", italic=True)
    for a, b in (("O", "L"), ("C", "N")):
        c.line(*pos[a], *pos[b], SERIES[1], 3)
        c.text(pos[a][0] + (-12 if a == "O" else 12), 214, "n", 13, "end" if a == "O" else "start", INK, "600",
               italic=True)
    for k, (x, y) in pos.items():
        _circle(c, x, y, 24, INK2, 1.5, BOX, 1.0)
        c.text(x, y + 6, k, 17, "middle", INK, "600")
        c.text(x, y + (-34 if k in "OC" else 46), full[k], 12, "middle", INK)
    c.text(350, 62, "s: correlative exchange, a change of perspective", 11.5, "middle", INK2)
    c.text(350, 372, "n: negation, a change of state that needs a trigger", 11.5, "middle", INK2)
    c.text(214, 178, "gates on n (Section 13.4.1)", 11, "end", INK, "600")
    c.text(214, 198, "\"I promise\": L to O", 11, "end", INK2)
    c.text(214, 216, "\"only if convenient\": O to L", 11, "end", INK2)
    x0, y0, cw = 536, 150, 36
    els = list(G)
    c.text(x0 + 2.5 * cw, y0 - 30, "multiplication table", 11.5, "middle", INK, "600")
    for i, a in enumerate(els):
        c.text(x0 + cw * (i + 1.5), y0 - 6, a, 12, "middle", INK, "600", italic=True)
        c.text(x0 + cw * 0.5, y0 + cw * (i + 1) - 12, a, 12, "middle", INK, "600", italic=True)
        for j, b in enumerate(els):
            c.text(x0 + cw * (j + 1.5), y0 + cw * (i + 1) - 12, table[(a, b)], 12, "middle", INK2, italic=True)
    c.line(x0 + cw, y0 - 20, x0 + cw, y0 + 4 * cw, GRID, 1)
    c.line(x0, y0 + 2, x0 + 5 * cw, y0 + 2, GRID, 1)
    c.text(x0 + 2.5 * cw, y0 + 4 * cw + 24, "symmetric: s n = n s", 11, "middle", INK2, italic=True)
    c.save(p)


def fig_13_5():
    liberty = [0, 0, 0, 0, 0, 100, 0, 55, 100, 100, 100]     # Section 13.4.2, percent Liberty at levels 0 to 10
    assert len(liberty) == 11 and liberty[4] == 0 and liberty[5] == 100 and liberty[6] == 0
    assert sum(1 for v in liberty if v not in (0, 100)) == 1
    p = reg(P5 + "ch13_gauge_theory.md", "13.2",
            "The Protocol 1 result as the chapter reports it in Section 13.4.2: the percentage of Liberty judgments "
            "at each of the eleven levels of contextual modification. Levels 0 to 4 give no Liberty judgments, the "
            "phrase \"only if convenient\" at level 5 gives all Liberty, \"found a friend\" at level 6 returns to "
            "none, and levels 8 to 10 give all Liberty. The chapter reads the jump between levels 4 and 5 as a "
            "discrete gate. Level 7, at 55 percent, is the one level that is neither, and the chapter calls its "
            "trigger ambiguous.",
            "### 13.4.3 Phase Transitions and Gate Reliability")
    c = Canvas(720, 400, "Liberty judgments switch on and off between levels (as reported)")
    ax = Axes(c, 70, 52, 620, 270, (0, 11), (0, 135), [], [0, 25, 50, 75, 100], "level of contextual modification",
              "judged Liberty (%)")
    slot = ax.w / 11
    notes = {5: ["\"only if convenient\""], 6: ["\"found a friend\""], 7: ["\"don't worry", "if busy\""]}
    for i, v in enumerate(liberty):
        x = ax.x0 + slot * (i + 0.5)
        col = CRITICAL if v not in (0, 100) else SERIES[0]
        c.rect(x - 12, ax.Y(v), 24, ax.Y(0) - ax.Y(v), col, title=f"level {i}: {v}% Liberty")
        c.text(x, ax.Y(v) - 6, str(v), 11, "middle", INK)
        c.text(x, ax.y0 + ax.h + 16, str(i), 11, "middle", INK2)
        for k, line in enumerate(reversed(notes.get(i, []))):
            c.text(x, ax.Y(v) - 22 - 13 * k, line, 10.5, "middle", INK2, italic=True)
    c.text(ax.x0 + slot * 2.5, ax.Y(22), "levels 0 to 4: weak modifications", 10.5, "middle", INK2, italic=True)
    c.text(ax.x0 + slot * 9.5, ax.Y(122), "levels 8 to 10: explicit releases", 10.5, "middle", INK2, italic=True)
    c.text(16, 390, "values as printed in Section 13.4.2 (SQND Protocol 1)", 10.5, "start", INK3, italic=True)
    c.save(p)


def fig_13_2():
    rows = [("journalist", 0.659, True), ("teacher", 0.862, True), ("consultant", 0.9996, False),
            ("doctor", 1.000, False), ("lawyer", 0.993, False), ("executive", 0.995, False),
            ("researcher", 0.987, False), ("friend", 0.962, False)]
    assert len(rows) == 8 and sum(1 for r in rows if r[2]) == 2
    assert max(v for _, v, x in rows if x) < min(v for _, v, x in rows if not x)   # the two cross-type are lowest
    p = reg(P5 + "ch13_gauge_theory.md", "13.3",
            "The Protocol 2 estimates of Section 13.5.3. For each of eight scenarios the same facts were presented "
            "in two orders, and the estimate W-hat is the overlap (Bhattacharyya coefficient) of the two "
            "distributions of judgments: 1 when the order makes no difference, lower as the two orders diverge. "
            "The two scenarios the chapter classes as cross-type, journalist and teacher, are the two with the "
            "lowest overlap and the two the chapter reports as significant; the other six lie between 0.96 and 1. "
            "The figure shows the estimates only; the earlier explanation of the pattern is withdrawn.",
            "### 13.5.4 Holonomy as Communicative Path Dependence")
    c = Canvas(720, 400, "Order of presentation matters in two of eight scenarios (reported)")
    ax = Axes(c, 150, 60, 480, 34 * len(rows), (0.6, 1.0), (0, len(rows)), [0.6, 0.7, 0.8, 0.9, 1.0], [],
              "W-hat: overlap of the judgments under the two orders", "")
    for v in (0.7, 0.8, 0.9):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    c.line(ax.X(1), ax.y0 - 4, ax.X(1), ax.y0 + ax.h, INK3, 1.5, dash="4 4")
    for i, (name, v, cross) in enumerate(rows):
        y = ax.y0 + 34 * (i + 0.5)
        c.text(ax.x0 - 12, y + 4, name, 11.5, "end", INK2)
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        col = CRITICAL if cross else SERIES[0]
        if cross:
            c.line(ax.X(v), y, ax.X(1), y, col, 2)
        c.dot(ax.X(v), y, col, 5.5, title=f"{name}: {v}")
        lab = f"{v:.4f}" if name == "consultant" else f"{v:.3f}"
        if cross:
            c.text(ax.X(v) - 12, y + 4, lab, 11, "end", INK)
        else:
            c.text(ax.X(1) + 12, y + 4, lab, 11, "start", INK)
    legend(c, 150, 42, [("cross-type (Definition 13.14)", CRITICAL), ("within-type", SERIES[0])], 11)
    c.text(ax.X(1) - 6, 50, "1 = no order effect", 10.5, "end", INK2, italic=True)
    c.text(16, 390, "W-hat = sum over positions of the square root of P(order 1) × P(order 2); table of Section 13.5.3",
           10.5, "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 14
def _wilson(k, n, z=1.959964):
    ph = k / n
    den = 1 + z * z / n
    mid = (ph + z * z / (2 * n)) / den
    half = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return 100 * (mid - half), 100 * (mid + half)


def fig_14_3():
    rows = [("Claude Sonnet 4.6", 59, 0, (0, 30), 0.588), ("Gemini 2.0 Flash", 71, 3, (12, 65), 0.377),
            ("Gemini 2.5 Pro", 68, 4, (19, 73), 0.238), ("Gemini 2.5 Flash", 76, 5, (27, 81), 0.206)]
    n = 9
    wrong = []
    for name, cf, k, ci, gap in rows:
        lo, hi = _wilson(k, n)
        assert round(lo) == ci[0] and round(hi) == ci[1], (name, lo, hi)     # the printed Wilson intervals
        assert abs((cf - 100 * k / n) / 100 - gap) < 0.012                    # gap = correct flip - wrong flip
        wrong.append(round(100 * k / n))
    assert wrong == [0, 33, 44, 56] and wrong == sorted(wrong)
    p = reg(P6 + "ch14_failure_modes.md", "14.1",
            "The table of Section 14.3.2 as the chapter reports it. For each model the left-hand mark is the rate "
            "at which it changed its verdict after an invalid correction and the right-hand mark the rate after a "
            "valid one; the distance between them is the discrimination gap. The bar through each wrong-flip mark "
            "is its Wilson 95 percent interval, recomputed here from the counts (0, 3, 4 and 5 of 9 items) and in "
            "agreement with the printed intervals. The intervals are wide and overlap, since each rests on nine "
            "items.",
            "### 14.3.3 Sycophancy Is a Discrimination Failure, Not a Revision Failure")
    c = Canvas(720, 400, "Wrong flips rise from 0 to 56 percent over four models (reported)")
    ax = Axes(c, 160, 66, 420, 58 * len(rows), (0, 100), (0, len(rows)), [0, 25, 50, 75, 100], [],
              "verdict changed after the correction (% of items)", "")
    for v in (25, 50, 75, 100):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    for i, (name, cf, k, ci, gap) in enumerate(rows):
        y = ax.y0 + 58 * (i + 0.5)
        lo, hi = _wilson(k, n)
        wf = 100 * k / n
        c.text(ax.x0 - 12, y + 4, name, 11.5, "end", INK2)
        c.line(ax.X(lo), y + 9, ax.X(hi), y + 9, SERIES[1], 1.5, opacity=0.8)
        for v in (lo, hi):
            c.line(ax.X(v), y + 5, ax.X(v), y + 13, SERIES[1], 1.5, opacity=0.8)
        c.line(ax.X(wf), y - 9, ax.X(cf), y - 9, INK3, 1.5)
        c.dot(ax.X(wf), y - 9, SERIES[1], 5.5, title=f"{name}: wrong flip {wf:.0f}% ({k}/{n})")
        c.dot(ax.X(cf), y - 9, SERIES[0], 5.5, title=f"{name}: correct flip {cf}%")
        c.text(ax.X(wf), y - 20, f"{wf:.0f}", 10.5, "middle", INK)
        c.text(ax.X(cf), y - 20, f"{cf}", 10.5, "middle", INK)
        c.text(ax.x0 + ax.w + 14, y - 5, f"gap +{gap:.3f}", 11, "start", INK)
    legend(c, 160, 42, [("wrong flip (invalid correction), 95% interval", SERIES[1]),
                        ("correct flip (valid correction)", SERIES[0])], 11)
    c.text(16, 390, "nine wrong-correction items per model; intervals recomputed from the counts", 10.5, "start", INK3,
           italic=True)
    c.save(p)


def fig_14_8():
    rows = [("Claude Sonnet 4.6", 4.2, 4.3, 5, 14, 36), ("Gemini 2.0 Flash", 3.2, 3.7, 1, 7, 14),
            ("Gemini 3 Flash", 1.1, 2.9, 2, 6, 33), ("Gemini 2.5 Flash", 1.7, 2.3, 5, 10, 50),
            ("Gemini 2.5 Pro", 1.0, 0.9, 1, 3, 33)]
    for name, s1, s2, k, m, pct in rows:
        assert round(100 * k / m) == pct
    mean_rate = sum(r[5] for r in rows) / len(rows)
    stouffer = sum(r[1] for r in rows) / math.sqrt(len(rows))
    assert round(mean_rate) == 33 and round(stouffer, 1) == 5.0
    assert sum(1 for r in rows if r[2] >= r[1]) == 4      # the warned value is not smaller in four of five models
    p = reg(P6 + "ch14_failure_modes.md", "14.2",
            "The per-model table of Section 14.5.2 as the chapter reports it. Left: the size of the displacement "
            "caused by a vivid distractor, in standard deviations, and the value the table gives for the warned "
            "condition, which is not smaller in four of the five models. Right: the share of displaced verdicts that the "
            "warning restored, with the counts; the five shares average 33 percent, the chapter's recovery ceiling, "
            "on counts of 3 to 14 verdicts per model. The five displacement values combine to 5.0 by Stouffer's "
            "method (their sum divided by the square root of 5), the combined figure the chapter prints.",
            "### 14.5.4 Why Gauge Invariance Is Fragile")
    c = Canvas(720, 400, "A warning restores about a third of displaced verdicts (as reported)")
    rh = 46
    ax = Axes(c, 150, 76, 230, rh * len(rows), (0, 5), (0, len(rows)), [0, 1, 2, 3, 4, 5], [],
              "displacement (standard deviations)", "")
    bx = Axes(c, 450, 76, 220, rh * len(rows), (0, 100), (0, len(rows)), [0, 25, 50, 75, 100], [],
              "displaced verdicts restored (%)", "")
    for v in (1, 2, 3, 4, 5):
        c.line(ax.X(v), ax.y0, ax.X(v), ax.y0 + ax.h, GRID, 1)
    for v in (25, 50, 75, 100):
        c.line(bx.X(v), bx.y0, bx.X(v), bx.y0 + bx.h, GRID, 1)
    c.line(bx.X(mean_rate), bx.y0 - 4, bx.X(mean_rate), bx.y0 + bx.h, INK3, 1.5, dash="4 4")
    c.text(bx.X(mean_rate) + 5, bx.y0 - 8, "mean 33%", 10.5, "start", INK2, italic=True)
    for i, (name, s1, s2, k, m, pct) in enumerate(rows):
        y = ax.y0 + rh * (i + 0.5)
        c.text(ax.x0 - 12, y + 4, name, 11.5, "end", INK2)
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        c.line(ax.X(s1), y, ax.X(s2), y, INK3, 2)
        c.dot(ax.X(s1), y, SERIES[0], 5.5, title=f"{name}: distractor {s1} sigma")
        c.dot(ax.X(s2), y, SERIES[1], 5.5, title=f"{name}: warned {s2} sigma")
        lo, hi = min(s1, s2), max(s1, s2)
        c.text(ax.X(lo) - 10, y + 4, f"{lo:.1f}", 10.5, "end", INK)
        c.text(ax.X(hi) + 10, y + 4, f"{hi:.1f}", 10.5, "start", INK)
        c.hrect(bx.x0, y - 9, bx.X(pct) - bx.x0, 18, SERIES[2], title=f"{name}: {k}/{m} restored")
        c.text(bx.X(57), y + 4, f"{k}/{m} = {pct}%", 10.5, "start", INK)
    legend(c, 150, 44, [("distractor", SERIES[0]), ("after warning", SERIES[1])], 11)
    legend(c, 450, 44, [("restored by the warning", SERIES[2])], 11)
    c.text(16, 390, "(4.2 + 3.2 + 1.1 + 1.7 + 1.0) / √5 = 5.0;  mean of 36, 14, 33, 50, 33 = 33", 10.5, "start", INK3,
           italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 15
def fig_15_2():
    prof = {"A: uniformly mediocre": (0.35, 0.35, 0.35, 0.35),
            "B: right words, wrong phrases": (0.70, 0.40, 0.30, 0.18),
            "C: fluent locally, incoherent": (0.60, 0.50, 0.25, 0.20)}
    gm = {k: math.exp(sum(math.log(x) for x in v) / 4) for k, v in prof.items()}
    assert all(round(g, 2) == 0.35 for g in gm.values()), gm
    p = reg(P6 + "ch15_scalar_irrecoverability.md", "15.1",
            "Three of the quality profiles of Section 15.2.1, with the n-gram precisions the chapter gives; the "
            "bars are the precisions for word sequences of length 1 to 4. BLEU without a brevity penalty is their "
            "geometric mean, and for all three profiles it is 0.35 (0.350, 0.351 and 0.350). The score is the "
            "dashed line; the shape of the bars, which is what tells the three systems apart, is what the score "
            "leaves out. Profile D is described in words only and is not drawn.",
            "### 15.2.2 The Quality Tensor")
    grouped_bars(p, "Three different translation systems, one BLEU score of 0.35",
                 ["1-gram", "2-gram", "3-gram", "4-gram"], [(k, list(v)) for k, v in prof.items()],
                 ylabel="n-gram precision", ylim=(0, 0.8), yticks=[0, 0.2, 0.4, 0.6, 0.8], refline=0.35,
                 note="dashed: the geometric mean of each profile, 0.35; precisions as given in Section 15.2.1, no "
                      "brevity penalty")


# ------------------------------------------------------------------ chapter 16
def fig_16_7():
    p = reg(P7 + "ch16_rosetta.md", "16.1",
            "The Rosetta trajectory as the chapter lays it out: four stations and the three levels of structure it "
            "posits. Each station is placed at the highest level the chapter says it adds. Whale codas and birdsong "
            "are studied through signal geometry alone, cuneiform adds the hierarchy of the sign taxonomy, and "
            "cross-lingual moral reasoning adds the semantic level. Each level needs more data than the one below "
            "it, and the bottom row gives the state of the meaning at each station; this is a diagram of the argument, "
            "not a measurement.",
            "### 16.6.3 The Subsumption Is Not Merely Logical")
    c = Canvas(720, 420, "Four stations, three posited levels of structure")
    levels = [("Level 3: semantic geometry", "needs parallel corpora", 60),
              ("Level 2: hierarchical geometry", "needs a taxonomy", 150),
              ("Level 1: signal geometry", "needs only the signal", 240)]
    for name, need, y in levels:
        c.line(16, y + 82, 704, y + 82, GRID, 1)
        c.text(16, y + 34, name, 11.5, "start", INK, "600")
        c.text(16, y + 52, need, 11, "start", INK2)
    stations = [("Station 1", "whale codas", 2, ["meaning", "opaque"]),
                ("Station 2", "birdsong", 2, ["meaning known:", "species identity"]),
                ("Station 3", "cuneiform", 1, ["partly", "decoded"]),
                ("Station 4", "moral reasoning", 0, ["invariant structure", "posited (V4)"])]
    bw, bh = 112, 50
    centres = []
    for i, (st, what, lev, meaning) in enumerate(stations):
        x = 222 + 124 * i
        y = levels[lev][2] + 16
        c.box(x, y, bw, bh, st, what, stroke=SERIES[i])
        centres.append((x, y))
        for k, line in enumerate(meaning):
            c.text(x + bw / 2, 352 + 16 * k, line, 11, "middle", INK2)
    for (x1, y1), (x2, y2) in zip(centres[:-1], centres[1:]):
        if y1 == y2:
            c.arrow(x1 + bw, y1 + bh / 2, x2 - 2, y2 + bh / 2, INK2, 1.5)
        else:
            c.arrow(x1 + bw - 20, y1, x2 + 20, y2 + bh + 2, INK2, 1.5)
    c.text(16, 358, "state of the meaning", 11.5, "start", INK, "600")
    c.text(16, 410, "levels and their data requirements from Section 16.6.1; stations from Sections 16.2 to 16.5", 10.5,
           "start", INK3, italic=True)
    c.save(p)


# ------------------------------------------------------------------ chapter 18
def fig_18_1():
    rows = [("S  signal", [("coda intervals", 9), ("birdsong bands", 16), ("birdsong topology", 2)]),
            ("C  content", [("coda features", 5), ("sign hierarchy", 3)]),
            ("P  pragmatics", [("framing", 2), ("sycophancy", 1)])]
    best = [max(v for _, v in items) for _, items in rows]
    assert best == [16, 5, 2] and sum(best) == 23      # "The total lower bound on dim(M) is at least 23"
    p = reg(P7 + "ch18_open_questions.md", "18.1",
            "The lower bounds of Section 18.5.1 on the dimension of each factor of the communication manifold, one "
            "mark per analysis. The chapter takes the largest bound on each factor (ringed) and adds them: 16 for "
            "the signal, 5 for the content and 2 for the pragmatics, a total of at least 23. These are counts of "
            "features the book's analyses used, posited as independent, and not estimates of the true dimension. "
            "The table's row for the Hohfeldian relations is left out because the book counts it in two ways; it "
            "does not change the total.",
            "### 18.5.2 Why the True Dimension Matters")
    c = Canvas(720, 400, "Lower bounds add up to at least 23 dimensions (the chapter's count)")
    ax = Axes(c, 150, 70, 520, 78 * len(rows), (0, 18), (0, len(rows)), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], [],
              "lower bound on the number of independent dimensions", "")
    for i, (name, items) in enumerate(rows):
        y = ax.y0 + 78 * (i + 0.5)
        c.text(ax.x0 - 14, y + 4, name, 12, "end", INK, "600")
        c.line(ax.x0, y, ax.x0 + ax.w, y, GRID, 1)
        for k, (lab, v) in enumerate(sorted(items, key=lambda t: t[1])):
            top = v == best[i]
            if top:
                _circle(c, ax.X(v), y, 11, CRITICAL, 2)
            c.dot(ax.X(v), y, SERIES[i], 5.5, title=f"{lab}: {v}")
            up = (k % 2 == 1) or len(items) == 3
            c.text(ax.X(v), y + (-18 if up else 28), f"{lab}: {v}", 11, "middle", INK if top else INK2)
    c.text(16, 366, "16 (signal) + 5 (content) + 2 (pragmatics) = 23", 12, "start", INK, "600")
    c.text(16, 390, "bounds as listed in Section 18.5.1; ringed: the largest for each factor", 10.5, "start", INK3,
           italic=True)
    c.save(p)
