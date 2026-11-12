# Direct-teaching Board 2 for Grade 9 Topic 7 "Perimeter, Area and Volume" (7 meetings).
# Run: python3 .claude/skills/directteach/examples/g09_t07_perimeter_area_volume.py <repo>
# Every numerical answer below was checked by computation before publishing.
import os, sys
REPO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else '.')
sys.path.insert(0, os.path.join(REPO, '.claude/skills/directteach/engine'))
from directteach import Board, S

b = Board('Board 2 - Perimeter, Area and Volume (Direct Teaching)',
          ['Overview', 'Perimeter & area', 'Trapeziums & composites', 'Circles', '3D objects & nets', 'Surface area', 'Volume', 'Spheres & test'])
yd = Board.youdo

# ---------- small SVG figures (labels in the figure, units in cm unless stated) ----------
L = 'font-size="13" font-weight="bold" text-anchor="middle"'
SVG_PARA = r"""<svg viewBox="0 0 330 120" style="width: 300px; height: 110px; flex-shrink: 0;"><polygon points="20,100 140,100 170,20 50,20" fill="#ebf8ff" stroke="#2d3748" stroke-width="2"/><polygon points="20,100 50,100 50,20" fill="#fed7d7" stroke="#c53030" stroke-width="1.5" stroke-dasharray="4,3"/><text x="160" y="65" font-size="22" fill="#718096">→</text><polygon points="190,100 280,100 280,20 190,20" fill="#ebf8ff" stroke="#2d3748" stroke-width="2"/><polygon points="280,100 310,100 310,20 280,20" fill="#fed7d7" stroke="#c53030" stroke-width="1.5"/><text x="80" y="116" """ + L + r""" fill="#1a365d">base b</text><line x1="50" y1="20" x2="50" y2="100" stroke="#c53030" stroke-width="1.5"/><text x="62" y="65" font-size="12" fill="#c53030" font-weight="bold">h</text><text x="250" y="116" """ + L + r""" fill="#1a365d">b × h</text></svg>"""
SVG_TRAP = r"""<svg viewBox="0 0 230 120" style="width: 210px; height: 110px; flex-shrink: 0;"><polygon points="15,100 215,100 160,20 60,20" fill="#ebf8ff" stroke="#2d3748" stroke-width="2"/><line x1="60" y1="20" x2="215" y2="100" stroke="#805ad5" stroke-width="2" stroke-dasharray="5,3"/><line x1="60" y1="20" x2="60" y2="100" stroke="#c53030" stroke-width="1.5" stroke-dasharray="3,3"/><text x="110" y="14" """ + L + r""" fill="#1a365d">a</text><text x="115" y="116" """ + L + r""" fill="#1a365d">b</text><text x="70" y="70" font-size="13" fill="#c53030" font-weight="bold">h</text></svg>"""
SVG_L = r"""<svg viewBox="0 0 260 200" style="width: 230px; height: 177px; flex-shrink: 0;"><polygon points="20,180 236,180 236,108 146,108 146,18 20,18" fill="#fefcbf" stroke="#2d3748" stroke-width="2"/><polygon points="146,18 236,18 236,108 146,108" fill="none" stroke="#a0aec0" stroke-dasharray="5,4"/><line class="step" x1="20" y1="108" x2="146" y2="108" stroke="#805ad5" stroke-width="2" stroke-dasharray="6,4"/><text x="128" y="196" """ + L + r""">12 m</text><text x="10" y="104" """ + L + r""">9</text><text x="83" y="13" """ + L + r""">7 m</text><text x="191" y="13" """ + L + r""" fill="#a0aec0">5 m</text><text x="250" y="148" """ + L + r""">5</text><text x="250" y="68" """ + L + r""" fill="#a0aec0">4</text></svg>"""
SVG_SECTOR = r"""<svg viewBox="0 0 150 130" style="width: 150px; height: 130px; flex-shrink: 0;"><circle cx="40" cy="105" r="95" fill="none" stroke="#cbd5e0" stroke-dasharray="4,4"/><path d="M40,105 L135,105 A95,95 0 0 0 69.4,14.6 Z" fill="#e9d8fd" stroke="#805ad5" stroke-width="2"/><text x="62" y="98" font-size="12" fill="#805ad5" font-weight="bold">72°</text><text x="88" y="121" """ + L + r""">r = 10</text></svg>"""
SVG_NETBOX = r"""<svg viewBox="0 0 300 170" style="width: 280px; height: 159px; flex-shrink: 0;"><g fill="#ebf8ff" stroke="#2d3748" stroke-width="1.5"><rect x="60" y="40" width="100" height="60"/><rect x="60" y="0" width="100" height="40"/><rect x="60" y="100" width="100" height="40"/><rect x="20" y="40" width="40" height="60"/><rect x="160" y="40" width="40" height="60"/><rect x="200" y="40" width="100" height="60"/></g><text x="110" y="75" """ + L + r""">5 × 3</text><text x="250" y="75" """ + L + r""">5 × 3</text><text x="110" y="25" font-size="11" text-anchor="middle">5 × 2</text><text x="110" y="125" font-size="11" text-anchor="middle">5 × 2</text><text x="40" y="75" font-size="11" text-anchor="middle">3×2</text><text x="180" y="75" font-size="11" text-anchor="middle">3×2</text><text x="150" y="160" font-size="12" fill="#4a5568" text-anchor="middle">cuboid 5 cm × 3 cm × 2 cm</text></svg>"""
SVG_CYLNET = r"""<svg viewBox="0 0 280 150" style="width: 260px; height: 140px; flex-shrink: 0;"><rect x="40" y="30" width="200" height="80" fill="#c6f6d5" stroke="#2d3748" stroke-width="1.5"/><circle cx="140" cy="15" r="15" fill="#c6f6d5" stroke="#2d3748" stroke-width="1.5"/><circle cx="140" cy="125" r="15" fill="#c6f6d5" stroke="#2d3748" stroke-width="1.5"/><text x="140" y="75" """ + L + r""">2πr × h</text><text x="20" y="75" """ + L + r""">h</text><line x1="140" y1="125" x2="155" y2="125" stroke="#c53030" stroke-width="1.5"/><text x="160" y="130" font-size="12" fill="#c53030" font-weight="bold">r</text></svg>"""
SVG_RICE = r"""<svg viewBox="0 0 270 120" style="width: 245px; height: 109px; flex-shrink: 0;"><polygon points="20,110 90,110 90,30 20,30" fill="#ebf8ff" stroke="#2d3748" stroke-width="2"/><polygon points="140,110 210,110 175,30" fill="#fefcbf" stroke="#2d3748" stroke-width="2"/><text x="55" y="75" """ + L + r""">prism</text><text x="175" y="102" font-size="11" font-weight="bold" text-anchor="middle">pyramid</text><text x="222" y="72" font-size="18" fill="#805ad5" font-weight="bold">× 3</text></svg>"""
SVG_ORANGE = r"""<svg viewBox="0 0 300 92" style="width: 270px; height: 83px; flex-shrink: 0;"><circle cx="40" cy="42" r="35" fill="#fbd38d" stroke="#c05621" stroke-width="2"/><text x="90" y="49" font-size="22" fill="#718096">→</text><g fill="#feebc8" stroke="#c05621" stroke-width="1.5"><circle cx="135" cy="42" r="19"/><circle cx="177" cy="42" r="19"/><circle cx="219" cy="42" r="19"/><circle cx="261" cy="42" r="19"/></g><text x="198" y="86" font-size="11" text-anchor="middle" fill="#4a5568">peel = 4 circles, radius r</text></svg>"""

# ---------- overview ----------
b.title('Perimeter, Area &amp; Volume', 'Grade 9 Mathematics — Topic 7 · Board 2: Direct Teaching')
b.raw(0, '🗺️ Chapter Roadmap &amp; Success Criteria', r"""                        <table class="tbl">
                            <tr><th>Meeting</th><th>Topic</th><th>Key formula</th></tr>
                            <tr><td>1 (7.1)</td><td>Perimeter &amp; basic area</td><td>$A = lw$ · $A = bh$ · $A = \frac12 bh$</td></tr>
                            <tr><td>2 (7.1)</td><td>Trapeziums &amp; composites</td><td>$A = \frac12(a + b)h$</td></tr>
                            <tr><td>3 (7.1)</td><td>Circles, arcs &amp; sectors</td><td>$C = 2\pi r$ · $A = \pi r^2$ · $\frac{\theta}{360}$</td></tr>
                            <tr><td>4 (7.2)</td><td>3D objects &amp; nets</td><td>faces · edges · vertices</td></tr>
                            <tr><td>5 (7.3)</td><td>Surface area</td><td>add up the net</td></tr>
                            <tr><td>6 (7.3)</td><td>Volume</td><td>$V = Ah$ · $V = \frac13 Ah$</td></tr>
                            <tr><td>7 (7.3)</td><td>Spheres &amp; Chapter 7 Test</td><td>$4\pi r^2$ · $\frac43\pi r^3$</td></tr>
                        </table>
                        <div class="content-box mini"><h3><span class="badge bg-exit">WILT</span> I can…</h3><p>① tell perimeter (cm), area (cm²) and volume (cm³) apart ② find composite areas by splitting or subtracting ③ use $\pi$ for circles, arcs and sectors ④ draw nets and find surface areas ⑤ find volumes of prisms, cylinders, pyramids, cones and spheres.</p></div>""")

# ================= MEETING 1 =================
b.slide(1, 'lec', 'Fence or Fertiliser?', r"""                        <div class="content-box"><h3><span class="badge bg-hook">Hook</span> 🌾</h3><p>A farmer puts a <strong>fence</strong> around a sawah and spreads <strong>fertiliser</strong> on the soil inside. Which is perimeter? Which is area?</p></div>
                        <div class="rule step"><h3>Perimeter (1D) vs Area (2D)</h3><p><strong>Perimeter</strong> = distance <em>around</em> the shape → cm, m</p><p><strong>Area</strong> = space <em>inside</em> the shape → cm², m²</p></div>
                        <div class="rule green step"><h3>Rectangle</h3><p style="text-align: center; font-size: 1.2em;">$P = 2(l + w)$ &nbsp;&nbsp;&nbsp; $A = l \times w$</p></div>""", 'Units: cm, cm²')
b.slide(1, 'lec', 'Parallelogram &amp; Triangle', r"""                        <div class="content-box"><p>❓ We only know $A = l \times w$. How can we <strong>prove</strong> the area of a parallelogram and a triangle?</p></div>
                        <div class="rule purple step" style="display: flex; gap: 10px; align-items: center;"><div><h3>Parallelogram</h3><p>Cut a right triangle off one end and slide it across: a rectangle!</p><p style="font-size: 1.2em;">$A = b \times h$</p></div>""" + SVG_PARA + r"""</div>
                        <div class="rule orange step"><h3>Triangle</h3><p>Two identical triangles make a parallelogram, so one triangle is half: &nbsp;<span style="font-size: 1.2em;">$A = \frac12 b \times h$</span></p></div>
                        <div class="warn step">⚠️ $h$ is the <strong>perpendicular</strong> height — never the slanted side.</div>""", 'Draw the Cut')
b.slide(1, 'ido', 'Example 1 · The Sawah', r"""                        <div class="question">A rectangular sawah is 45 m by 28 m. Find the length of fence and the area to fertilise.</div>
                        <div class="steps">
                            """ + S('Perimeter', r"""$P = 2(l + w) = 2(45 + 28) = 2 \times 73$""") + r"""
                            """ + S('Answer', r"""<span class="final">$P = 146$ m</span> &nbsp; (1D — metres)""") + r"""
                            """ + S('Area', r"""$A = l \times w = 45 \times 28$""") + r"""
                            """ + S('Answer', r"""<span class="final">$A = 1260$ m²</span> &nbsp; (2D — square metres)""") + r"""
                        </div>""")
b.slide(1, 'ido', 'Example 2 · Parallelogram &amp; Triangle', r"""                        <div class="question">Parallelogram: base 9 cm, slanted side 5 cm, perpendicular height 4 cm.</div>
                        <div class="steps">
                            """ + S('Perimeter', r"""add all four sides: $P = 2(9 + 5) = $ <span class="final">28 cm</span>""") + r"""
                            """ + S('Area', r"""$A = b \times h = 9 \times 4 = $ <span class="final">36 cm²</span>""") + r"""
                            """ + S('Trap', r"""❌ $9 \times 5 = 45$ uses the slanted side — wrong!""") + r"""
                        </div>
                        <div class="question step">Triangle: base 10 cm, perpendicular height 7 cm.</div>
                        <div class="steps">""" + S('Area', r"""$A = \frac12 \times 10 \times 7 = $ <span class="final">35 cm²</span>""") + r"""</div>""")
b.slide(1, 'wedo', 'Mini-Whiteboards', r"""                        <div class="content-box"><p>✍️ Formula → substitute → answer <strong>with units</strong>. Boards up on <strong>3 – 2 – 1</strong>!</p></div>
                        <div class="question">(a) Rectangle 13 cm × 6 cm: perimeter and area</div>
                        <div class="steps">""" + S('(a)', r"""$P = 2(13 + 6) = $ <span class="final">38 cm</span> &nbsp; $A = 13 \times 6 = $ <span class="final">78 cm²</span>""") + r"""</div>
                        <div class="question">(b) Triangle: base 14 cm, height 9 cm</div>
                        <div class="steps">""" + S('(b)', r"""$A = \frac12 \times 14 \times 9 = $ <span class="final">63 cm²</span>""") + r"""</div>
                        <div class="question">(c) Parallelogram: base 11 cm, slant 7 cm, height 5 cm</div>
                        <div class="steps">""" + S('(c)', r"""$A = 11 \times 5 = $ <span class="final">55 cm²</span> &nbsp; $P = 2(11 + 7) = $ <span class="final">36 cm</span>""") + r"""</div>""", 'Common Mistakes')
b.slide(1, 'youdo', 'Worksheet 1', yd('Worksheet 1', 30, [r"""Write the formula first, then substitute.""", r"""Perimeter in cm, area in cm².""", r"""Use the <strong>perpendicular</strong> height for area.""", r"""Exit ticket: why must we use the perpendicular height, not the slanted side?"""]), 'Questions &amp; Help', 30)

# ================= MEETING 2 =================
b.slide(2, 'lec', 'Trapeziums &amp; Composite Shapes', r"""                        <div class="content-box"><h3><span class="badge bg-hook">Hook</span> 🏠</h3><p>An L-shaped room needs carpet. There is no single formula — <strong>split</strong> it into rectangles, or <strong>subtract</strong> the missing corner.</p></div>
                        <div class="rule step" style="display: flex; gap: 12px; align-items: center;"><div><h3>Trapezium</h3><p>A diagonal makes two triangles with the same height $h$:</p><p>$\frac12 ah + \frac12 bh = \frac12(a + b)h$</p><p style="font-size: 1.2em;"><strong>$A = \frac12(a + b)h$</strong></p><p class="mini">"half the sum of the parallel sides × the height"</p></div>""" + SVG_TRAP + r"""</div>
                        <div class="tip step">💡 Composite shapes: <strong>add</strong> the pieces, or <strong>subtract</strong> the holes — both give the same answer.</div>""", 'Notes')
b.slide(2, 'ido', 'Example 1 · A Trapezium', r"""                        <div class="question">Trapezium: parallel sides 5 cm and 11 cm, height 6 cm.</div>
                        <div class="steps">
                            """ + S('Formula', r"""$A = \frac12(a + b)h$""") + r"""
                            """ + S('Substitute', r"""$A = \frac12(5 + 11) \times 6 = \frac12 \times 16 \times 6$""") + r"""
                            """ + S('Answer', r"""<span class="final">$A = 48$ cm²</span>""") + r"""
                        </div>
                        <div class="tip step">✅ Check with two triangles: $\frac12(5)(6) + \frac12(11)(6) = 15 + 33 = 48$ ✔</div>""")
b.slide(2, 'ido', 'Example 2 · The L-Shaped Room', r"""                        <div style="display: flex; gap: 14px; align-items: center;">""" + SVG_L + r"""<div class="question" style="flex: 1;">Find the area of carpet: a 12 m × 9 m room with a 5 m × 4 m corner missing.</div></div>
                        <div class="steps">
                            """ + S('Subtract', r"""$12 \times 9 - 5 \times 4 = 108 - 20 = $ <span class="final">88 m²</span>""") + r"""
                            """ + S('Split', r"""bottom $12 \times 5 = 60$, top-left $7 \times 4 = 28$: $\;60 + 28 = $ <span class="final">88 m²</span> ✔""") + r"""
                        </div>""")
b.slide(2, 'wedo', 'Mini-Whiteboards', r"""                        <div class="content-box"><p>✍️ Formula → substitute → units. Boards up on <strong>3 – 2 – 1</strong>!</p></div>
                        <div class="question">(a) Trapezium: parallel sides 8 cm and 14 cm, height 5 cm</div>
                        <div class="steps">""" + S('(a)', r"""$A = \frac12(8 + 14) \times 5 = \frac12 \times 22 \times 5 = $ <span class="final">55 cm²</span>""") + r"""</div>
                        <div class="question">(b) Working backwards: a trapezium has area 60 cm² and parallel sides 7 cm and 13 cm. Find its height.</div>
                        <div class="steps">""" + S('(b)', r"""$\frac12(7 + 13)h = 60 \Rightarrow 10h = 60 \Rightarrow $ <span class="final">$h = 6$ cm</span>""") + r"""</div>""", 'Common Mistakes')
b.slide(2, 'youdo', 'Worksheet 2', yd('Worksheet 2', 30, [r"""Trapezium: $\frac12(a + b)h$ — add the parallel sides first.""", r"""Composite: draw dotted lines to split, or subtract the hole.""", r"""Label every piece's area before adding.""", r"""Exit ticket: trapezium with parallel sides 5 cm and 9 cm, height 6 cm."""]), 'Questions &amp; Help', 30)

# ================= MEETING 3 (circles) =================
b.slide(3, 'lec', 'π and the Circumference', r"""                        <div class="content-box"><h3><span class="badge bg-hook">Hook</span> 🧺</h3><p>A round <em>tampah</em> needs rattan around the rim and a banana leaf on top. A circle has <strong>no straight sides</strong> — how do we measure it?</p></div>
                        <div class="rule step"><h3>$\pi$</h3><p>Measure any circle: circumference ÷ diameter $\approx 3.14$ — always! This constant is $\pi = 3.14159\ldots$</p></div>
                        <div class="rule green step"><h3>Circumference</h3><p style="text-align: center; font-size: 1.2em;">$C = \pi d = 2\pi r$</p><p class="mini" style="text-align: center;">$d$ = diameter (across), $r$ = radius (centre to edge), $d = 2r$</p></div>""", 'Notes')
b.slide(3, 'lec', 'Area, Arcs &amp; Sectors', r"""                        <div class="rule purple"><h3>Area</h3><p>Cut a circle into thin sectors and lay them top-to-tail: almost a rectangle, $\pi r$ long and $r$ high.</p><p style="text-align: center; font-size: 1.2em;">$A = \pi r \times r = \pi r^2$</p></div>
                        <div class="rule orange step"><h3>Sector with angle $\theta$ = the fraction $\frac{\theta}{360}$ of the circle</h3><p style="text-align: center; font-size: 1.1em;">arc $= \frac{\theta}{360} \times 2\pi r$ &nbsp;&nbsp; area $= \frac{\theta}{360} \times \pi r^2$</p></div>
                        <div class="warn step">⚠️ The perimeter of a sector or semicircle = curve + the straight edges.</div>""", 'Notes')
b.slide(3, 'ido', 'Example 1 · A Whole Circle', r"""                        <div class="question">A circle has radius 6 cm. Find its circumference and its area (1 d.p.).</div>
                        <div class="steps">
                            """ + S('Circumference', r"""$C = 2\pi r = 2 \times \pi \times 6 = 12\pi$""") + r"""
                            """ + S('Answer', r"""<span class="final">$C = 12\pi \approx 37.7$ cm</span>""") + r"""
                            """ + S('Area', r"""$A = \pi r^2 = \pi \times 6^2 = 36\pi$""") + r"""
                            """ + S('Answer', r"""<span class="final">$A = 36\pi \approx 113.1$ cm²</span>""") + r"""
                        </div>
                        <div class="warn step">⚠️ $6^2 = 36$, not $12$ — square the radius <em>before</em> multiplying by $\pi$.</div>""")
b.slide(3, 'ido', 'Example 2 · A Sector', r"""                        <div style="display: flex; gap: 14px; align-items: center;">""" + SVG_SECTOR + r"""<div class="question" style="flex: 1;">A sector has radius 10 cm and angle 72°. Find the arc length, the area and the perimeter.</div></div>
                        <div class="steps">
                            """ + S('Fraction', r"""$\frac{72}{360} = \frac15$ of the circle""") + r"""
                            """ + S('Arc', r"""$\frac15 \times 2\pi \times 10 = 4\pi \approx $ <span class="final">12.6 cm</span>""") + r"""
                            """ + S('Area', r"""$\frac15 \times \pi \times 10^2 = 20\pi \approx $ <span class="final">62.8 cm²</span>""") + r"""
                            """ + S('Perimeter', r"""arc + two radii $= 4\pi + 20 \approx $ <span class="final">32.6 cm</span>""") + r"""
                        </div>""")
b.slide(3, 'wedo', 'Mini-Whiteboards', r"""                        <div class="content-box"><p>✍️ Which formula? Then substitute. Boards up on <strong>3 – 2 – 1</strong>!</p></div>
                        <div class="question">(a) Semicircle, diameter 8 cm: area and perimeter</div>
                        <div class="steps">""" + S('(a)', r"""$r = 4$: $A = \frac12\pi(4)^2 = 8\pi \approx $ <span class="final">25.1 cm²</span> &nbsp; $P = \frac12(8\pi) + 8 = 4\pi + 8 \approx $ <span class="final">20.6 cm</span>""") + r"""</div>
                        <div class="question">(b) Working backwards: a circle has circumference 50 cm. Find its diameter.</div>
                        <div class="steps">""" + S('(b)', r"""$\pi d = 50 \Rightarrow d = \frac{50}{\pi} \approx $ <span class="final">15.9 cm</span>""") + r"""</div>""", 'Common Mistakes')
b.slide(3, 'youdo', 'Worksheet 3', yd('Worksheet 3', 30, [r"""Radius or diameter? $r = \frac{d}{2}$.""", r"""$C = 2\pi r$ (cm) · $A = \pi r^2$ (cm²).""", r"""Semicircles and sectors: the perimeter includes the straight edges.""", r"""Give answers to 1 d.p.; exit ticket: the tampah (diameter 50 cm)."""]), 'Questions &amp; Help', 30)

# ================= MEETING 4 (3D & nets) =================
b.slide(4, 'lec', '3D Objects &amp; Nets', r"""                        <div class="content-box"><p>📦 <strong>Hook:</strong> a cereal box and a Toblerone box: their "skin" is flat. A <strong>net</strong> is that skin unfolded.</p></div>
                        <div class="rule step"><h3>Vocabulary</h3><p><strong>Face</strong> (flat surface) · <strong>edge</strong> (where two faces meet) · <strong>vertex</strong> (corner)</p><p>A <strong>prism</strong> has the same cross-section all the way through.</p><p class="mini">💡 Check: $F + V - E = 2$ (cuboid: $6 + 8 - 12 = 2$ ✔)</p></div>
                        <table class="tbl step"><tr><th>Solid</th><th>Faces</th><th>Edges</th><th>Vertices</th></tr><tr><td>Cuboid</td><td>6</td><td>12</td><td>8</td></tr><tr><td>Square-based pyramid</td><td>5</td><td>8</td><td>5</td></tr><tr><td>Cylinder</td><td>3 (2 flat + 1 curved)</td><td>2 (curved)</td><td>0</td></tr></table>""", 'Sketch Here')
b.slide(4, 'ido', 'Example 1 · Net of a Cuboid', r"""                        <div class="question">Draw the net of a cuboid 5 cm × 3 cm × 2 cm and label every face.</div>
                        <div class="steps">
                            """ + S('Pairs', r"""Opposite faces are equal: two of each.""") + r"""
                            """ + S('Faces', r"""$5 \times 3$ (top and bottom) · $5 \times 2$ (front and back) · $3 \times 2$ (two ends)""") + r"""
                        </div>
                        <div class="step" style="display: flex; justify-content: center;">""" + SVG_NETBOX + r"""</div>
                        <div class="tip step">✅ Fold it in your head: every edge must meet an edge of the same length.</div>""")
b.slide(4, 'ido', 'Example 2 · Net of a Cylinder', r"""                        <div class="question">A cylinder has radius 3 cm and height 10 cm. What shapes are in its net, and how long is the rectangle?</div>
                        <div class="steps">
                            """ + S('Shapes', r"""two circles (top and bottom) + one rectangle (the curved side, unrolled)""") + r"""
                            """ + S('Length', r"""the rectangle wraps once around the circle, so its length = circumference $= 2\pi r$""") + r"""
                            """ + S('Answer', r"""$2\pi \times 3 = 6\pi \approx$ <span class="final">18.8 cm by 10 cm</span>""") + r"""
                        </div>
                        <div class="step" style="display: flex; justify-content: center;">""" + SVG_CYLNET + r"""</div>""")
b.slide(4, 'wedo', 'Mini-Whiteboards', r"""                        <div class="content-box"><p>✍️ Boards up on <strong>3 – 2 – 1</strong>!</p></div>
                        <div class="question">(a) A pentagonal prism: how many faces, edges and vertices?</div>
                        <div class="steps">""" + S('(a)', r"""<span class="final">F = 7, E = 15, V = 10</span> &nbsp; Euler: $7 + 10 - 15 = 2$ ✔""") + r"""</div>
                        <div class="question">(b) A cylinder has radius 5 cm and height 8 cm. Give the size of the rectangle in its net.</div>
                        <div class="steps">""" + S('(b)', r"""$2\pi \times 5 = 10\pi \approx $ <span class="final">31.4 cm by 8 cm</span>""") + r"""</div>""", 'Common Mistakes')
b.slide(4, 'youdo', 'Worksheet 4', yd('Worksheet 4', 30, [r"""Count faces, edges and vertices; check with $F + V - E = 2$.""", r"""Nets: opposite faces are equal; edges that meet must match.""", r"""Cylinder net: rectangle $2\pi r$ by $h$, plus two circles.""", r"""Exit ticket: the length of the rectangle in a cylinder's net."""]), 'Questions &amp; Help', 30)

# ================= MEETING 5 (surface area) =================
b.slide(5, 'lec', 'Surface Area', r"""                        <div class="content-box"><h3><span class="badge bg-hook">Hook</span> 🎁</h3><p>Wrapping paper costs Rp 5 000 per m². How much paper does a gift box need — without waste?</p></div>
                        <div class="rule step"><h3>Total surface area = area of the net</h3><p>Find the area of every face, then add them up.</p></div>
                        <table class="tbl step"><tr><th>Solid</th><th>Total surface area</th></tr><tr><td>Cuboid $l \times w \times h$</td><td>$2(lw + lh + wh)$</td></tr><tr><td>Cylinder</td><td>$2\pi r^2 + 2\pi rh$ &nbsp;(two circles + curved side)</td></tr><tr><td>Prism</td><td>$2 \times$ cross-section $+$ perimeter of cross-section $\times$ length</td></tr></table>
                        <div class="warn step">⚠️ Surface area is an <strong>area</strong>: cm² or m² — not cm³.</div>""", 'Notes')
b.slide(5, 'ido', 'Example 1 · The Gift Box', r"""                        <div class="question">A gift box is 40 cm × 30 cm × 20 cm. Paper costs Rp 5 000 per m². Find the cost of paper to cover it.</div>
                        <div class="steps">
                            """ + S('Faces', r"""$40 \times 30 = 1200$, &nbsp; $40 \times 20 = 800$, &nbsp; $30 \times 20 = 600$ (two of each)""") + r"""
                            """ + S('TSA', r"""$2(1200 + 800 + 600) = 2 \times 2600 = 5200$ cm²""") + r"""
                            """ + S('Convert', r"""$1$ m² $= 100 \times 100 = 10\,000$ cm², so $5200$ cm² $= 0.52$ m²""") + r"""
                            """ + S('Cost', r"""$0.52 \times 5000 = $ <span class="final">Rp 2 600</span>""") + r"""
                        </div>""")
b.slide(5, 'ido', 'Example 2 · A Cylinder', r"""                        <div class="question">A cylinder has radius 4 cm and height 9 cm. Find its total surface area (1 d.p.).</div>
                        <div class="steps">
                            """ + S('Circles', r"""$2\pi r^2 = 2\pi(4)^2 = 32\pi$""") + r"""
                            """ + S('Curved', r"""$2\pi rh = 2\pi(4)(9) = 72\pi$ &nbsp; (the rectangle in the net)""") + r"""
                            """ + S('Total', r"""$32\pi + 72\pi = 104\pi \approx $ <span class="final">326.7 cm²</span>""") + r"""
                        </div>
                        <div class="tip step">💡 Keep answers in terms of $\pi$ until the last step — it avoids rounding errors.</div>""")
b.slide(5, 'wedo', 'Mini-Whiteboards', r"""                        <div class="content-box"><p>✍️ List the faces first. Boards up on <strong>3 – 2 – 1</strong>!</p></div>
                        <div class="question">(a) A triangular prism: right-angled cross-section with sides 3, 4, 5 cm; length 10 cm</div>
                        <div class="steps">""" + S('(a)', r"""$2 \times \frac12(3)(4) + (3 + 4 + 5) \times 10 = 12 + 120 = $ <span class="final">132 cm²</span>""") + r"""</div>
                        <div class="question">(b) A cylinder with radius 2 cm and height 5 cm</div>
                        <div class="steps">""" + S('(b)', r"""$2\pi(2)^2 + 2\pi(2)(5) = 8\pi + 20\pi = 28\pi \approx $ <span class="final">88.0 cm²</span>""") + r"""</div>""", 'Common Mistakes')
b.slide(5, 'youdo', 'Worksheet 5', yd('Worksheet 5', 30, [r"""Scaffold: list every face in a table (shape, size, area, how many).""", r"""Cylinder: $2\pi r^2 + 2\pi rh$.""", r"""Answer in cm² (convert to m² for costs: ÷ 10 000).""", r"""Exit ticket: cylinder with radius 5 cm and height 10 cm."""]), 'Questions &amp; Help', 30)

# ================= MEETING 6 (volume) =================
b.slide(6, 'lec', 'Volume', r"""                        <div class="content-box"><p>🥩 "Surface area is the <strong>skin</strong>. Volume is the <strong>meat</strong>." How much space is inside?</p></div>
                        <div class="rule step"><h3>Prisms and cylinders: stack the cross-section</h3><p style="text-align: center; font-size: 1.15em;">$V = \text{area of cross-section} \times \text{length}$ &nbsp;·&nbsp; cylinder $V = \pi r^2 h$</p></div>
                        <div class="rule purple step" style="display: flex; gap: 10px; align-items: center;"><div><h3>Pyramids and cones</h3><p>Rice from <strong>3</strong> pyramids exactly fills a prism with the same base and height:</p><p style="text-align: center; font-size: 1.15em;">$V = \frac13 \times \text{base area} \times h$ &nbsp;·&nbsp; cone $V = \frac13\pi r^2 h$</p></div>""" + SVG_RICE + r"""</div>
                        <div class="tip step">💡 Units: cm³ · and $1$ litre $= 1000$ cm³.</div>""", 'Notes')
b.slide(6, 'ido', 'Example 1 · Prism &amp; Cylinder', r"""                        <div class="question">(i) A triangular prism: cross-section base 6 cm and height 4 cm, length 15 cm.</div>
                        <div class="steps">
                            """ + S('Area', r"""cross-section $= \frac12 \times 6 \times 4 = 12$ cm²""") + r"""
                            """ + S('Volume', r"""$V = 12 \times 15 = $ <span class="final">180 cm³</span>""") + r"""
                        </div>
                        <div class="question step">(ii) A cylinder: radius 3 cm, height 10 cm.</div>
                        <div class="steps">""" + S('Volume', r"""$V = \pi r^2 h = \pi \times 9 \times 10 = 90\pi \approx $ <span class="final">282.7 cm³</span>""") + r"""</div>""")
b.slide(6, 'ido', 'Example 2 · Cone &amp; Pyramid', r"""                        <div class="question">(i) A cone: radius 5 cm, height 12 cm.</div>
                        <div class="steps">""" + S('Volume', r"""$V = \frac13\pi r^2 h = \frac13 \times \pi \times 25 \times 12 = 100\pi \approx $ <span class="final">314.2 cm³</span>""") + r"""</div>
                        <div class="question step">(ii) A square-based pyramid: base 6 cm, height 10 cm.</div>
                        <div class="steps">""" + S('Volume', r"""$V = \frac13 \times 6^2 \times 10 = \frac13 \times 360 = $ <span class="final">120 cm³</span>""") + r"""</div>
                        <div class="warn step">⚠️ Use the <strong>perpendicular</strong> height of the cone or pyramid, not the slant height.</div>""")
b.slide(6, 'wedo', 'Mini-Whiteboards', r"""                        <div class="content-box"><p>✍️ Boards up on <strong>3 – 2 – 1</strong>!</p></div>
                        <div class="question">(a) A cone and a cylinder have the same radius and height. The cylinder holds 300 cm³. The cone?</div>
                        <div class="steps">""" + S('(a)', r"""$\frac13 \times 300 = $ <span class="final">100 cm³</span>""") + r"""</div>
                        <div class="question">(b) A fish tank is 50 cm × 30 cm × 40 cm. How many litres?</div>
                        <div class="steps">""" + S('(b)', r"""$60\,000$ cm³ $\div 1000 = $ <span class="final">60 litres</span>""") + r"""</div>
                        <div class="question">(c) A cylinder has volume $200\pi$ cm³ and radius 5 cm. Find its height.</div>
                        <div class="steps">""" + S('(c)', r"""$25\pi h = 200\pi \Rightarrow $ <span class="final">$h = 8$ cm</span>""") + r"""</div>""", 'Common Mistakes')
b.slide(6, 'youdo', 'Worksheet 6', yd('Worksheet 6', 30, [r"""Prism / cylinder: area of cross-section × length.""", r"""Pyramid / cone: $\frac13$ × base area × height.""", r"""Volume in cm³ (1 litre = 1000 cm³).""", r"""Exit ticket: the cone and cylinder with the same radius and height."""]), 'Questions &amp; Help', 30)

# ================= MEETING 7 (spheres, review, test) =================
b.slide(7, 'lec', 'Peeling the Orange', r"""                        <div class="content-box" style="display: flex; gap: 10px; align-items: center;"><div><h3><span class="badge bg-hook">Hook</span> 🍊</h3><p>Draw 4 circles with the orange's radius. The peel fills <strong>exactly 4</strong> of them!</p></div>""" + SVG_ORANGE + r"""</div>
                        <div class="rule step"><h3>Sphere</h3><p style="text-align: center; font-size: 1.2em;">surface area $= 4\pi r^2$ &nbsp;&nbsp;&nbsp; volume $= \frac43\pi r^3$</p></div>
                        <div class="question step">A ball has radius 5 cm.</div>
                        <div class="steps">
                            """ + S('Surface', r"""$4\pi(5)^2 = 100\pi \approx $ <span class="final">314.2 cm²</span>""") + r"""
                            """ + S('Volume', r"""$\frac43\pi(5)^3 = \frac{500}{3}\pi \approx $ <span class="final">523.6 cm³</span>""") + r"""
                        </div>""", 'Notes')
b.slide(7, 'ido', 'Example · A Hemisphere', r"""                        <div class="question">A solid hemisphere has radius 4 cm. Find its total surface area and its volume (1 d.p.).</div>
                        <div class="steps">
                            """ + S('Curved', r"""half a sphere: $\frac12 \times 4\pi r^2 = 2\pi(4)^2 = 32\pi$""") + r"""
                            """ + S('Flat', r"""the circular base: $\pi r^2 = 16\pi$""") + r"""
                            """ + S('Total', r"""$32\pi + 16\pi = 48\pi \approx $ <span class="final">150.8 cm²</span>""") + r"""
                            """ + S('Volume', r"""$\frac12 \times \frac43\pi(4)^3 = \frac{128}{3}\pi \approx $ <span class="final">134.0 cm³</span>""") + r"""
                        </div>
                        <div class="warn step">⚠️ Don't forget the flat circle on a <strong>solid</strong> hemisphere.</div>""")
WR = [(r"""Fence around a field""", r"""Perimeter — m"""), (r"""Paint for a wall with a door""", r"""Composite area (subtract) — m²"""), (r"""Rattan around a round tray""", r"""Circumference $2\pi r$ — cm"""), (r"""Paper to wrap a tin""", r"""Surface area $2\pi r^2 + 2\pi rh$ — cm²"""), (r"""Water in an ice-cream cone""", r"""Volume $\frac13\pi r^2h$ — cm³"""), (r"""Leather on a football""", r"""Sphere surface $4\pi r^2$ — cm²""")]
b.slide(7, 'rev', '1D, 2D or 3D? Which Formula?', r"""                        <div class="content-box"><p>🗣️ Name the measurement, the formula and the unit — <strong>don't calculate</strong>. Cold call!</p></div>
                        <table class="tbl">""" + ''.join(r"""<tr><td style="width: 45%%;">%d. %s</td><td class="step answer">%s</td></tr>""" % (i + 1, q, a) for i, (q, a) in enumerate(WR)) + r"""</table>""", 'Votes')
b.slide(7, 'rev', 'Chapter 7 Evaluation', r"""                        <div class="rule green">
                            <h3><span class="badge bg-exit">Chapter 7 Test</span> 45 minutes</h3>
                            <ul class="checklist"><li>Composite areas, circles, surface areas from nets, volumes and working backwards.</li><li>Visual aids away — formulas from <strong>your own memory</strong>.</li><li>Show your working and write the units (cm, cm², cm³) in every answer.</li><li><span style="color: #c0392b; font-weight: bold;">Self-Regulated:</span> about 1 minute per mark; leave 5 minutes to check.</li></ul>
                        </div>
                        <div class="slide-timer" data-min="45">45:00</div>
                        <div class="content-box mini"><p>🔚 <strong>Reflection (10 min):</strong> which formula was hardest to remember — and which example on this board helped you most?</p></div>""", 'Reflection', 45)

out = os.path.join(REPO, 'dm/g09/t07-perimeter-area-and-volume/bd-02.html')
print('slides', b.build(out), '->', out)
