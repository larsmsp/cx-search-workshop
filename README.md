# Computas' workshop for søkemotor på GCP

En workshop for å lage backend til en enkel søkemotor til Computas.com, kjørende på Google Cloud Platform.

# Oppgaver

## Introduksjon

Første oppgave skal gjøre studenten kjent med Python, web-rammeverket Flask og hvordan man ruller ut versjoner
til Google App Engine Standard. Man skal lage et enkelt endepunkt som viser "Hello, World!" og en enkel kalkulator.

1. Endre metoden `hello_world` til å returnere "Hello, World!". \
Kan testes lokalt ved å kjøre `python main.py` og gå til [localhost:5000](http://localhost:5000) i nettleseren.

2. Fullfør metoden `calculator` til å gjøre riktig operasjon på operandene etter hvilken verdi `operator` har:
   * `plus`: Addere
   * `minus`: Subtrahere
   * `mult`: Multiplisere
   * `div`: Divisjon
   
   Kan testes lokalt ved å kjøre `python main.py` og gå til 
   [localhost:5000?operand1=1&operand2=5&operator=plus](http://localhost:5000?operand1=1&operand2=5&operator=plus) 
   i nettleseren.
   
3. Rulle ut versjonen til Google Cloud Platform.
   * Endre service-navn i filen `app.yaml`
   * Rulle ut ved å kjøre `gcloud app deploy` fra kommandolinjen
   
   Versjonen vil være synlig på `https://<ditt-servicenavn>-dot-sinuous-tine-156112.appspot.com`.

## Søkemotor
