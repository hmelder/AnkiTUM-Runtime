import genanki



styling = """
:root {
	--s: 10px;
  --card-max-width: 80em;
  --card-text-align: left;
  --font-size-regular: 16px;
  --font-size-small: 14px;
  --font-family: "Rubik", -apple-system, sytem-ui, BlinkMacSystemFont, Segoe UI,
    Roboto, Helvetica, Arial, sans-serif;
  --img-width: 80%;
  --img-width-hover: 110%;
  --img-brightness: 1.0;
  --img-filter: brightness(100%);

	--max-width: 85%;
	--max-width-typeans: 450px;

	--opacity: 50%;
}

.card {
	font-family: arial;
	font-size: 22px;
 	text-align: center;
	color: var(--text-dark-white);
  line-height: 1.75;
  cursor: default;
  padding: 0.5em 0;
}

.card.night_mode {
  /* Dark theme */
  background-color: #191919;
  --text-bg-selected: #3b4252;
  --card-bg: #2e3440;
  --card-border: transparent;
  --card-box-shadow: #0f111540;
  --divider: #4c566a;
  --tag-fg: #d8dee9;
  --tag-bg: transparent;
  --tag-fg-active: #8fbcbb;
  --tag-bg-active: transparent;
  --tag-border: #4c566a;
  --tag-border-active: #8fbcbb;
  --cloze-fg: #CE8179;
  --cloze-bg: transparent;
  --link-fg: #81a1c1;
  --link-bg: transparent;
  --link-fg-active: #8fbcbb;
  --link-bg-active: #434c5e;
  --bold-fg: #8FB98C;
  --italic-fg: #D1C788;
  --bold-italic-fg: #869DB2;
  --underline-fg: #A6829F;	
	--text-dark-white: #d9d9d9;
}

html:not(.mobile) .card {
  padding: 0.5em;
}

.card::-webkit-scrollbar {
  display: none;
}

.inline-block{
	display: inline-block;
 	position: relative;
	left: 50%;
  transform: translateX(-50%);
	max-width: var(--max-width);
	margin: 0 auto;
	padding: 9px;
	color: var(--text-dark-white);
}

.inline-block#front {
	font-size: calc(27px + var(--s));
	margin-top: 0px;
	line-height: 1.6;
}

.inline-block#back {
	border: 2px solid var(--card-bg);
	font-size: calc(20px + var(--s));
	line-height: 1.5;
}

.inline-block#example {
	font-size: calc(15px + var(--s));
	line-height: 1.5;
}

#image {
	font-size: calc(20px + var(--s));
	margin-top: 9px;
	padding: 0px;
	text-align: center;
}

#title {
	font-family: times new roman;
	font-size: calc(15px + var(--s));
	padding: 0px;
	margin-bottom: 0px;
	border-radius: 0px;
	line-height: 110%;
	color: #7a869f;
	text-align: center;
}

hr#answer {
  height: 4px;
  background: var(--divider);
	border: 0;
	magin: 0;
}

hr#answer--fade {
  height: 4px;
  background: var(--divider);
	border: 0;
	magin: 0;
	margin-top: -5px;
}

.flashcard {
  background-color: var(--card-bg);
  border-radius: 1em;
  border: 1px solid var(--card-border);
  box-shadow: var(--card-box-shadow) 0px 5px 7px;
  color: var(--text-fg);
  font-family: var(--font-family);
  font-size: var(--font-size-regular);
  line-height: 1.2;
  margin: 0 auto;
  max-width: var(--card-max-width);
  text-align: var(--card-text-align);
  word-wrap: break-word;
}

.flashcard#fade-top {
  border-radius: 1em 1em 0em 0em;
	opacity: 0.5;
  box-shadow: var(--card-box-shadow) 0px 0px 0px;
}

.flashcard#fade-bottom {
  border-radius: 0em 0em 1em 1em;
}

.flashcard .hr{
	height: 4px;
  background: var(--divider);
	border: 0;
	magin: 0;
}

.flashcard ::selection {
  background-color: var(--text-bg-selected);
}

.field {
  margin: 2em;
}

.fade .field {
  margin: 2em;
}

.mobile .field {
  margin: 1em;
}

.mobile .fade .field {
  margin: 1em;
}

.field-back {
  font-size: var(--font-size-small);
}

.fade .field-back {
  font-size: var(--font-size-small);
	opacity: var(--opacity);
}

.field-front {
  font-size: var(--font-size-small);
}

.fade .field-front {
  font-size: var(--font-size-small);
	opacity: var(--opacity);
}

.divider {
  background-color: transparent;
  border: none;
  border-bottom: 1px dashed var(--divider);
  margin: 1em;
  padding: 0;
}

.divider-answer {
  border-bottom: 2px solid var(--divider);
}

img {
  border-radius: 0.25em;
  display: block;
  margin: 1em auto;
  max-width: var(--img-width) !important;
  transition: max-width 0.25s 0.1s, opacity 0.25s 0.1s, 		filter 0.1s, transform 0s;
}

.night_mode img {
  filter: var(--img-filter);
  opacity: var(--img-brightness);
}

img:hover {
  border-radius: 0.25em;
  cursor: zoom-in;
  filter: none;
  max-width: var(--img-width-hover) !important;
  opacity: 1;
}

img + br {
  display: none;
}

html:not(.mobile) img:active {
  border: 1px solid var(--link-fg-active);
  cursor: zoom-out;
  filter: none;
  left: 0;
  max-width: 95% !important;
  opacity: 1;
  position: fixed;
  top: 0;
  transform: translate(calc(50vw - 50%), calc(50vh - 50%));
  z-index: 100;
}

a, a:visited {
  text-decoration: none;
  color: var(--link-fg);
  border-radius: 0.25em;
  padding: 0 0.1em;
  transition: all 0.1s;
}

a:hover, a:active {
  color: var(--link-fg-active);
  background-color: var(--link-bg-active);
}

b, strong {
  color: var(--bold-fg);
}

i, em {
  color: var(--italic-fg);
}

b > i, i > b {
  color: var(--bold-italic-fg);
}

u {
  color: var(--underline-fg);
}


@font-face {
  font-family: Rubik;
  src: local("Rubik-Regular"), url("_Rubik-Regular.woff2") format("woff2");
  font-style: normal;
  font-weight: normal;
}

@font-face {
  font-family: Rubik;
  src: local("Rubik-Bold"), url("_Rubik-Bold.woff2") format("wofff2");
  font-style: normal;
  font-weight: bold;
}

@font-face {
  font-family: Rubik;
  src: local("Rubik-Italic"), url("_Rubik-Italic.woff2") format("wofff2");
  font-style: italic;
  font-weight: normal;
}

@font-face {
  font-family: Rubik;
  src: local("Rubik-BoldItalic"), url("_Rubik-BoldItalic.woff2") format("wofff2");
  font-style: italic;
  font-weight: bold;
}
"""

basic_model = genanki.Model(
    1559323000,
    'AnkiTUM Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Title'},
        {'name': 'Chapter'},
        {'name': 'Logo'}
    ],
    templates=[
        {
            'name': 'AnkiTUM Basic',
            'qfmt': """     
                <div class="flashcard">
                  <div class="field field-front">
                        {{#Title}}
                            <div id="title">
                                {{Title}}
                            </div>
                        {{/Title}}
                  </div>
                    <div class="field field-front">
                        <div class="inline-block" id="front">
                            <span style="font-weight:normal;">{{edit::Front}}</span>
                        </div>
                    </div>
                </div>
            """,
            'afmt': """
                <div class="flashcard" id="fade-top">
                  <div class="field field-front">
                        {{#Title}}
                            <div id="title">
                                {{Title}}
                            </div>
                        {{/Title}}
                  </div>
                    <div class="field field-front">
                        <div class="inline-block" id="front">
                            <span style="font-weight:normal;">{{edit::Front}}</span>
                        </div>
                    </div>
                </div>
                <div class="flashcard" id="fade-bottom">
                    <hr id=answer--fade>
                    {{#Back}}
                        <div class="field field-back">
                            <div class="inline-block" id="back">
                                {{Back}}
                            </div>
                        </div>
                    {{/Back}}
                </div>
            """,
        },
    ],
    css=styling
)

cloze_field = """
                    <div class="flashcard">
                  <div class="field field-front">
                        {{#Title}}
                            <div id="title">
                                {{Title}}
                            </div>
                        {{/Title}}
                  </div>
                    <div class="field field--front">
                        <div class="inline-block" id="front">
                            <span style="font-weight:normal;">
                                {{cloze::Front}}
                            </span>
                        </div>
                    </div>
                </div>
"""
cloze_model = genanki.Model(
  340857584,
  'AnkiTUM Cloze',
  model_type=genanki.Model.CLOZE,
  fields=[
    {'name': 'Front'},
    {'name': 'Title'},
    {'name': 'Chapter'}
  ],
  templates=[
    {
      'name': 'Cloze',
      'qfmt': cloze_field,
      'afmt': cloze_field
    },
  ],
  css=styling
)

latex_plus = genanki.Model(
    24354521800,
    'AnkiTUM Latex',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Title'},
        {'name': 'Chapter'},
        {'name': 'Logo'}
    ],
    templates=[
        {
            'name': 'AnkiTUM Latex+',
            'qfmt': """     
                <div class="flashcard">
                  <div class="field field-front">
                        {{#Title}}
                            <div id="title">
                                {{Title}}
                            </div>
                        {{/Title}}
                  </div>
                    <div class="field field-front">
                        <div class="inline-block" id="front">
                            <span style="font-weight:normal;">{{edit::Front}}</span>
                        </div>
                    </div>
                </div>
            """,
            'afmt': """
            <div class="flashcard" id="fade-top">
              <div class="field field-front">
                    {{#Title}}
                        <div id="title">
                            {{Title}}
                        </div>
                    {{/Title}}
              </div>
                <div class="field field-front">
                    <div class="inline-block" id="front">
                        <span style="font-weight:normal;">{{edit::Front}}</span>
                    </div>
                </div>
            </div>
            <div class="flashcard" id="fade-bottom">
                <hr id=answer--fade>
                {{#Back}}
                    <div class="field field-back">
                        <div class="inline-block" id="back">
                            {{Back}}
                        </div>
                    </div>
                {{/Back}}
            </div>
            """,
        },
    ],
    css=styling,
    # credit: Sebastian Pfister
    latex_pre=""" 
    
        \\documentclass[12pt]{article}
        \\usepackage[ngerman]{babel}
        \\special{papersize=3in,5in}
        \\usepackage[utf8]{inputenc}
        \\usepackage{amssymb,amsmath}
        \\pagestyle{empty}
        \\setlength{\\parindent}{0in}
        
        %start preamble
        \\usepackage{tikz}
        \\usepackage{parskip}
        \\usepackage{amsmath}
        \\usepackage{mathtools}
        \\usepackage{bm}
        \\usepackage{tabularx}
        
        % packages for fancy description
        \\usepackage{enumitem}
        \\setlist[description]{font={\\normalfont\\itshape}}
        
        % keep the parskip on minipages
        \\newlength{\\currentparskip}
        \\newenvironment{halfpage}
        {\\setlength{\\currentparskip}{\\parskip}%
            \\begin{minipage}[t]{0.46\\textwidth}%
                \\setlength{\\parskip}{\\currentparskip}%
                }
                {\\end{minipage}}
        %end preamble
        
        % start numprog specific
        \\usepackage{listings}
        
        \\lstset{
            escapeinside={(*@}{@*)},
        }
        
        \\lstset{
            basicstyle=\\normalsize,
            columns=flexible,
            breaklines=true,
            language=SQL,
            showstringspaces=false,
            keepspaces=true,
            %aboveskip=0pt,
        }
        % end numprog specific
        
        \\begin{document}

    """
)
