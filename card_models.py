import genanki

basic_model = genanki.Model(
    1559323000,
    'AnkiTUM Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Chapter'},
        {'name': "TUMLogo"}
    ],
    templates=[
        {
            'name': 'AnkiTUM Basic',
            'qfmt': '<img src=\"{{TUMLogo}}\"> {{Front}}',
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
        
    """
)

cloze_model = genanki.Model(
  340857584,
  'AnkiTUM Cloze',
  model_type=genanki.Model.CLOZE,
  fields=[
    {'name': 'Front'},
    {'name': 'Chapter'},
    {'name': "TUMLogo"}
  ],
  templates=[
    {
      'name': 'Cloze',
      'qfmt': '{{cloze:Text}}',
      'afmt': '{{cloze:Text}}<br>\n{{Back Extra}}',
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
  """
)
