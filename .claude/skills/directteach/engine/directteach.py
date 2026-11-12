'''Direct-teaching board engine (Lecture -> I Do -> We Do -> You Do).

Usage (from a content script):

    import sys; sys.path.insert(0, '<repo>/.claude/skills/directteach/engine')
    from directteach import Board, S
    b = Board('Board 2 - Perimeter, Area and Volume (Direct Teaching)',
              meetings=['Overview', 'Perimeter & area', ...])          # index 0 = overview
    b.title('Perimeter, Area &amp; Volume', 'Grade 9 Mathematics — Topic 7')
    b.slide(1, 'lec', 'Title', r"""...left column HTML...""", write='Notes')
    b.slide(1, 'ido', 'Example 1', r"""<div class="question">...</div>""" + S('Step 1', r"""...""") )
    b.slide(1, 'youdo', 'Worksheet 1', b.youdo('Worksheet 1', 30, ['tip', ...]), timer=30)
    b.build('<repo>/dm/g09/t07-.../bd-02.html')

Authoring rules
- Always write HTML/TeX in raw triple-double-quoted strings r\"\"\"...\"\"\" (primes like u' and
  backslashes like \\frac then survive; never use plain '...' strings for TeX).
- Anything with class "step" is hidden until revealed (Space / -> / clicker / Reveal button).
  S(label, body) makes a numbered step line; put class="step" on any other element to reveal it.
- Answers that should stand out: <span class="final">...</span>.
- Useful blocks: .question, .rule (.purple/.orange/.green), .warn, .tip, .content-box, .grid22, .tbl, .mini.
- A slide with timer=N gets the toolbar countdown preset to N minutes; youdo(...) also prints a big clock.
'''
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TAGS = {'lec': ('p-lec', 'Lecture'), 'ido': ('p-ido', 'I Do'), 'wedo': ('p-wedo', 'We Do'),
        'youdo': ('p-youdo', 'You Do'), 'rev': ('p-rev', 'Review')}


def S(label, body, step=True):
    """A numbered/labelled step line, hidden until revealed (step=False shows it immediately)."""
    return '<div class="stepl%s"><span class="n">%s</span><div>%s</div></div>' % (' step' if step else '', label, body)


class Board:
    def __init__(self, page_title, meetings):
        self.page_title = page_title
        self.meetings = meetings
        self.slides = []

    def title(self, h1, h2, tagline='Direct Teaching — watch the method, practise it together, then master it alone.'):
        self.slides.append('''        <div class="slide title-slide active" data-meeting="0">
            <canvas class="drawing-board"></canvas>
            <div class="content-layer">
                <h1>%s</h1>
                <h2>%s</h2>
                <div class="flow"><span class="chip p-lec">📢 Lecture</span><span class="arrow">→</span><span class="chip p-ido">👩‍🏫 I Do</span><span class="arrow">→</span><span class="chip p-wedo">🤝 We Do</span><span class="arrow">→</span><span class="chip p-youdo">✍️ You Do</span></div>
                <p style="font-size: 1.3em; color: #276749; font-weight: bold;">%s</p>
                <p><em>Space / → / clicker reveals the next step · ← goes back · ✏️ write on any slide · ⏱️ timer on every "You Do" slide</em></p>
            </div>
        </div>
''' % (h1, h2, tagline))

    def raw(self, meeting, title, left, write='Notes', flex='1.4'):
        """A slide without a phase tag (e.g. roadmap)."""
        self.slides.append(self._wrap(meeting, '', title, left, write, None, flex))

    def slide(self, meeting, phase, title, left, write='Teacher Working', timer=None, flex='1.25'):
        cls, lab = TAGS[phase]
        head = 'Meeting %d · <span class="%s tag">%s</span> %s' % (meeting, cls, lab, title)
        self.slides.append(self._wrap(meeting, ' data-timer="%d"' % timer if timer else '', head, left, write, None, flex))

    def _wrap(self, meeting, attrs, head, left, write, _unused, flex):
        return '''        <div class="slide" data-meeting="%d"%s>
            <canvas class="drawing-board"></canvas>
            <div class="content-layer">
                <h2 class="header-title">%s</h2>
                <div class="two-column">
                    <div class="col" style="flex: %s;">
%s
                    </div>
                    <div class="col-write"><div class="write-label">%s</div></div>
                </div>
            </div>
        </div>
''' % (meeting, attrs, head, flex, left, write)

    @staticmethod
    def youdo(label, mins, items, extra=''):
        return '''                        <div class="rule green">
                            <h3><span class="badge bg-activity">%s</span> Independent practice · %d min</h3>
                            <ul class="checklist">%s</ul>
                        </div>
%s                        <div class="slide-timer" data-min="%d">%02d:00</div>''' % (label, mins, ''.join('<li>%s</li>' % i for i in items), extra, mins, mins)

    def build(self, out_path):
        with open(os.path.join(HERE, 'board_template.html')) as f:
            tpl = f.read()
        jump = ''.join('<option value="%d">%s</option>' % (i, ('📅 ' + m) if i == 0 else 'Meeting %d · %s' % (i, m))
                       for i, m in enumerate(self.meetings))
        html = tpl.replace('{{TITLE}}', self.page_title).replace('{{JUMP}}', jump).replace('{{SLIDES}}', ''.join(self.slides))
        assert '{{' not in html
        bad = [c for c in html if ord(c) < 32 and c not in '\n\t']
        assert not bad, 'control characters in output: a TeX string was not raw'
        with open(out_path, 'w') as f:
            f.write(html)
        return len(self.slides)
