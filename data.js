/**
 * Ghozi Learning Kit — content map
 * -----------------------------------------------------------------------
 * This file is the single source of truth for the menu and the router.
 * To add content: drop the .html file in the matching dm/g{grade}/{topic}
 * folder, then add one line below. No other code needs to change.
 *
 * Section keys (fixed, in teaching order):
 *   lp = Lesson Plan        (always exactly one file, no index)
 *   bd = Board               (1 or more files)
 *   im = Interactive Media   (1 or more files)
 *   ws = Worksheet           (1 or more files)
 *   ha = Hands-on Activity   (1 or more files)
 */

const LEARNING_KIT_DATA = {
  kitTitle: "Mr. Ghozi Learning Kit",
  grades: [
    {
      grade: 9,
      folder: "g09",
      label: "Grade 9",
      topics: [
        {
          id: 1,
          slug: "t01-review-number-concept",
          title: "Review of Number Concept",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [{ index: 1, file: "im-01.html", title: "Interactive Media 1" }] },
            ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2" },
              ],
            },
            ha: { label: "Hands-on Activity", files: [{ index: 1, file: "ha-01.html", title: "Hands-on Activity 1" }] },
          },
        },
        {
          id: 2,
          slug: "t02-making-sense-of-algebra",
          title: "Making Sense of Algebra",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: {
              label: "Interactive Media",
              files: [
                { index: 1, file: "im-01.html", title: "Interactive Media 1" },
                { index: 2, file: "im-02.html", title: "Interactive Media 2" },
              ],
            },
             ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2" },
                { index: 3, file: "ws-03.html", title: "Worksheet 3" },
              ],
            },
            ha: { label: "Hands-on Activity", files: [{ index: 1, file: "ha-01.html", title: "Hands-on Activity 1" }] },
          },
        },
        {
          id: 3,
          slug: "t03-lines-angles-and-shapes",
          title: "Lines, Angles and Shapes",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2" },
				{ index: 3, file: "ws-03.html", title: "Worksheet 3" },
              ],
            },
            ha: { label: "Hands-on Activity", files: [{ index: 1, file: "ha-01.html", title: "Hands-on Activity 1" }] },
          },
        },
        {
          id: 4,
          slug: "t04-collecting-organising-and-displaying-data",
          title: "Collecting, Organising and Displaying Data",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: {
              label: "Board",
              files: [
                { index: 1, file: "bd-01.html", title: "Board 1" },
                { index: 2, file: "bd-02.html", title: "Board 2" },
              ],
            },
            ws: { label: "Worksheet", files: [{ index: 1, file: "ws-01.html", title: "Worksheet 1" }] },
          },
        },
        {
          id: 5,
          slug: "t05-fractions-percentages-and-standard-form",
          title: "Fractions, Percentages and Standard Form",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [{ index: 1, file: "im-01.html", title: "Interactive Media 1" }] },
            ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1 Fractions (Meeting 1)" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2 Percentages (Meeting 2)" },
                { index: 3, file: "ws-03.html", title: "Worksheet 3 Standard Form (Meeting 3)" },
                { index: 4, file: "ws-04.html", title: "🔒 Worksheet 4 Chapter 5 Test (Meeting 4)" },
              ],
            },
            ha: {
              label: "Hands-on Activity",
              files: [
                { index: 1, file: "ha-01.html", title: "Hands-on 1 Fraction Circles (Meeting 1)" },
                { index: 2, file: "ha-02.html", title: "Hands-on 2 Nutrition Labels (Meeting 2)" },
                { index: 3, file: "ha-03.html", title: "Hands-on 3 Frog-Jump Strips (Meeting 3)" },
                { index: 4, file: "ha-04.html", title: "Hands-on 4 Review Loop Cards (Meeting 4)" },
              ],
            },
          },
        },
        {
          id: 6,
          slug: "t06-equations-factors-and-formulae",
          title: "Equations, Factors and Formulae",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [{ index: 1, file: "im-01.html", title: "Interactive Media 1" }] },
            ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1 Linear Equations (Meeting 1)" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2 Complex Equations (Meeting 2)" },
                { index: 3, file: "ws-03.html", title: "Worksheet 3 Factorising (Meeting 3)" },
                { index: 4, file: "ws-04.html", title: "Worksheet 4 Complex Factorisation (Meeting 4)" },
                { index: 5, file: "ws-05.html", title: "Worksheet 5 Rearranging Formulae (Meeting 5)" },
                { index: 6, file: "ws-06.html", title: "🔒 Worksheet 6 Chapter 6 Test (Meeting 6)" },
              ],
            },
            ha: {
              label: "Hands-on Activity",
              files: [
                { index: 1, file: "ha-01.html", title: "Hands-on 1 Balance Mat (Meeting 1)" },
                { index: 2, file: "ha-02.html", title: "Hands-on 2 Algebra Tiles (Meeting 2)" },
                { index: 3, file: "ha-03.html", title: "Hands-on 3 Area Model (Meeting 3)" },
                { index: 4, file: "ha-04.html", title: "Hands-on 4 Fully or Not? (Meeting 4)" },
                { index: 5, file: "ha-05.html", title: "Hands-on 5 Formula Machines (Meeting 5)" },
                { index: 6, file: "ha-06.html", title: "Hands-on 6 Review Loop (Meeting 6)" },
              ],
            },
          },
        },
        {
          id: 7,
          slug: "t07-perimeter-area-and-volume",
          title: "Perimeter, Area and Volume",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: {
              label: "Interactive Media",
              files: [
                { index: 1, file: "im-01.html", title: "Interactive Media 1 Cut & Slide (Meeting 1)" },
                { index: 2, file: "im-02.html", title: "Interactive Media 2 Trapezium & Composite (Meeting 2)" },
                { index: 3, file: "im-03.html", title: "Interactive Media 3 Circle Lab (Meeting 3)" },
                { index: 4, file: "im-04.html", title: "Interactive Media 4 Net Folder 3D (Meeting 4)" },
                { index: 5, file: "im-05.html", title: "Interactive Media 5 Gift Wrap Calculator (Meeting 5)" },
                { index: 6, file: "im-06.html", title: "Interactive Media 6 Rice Pouring Lab (Meeting 6)" },
                { index: 7, file: "im-07.html", title: "Interactive Media 7 Orange Peel & Review (Meeting 7)" },
              ],
            },
            ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1 Perimeter & Area (Meeting 1)" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2 Trapezium & Composite (Meeting 2)" },
                { index: 3, file: "ws-03.html", title: "Worksheet 3 Circles (Meeting 3)" },
                { index: 4, file: "ws-04.html", title: "Worksheet 4 3D Objects & Nets (Meeting 4)" },
                { index: 5, file: "ws-05.html", title: "Worksheet 5 Surface Area (Meeting 5)" },
                { index: 6, file: "ws-06.html", title: "Worksheet 6 Volume (Meeting 6)" },
                { index: 7, file: "ws-07.html", title: "🔒 Worksheet 7 Chapter 7 Test (Meeting 7)" },
              ],
            },
            ha: {
              label: "Hands-on Activity",
              files: [
                { index: 1, file: "ha-01.html", title: "Hands-on 1 Cut & Slide (Meeting 1)" },
                { index: 2, file: "ha-02.html", title: "Hands-on 2 Trapezium & Rooms (Meeting 2)" },
                { index: 3, file: "ha-03.html", title: "Hands-on 3 Hunt for π & Pizza (Meeting 3)" },
                { index: 4, file: "ha-04.html", title: "Hands-on 4 Nets to Fold (Meeting 4)" },
                { index: 5, file: "ha-05.html", title: "Hands-on 5 Measure the Net (Meeting 5)" },
                { index: 6, file: "ha-06.html", title: "Hands-on 6 Rice Pouring (Meeting 6)" },
                { index: 7, file: "ha-07.html", title: "Hands-on 7 Orange & Review Loop (Meeting 7)" },
              ],
            },
          },
        },
      ],
    },
    {
      grade: 12,
      folder: "g12",
      label: "Grade 12",
      topics: [
        {
          id: 1,
          slug: "t01-permutation-combination",
          title: "Permutation & Combination",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [{ index: 1, file: "im-01.html", title: "Interactive Media 1" }] },
            ws: { label: "Worksheet", files: [{ index: 1, file: "ws-01.html", title: "Worksheet 1" }] },
            ha: { label: "Hands-on Activity", files: [{ index: 1, file: "ha-01.html", title: "Hands-on Activity 1" }] },
          },
        },
		 {
          id: 2,
          slug: "t02-algebra",
          title: "Algebra",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [{ index: 1, file: "im-01.html", title: "Interactive Media 1" }] },
            ws: { label: "Worksheet", files: [{ index: 1, file: "ws-01.html", title: "Worksheet 1" }] },
          },
        },
		  {
          id: 3,
          slug: "t03-logarithm",
          title: "Logarithm",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [{ index: 1, file: "im-01.html", title: "Interactive Media 1" }] },
            ws: { 
				label: "Worksheet", 
				files: [
					{ index: 1, file: "ws-01.html", title: "Worksheet 1" },
					{ index: 2, file: "ws-02.html", title: "Worksheet 2" },
					{ index: 3, file: "ws-03.html", title: "Worksheet 3 Solving Log Equation" }
				] },
          },
        },
        {
          id: 4,
          slug: "t04-trigonometry",
          title: "Trigonometry",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1" }] },
            im: { label: "Interactive Media", files: [
              { index: 1, file: "im-01.html", title: "Interactive Media 1 Web Lab" },
              { index: 2, file: "im-02.html", title: "Interactive Media 2 Unit Circle (Meeting 1) — twin of Hands-on 1" },
              { index: 3, file: "im-03.html", title: "Interactive Media 3 Proof Kit (Meeting 2) — twin of Hands-on 2" },
              { index: 4, file: "im-04.html", title: "Interactive Media 4 Double Angle (Meeting 3) — twin of Hands-on 3" },
              { index: 5, file: "im-05.html", title: "Interactive Media 5 Proof Puzzles (Meeting 4) — twin of Hands-on 4" },
              { index: 6, file: "im-06.html", title: "Interactive Media 6 Waves, Tide & Transformations (Meeting 5) — twin of Hands-on 5" },
              { index: 7, file: "im-07.html", title: "Interactive Media 7 Review Loop (Meeting 6) — twin of Hands-on 6" }
            ] },
            ws: {
              label: "Worksheet",
              files: [
                { index: 1, file: "ws-01.html", title: "Worksheet 1 sec, cosec, cot (Meeting 1)" },
                { index: 2, file: "ws-02.html", title: "Worksheet 2 Compound Angles (Meeting 2)" },
                { index: 3, file: "ws-03.html", title: "Worksheet 3 Double Angles (Meeting 3)" },
                { index: 4, file: "ws-04.html", title: "Worksheet 4 Identities (Meeting 4)" },
                { index: 5, file: "ws-05.html", title: "Worksheet 5 R-Formula & Tide (Meeting 5)" },
                { index: 6, file: "ws-06.html", title: "🔒 Worksheet 6 Chapter 3 Test (Meeting 6)" },
              ],
            },
            ha: {
              label: "Hands-on Activity",
              files: [
                { index: 1, file: "ha-01.html", title: "Hands-on 1 Unit Circle (Meeting 1)" },
                { index: 2, file: "ha-02.html", title: "Hands-on 2 Proof Kit (Meeting 2)" },
                { index: 3, file: "ha-03.html", title: "Hands-on 3 Double Angle (Meeting 3)" },
                { index: 4, file: "ha-04.html", title: "Hands-on 4 Proof Puzzles (Meeting 4)" },
                { index: 5, file: "ha-05.html", title: "Hands-on 5 Waves & Tide Report (Meeting 5)" },
                { index: 6, file: "ha-06.html", title: "Hands-on 6 Review Loop (Meeting 6)" },
              ],
            },
          },
        },
        {
          id: 5,
          slug: "t05-differentiation",
          title: "Differentiation",
          sections: {
            lp: { label: "Lesson Plan", files: [{ file: "lp.html", title: "Lesson Plan" }] },
            bd: { label: "Board", files: [{ index: 1, file: "bd-01.html", title: "Board 1 (Direct Instruction)" }] },
          },
        },
      ],
    },
  ],
};
