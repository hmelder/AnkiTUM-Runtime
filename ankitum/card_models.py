import genanki

basic_model = genanki.Model(
    1559323000,
    'AnkiTUM Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Chapter'},
        {'name': 'Logo'}
    ],
    templates=[
        {
            'name': 'AnkiTUM Basic',
            'qfmt': """     
                <meta charset="UTF-8">
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                </div>
                        
                <div class="card-text">
                    {{Front}}
                </div>
            """,
            'afmt': """
            <meta charset="UTF-8">
            {{FrontSide}}
            <hr id=answer>
            <div class="card-text">
                {{Back}}
            </div>
            """,
        },
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 35px;
            text-align: center;
            color: black;
            background-color: white;
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .chapter-title {
            font-size: 18px;
            font-weight: bold;
            color: grey;
        }
        .separator {
            border-top: 1px solid #ccc;
            margin-bottom: 10px;
        }
        .card-text {
            font-size: 16px;
        }
    """
)

cloze_model = genanki.Model(
  340857584,
  'AnkiTUM Cloze',
  model_type=genanki.Model.CLOZE,
  fields=[
    {'name': 'Front'},
    {'name': 'Chapter'}
  ],
  templates=[
    {
      'name': 'Cloze',
      'qfmt': """       
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                </div>
                        
                <div class="card-text">
                    {{cloze:Front}}
                </div>
            """,
      'afmt': """       
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                </div>
                        
                <div class="card-text">
                    {{cloze:Front}}
                </div>
            """
    },
  ],
  css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        
        .cloze {
            font-weight: bold;
            color: blue;
        }
        
                .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .chapter-title {
            font-size: 18px;
            font-weight: bold;
            color: grey;
        }
        .separator {
            border-top: 1px solid #ccc;
            margin-bottom: 10px;
        }
        .card-text {
            font-size: 16px;
        }
  """
)

latex_plus = genanki.Model(
    58399521800,
    'AnkiTUM Latex+',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Chapter'},
        {'name': 'Logo'}
    ],
    templates=[
        {
            'name': 'AnkiTUM Latex+',
            'qfmt': """     
                <meta charset="UTF-8">
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                </div>

                <div class="card-text">
                    {{Front}}
                </div>
            """,
            'afmt': """
            <meta charset="UTF-8">
            {{FrontSide}}
            <hr id=answer>
            <div class="card-text">
                {{Back}}
            </div>
            """,
        },
    ],
    css="""
        .card {
            font-family: arial;
            font-size: 35px;
            text-align: center;
            color: black;
            background-color: white;
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .chapter-title {
            font-size: 18px;
            font-weight: bold;
            color: grey;
        }
        .separator {
            border-top: 1px solid #ccc;
            margin-bottom: 10px;
        }
        .card-text {
            font-size: 16px;
        }
    """,
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
