import genanki

basic_model = genanki.Model(
    1559323000,
    'AnkiTUM Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Chapter'}
    ],
    templates=[
        {
            'name': 'AnkiTUM Basic',
            'qfmt': """       
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                    <img src="tum_logo.png" alt="Logo" class="logo">
                </div>
                        
                <div class="card-text">
                    {{Front}}
                </div>
            """,
            'afmt': '{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}',
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
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .logo {
            max-height: 50px; /* Adjust the height of your logo */
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
                    <img src="tum_logo.png" alt="Logo" class="logo">
                </div>
                        
                <div class="card-text">
                    {{cloze:Front}}
                </div>
            """,
      'afmt': """       
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                    <img src="{{TUMLogo}}" {{Front}}" alt="Logo" class="logo">
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
        .logo {
            max-height: 50px; /* Adjust the height of your logo */
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
