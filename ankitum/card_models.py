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
                    
                    <div class="logo">
                       <!-- {{Logo}}-->
                       <h2>ankiTUM</h2>
                    </div> 
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
        
        .logo {
            font-size: 20px;
            font-weight: bold;
            color: #1b5aab;
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
    {'name': 'Chapter'},
    {'name': 'Logo'}
  ],
  templates=[
    {
      'name': 'Cloze',
      'qfmt': """    
            <div class="card">
                <div class="card-header">
                    <div class="chapter-title">{{Chapter}}</div>
                    <div class="logo">
                        {{Logo}}
                    </div> 
                </div>
                        
                <div class="card-text">
                    {{cloze:Front}}
                </div>
            </div>
            """,
      'afmt': """       
      <div class="card">
            <div class="card-header">
                <div class="chapter-title">{{Chapter}}</div>
                <div class="logo">
                   <!-- {{Logo}}-->
                   <h3 style="color: blue; font-weight: bold;">ankiTUM</h2>
                </div> 
            </div>
                    
            <div class="card-text">
                {{cloze:Front}}
            </div>
        </div>
        """
    },
  ],
  css="""
        .card {
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
            font-size: 20px;
            font-weight: bold;
            color: #1b5aab;
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
