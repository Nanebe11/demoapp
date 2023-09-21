from viktor.parametrization import (
    ViktorParametrization,
    NumberField, 
    IntegerField,
    OptionField,
    Text,
    Step,
    Lookup,
)

#def get_Jahresenergiebedarf(params, **kwargs):
  #if params.step_1.GA == "Neubau" or "Sanierung" :
       # GA = 45
  #if params.step_1.GA == "Bestandsgebäude" :
   #     GA = 100
      
 # Heizwärmebedarf = GA * params.step_1.Wf,
#
 #if params.step_1.WE<3:
#      BedarfTWW = 500 * params.step_1.Pers
 # i#f params.step_1.WE>2:   
  #      BedarfTWW = 1000 * params.step_1.WE

  #Jahresenergiebedarf == Heizwärmebedarf + BedarfTWW  
  #return param.Jahresenergiebedarf


class Parametrization(ViktorParametrization):

  step_1 = Step("Start", views="get_image_view")

  step_1.text1 = Text (
    """ Welcome! 

    This is my Masterthesis

    I hope we can get along
    
    User Information

    XXXX
    
    Enter your input
    """
  )

  step_1.GA = OptionField(
    "Gebäudeart", 
    options=['Neubau', 'Sanierung', 'Bestandsgebäude'], 
    variant='radio-inline'
  ) 

  step_1.WE = IntegerField(
    "Anzahl Wohneinheiten", 
    suffix="WE",
    default=1,
    min=1,
    max=10,
    description="Anzahl der getrennt lebenden Haushalte in einem Gebäude mit gemeinsamer Warmwassererzeugung und Heizungsanlage",
    )

  if Lookup('step_1.WE') == 1 or 2:
    step_1.Pers = IntegerField( #dieses Feld ist nur erforderlich für WE>2 
    "Anzahl Personen", 
    suffix="Personen",
    default=1,
    min=1,
    max=6,
    description="Anzahl der Personen, die in dem Gebäude leben",
    )
  
  step_1.Wf = NumberField(
    "Wohnfläche", 
    suffix="m2", 
    min=5,
    description="Zusammengerechnete beheizte Wohnfläche alle Wohneinheiten"
  )

  step_1.text2 = Text("""
  
  Bitte geben Sie im folgenden die Art der aktuellen Wärmeerzeugung an. 
  Diese Information wird berücksichtigt, um die ökologischen Kennzahlen zu berechnen. 
  Dabei werden die Auswirkungen eines Gebäudes mit BIPV(T)-Anlage mit denen eines Vergleichsgebäudes verglichen.
  """)

  step_1.Wä = OptionField(
    "aktuelle Wärmeerzeugung",
    options=["Erdgas", "Heizöl"],
    default="Erdgas",
    variant='radio-inline',
    description="Bei Neubauten bitte alternative Wärmeerzeugung wählen (Vergleichswert)",
  )

  step_1.Energiebedarf = NumberField(
    "Jahresenergiebedarf",
    suffix="kWh",
   # default= get_Jahresenergiebedarf,
    description="Kann beispielsweise aus dem Energieausweis abgelesen werden"
  )
  
  step_2 = Step("Anlagenkonfiguration", views=["get_image2_view","get_Erträge_view", "get_Energie_view"])

  step_2.text3 = Text (
    """ Here are going to be more Inputs necessary"""
  )

  step_2.textA1 = Text ("BIPV-Anlage Dachintegriert")

  step_2.Area1 = NumberField(
    "Fläche der PV-Anlage", 
    suffix="m2", 
    min=1,
    max=500,
  )

  step_2.Azimut1 = OptionField(
    "Ausrichtung der Fläche", 
    options=["Nord", "Nord-Ost", "Ost", "Süd-Ost", "Süd", "Süd-West", "West", "Nord-West"], 
    default="Süd", 
  )

  step_2.Neigung1 = OptionField(
    "Neigung der Fläche",
    options=["5°","25°","35°","45°","55°","70°","90°"], 
    default="35°",
    description="Die nächstmögliche Neigung wählen, für Flachdächer 5°", 
  )

  step_2.textA2 = Text ("BIPVT-Anlage Dachintegriert")

  step_2.Area2 = NumberField(
    "Fläche der PVT-Anlage", 
    suffix="m2", 
    min=1,
    max=500,
  )

  step_2.Azimut2 = OptionField(
    "Ausrichtung der Fläche", 
    options=["Nord", "Nord-Ost", "Ost", "Süd-Ost", "Süd", "Süd-West", "West", "Nord-West"], 
    default="Süd", 
  )

  step_2.Neigung2 = OptionField(
    "Neigung der Fläche",
    options=["5°","25°","35°","45°","55°","70°","90°"], 
    default="35°",
    description="Die nächstmögliche Neigung wählen, für Flachdächer 5°", 
  )

  step_2.textA3 = Text ("BIPV-Anlage Fassadenintegriert")

  step_2.Area3 = NumberField(
    "Fläche der PV-Anlage", 
    suffix="m2", 
    min=1,
    max=500,
  )

  step_2.Azimut3 = OptionField(
    "Ausrichtung der Fläche", 
    options=["Nord", "Nord-Ost", "Ost", "Süd-Ost", "Süd", "Süd-West", "West", "Nord-West"], 
    default="Süd", 
  )

  step_2.textA4 = Text ("BIPVT-Anlage Fassadenintegriert")

  step_2.Area4 = NumberField(
    "Fläche der PV-Anlage", 
    suffix="m2", 
    min=1,
    max=500,
  )

  step_2.Azimut4 = OptionField(
    "Ausrichtung der Fläche", 
    options=["Nord", "Nord-Ost", "Ost", "Süd-Ost", "Süd", "Süd-West", "West", "Nord-West"], 
    default="Süd", 
  )

  step_2.Speicher = OptionField(
    "Anlage mit Stromspeicher",
    options=["Mit Stromspeicher","ohne Stromspeicher"], 
    variant='radio-inline',
    description="Durch einen Stromspeicher kann ein höherer Anteil des produzierten Stroms verwendet werden (vgl. Lastmanagement)",
  )
  
  step_2.Inbetrieb = OptionField(
    "Inbetriebnahme-Zeitpunkt der Anlage", 
    options=["bis 31.01.2024", "ab 01.02.2024", "ab 01.08.2024", "ab 01.02.2025", "ab 01.08.2025", "ab 01.02.2026"], 
    default="bis 31.01.2024",
  )

  step_3 = Step("Summary",views=["get_plotly_view", "get_image_view"])

  step_3.text4 = Text (
    """ Hi, 
    this is the summary,
    I hope you got all the information you needed to make a solid decision!
    
    Thanks for using this tool""")
