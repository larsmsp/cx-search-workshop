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

## Frontend til søkemotor

I andre oppgave skal studenten rulle ut frontend til søkeapplikasjonen. Denne kan brukes for å teste søkeendepunktet som 
lages i siste oppgave.

1. Rulle ut versjonen til Google Cloud Platform.
   * Endre service-navn i filen `app.yaml`
   * Rulle ut ut ved å kjøre `gcloud app deploy` fra kommandolinjen
   
   Versjonen vil være synlig på `https://<ditt-servicenavn>-dot-sinuous-tine-156112.appspot.com`.
   
## Endepunkt for søk

Tredje oppgave skal knytte søkeindeksen i Google Cloud Platform til frontend. Studentene skal lage et
søkeendepunkt som spør og henter resultat fra indeksen.

Metoden skal ligge på endepunktet `/search`og lese query-parameteret `q`, 
f.eks. `www.minsøkemotor.com/search?q=Computas`. 

1. Skriv koden som leser query-parameteret `q`, henter resultatet fra Google Cloud Platform og returnerer det til brukeren.
   * Query-parameter kan leses ved å kalle `request.args['parameter-navn]`
   * Det finnes en hjelpeklasse `Document`som kan brukes for å utføre søk. Denne må derimot utvides noe:
       * Feltene `ID`, `TITLE`, `URL` og `CONTENTS` må gis riktige verdier. 
       Verdiene på disse er synlige i Google Cloud Platform-konsollet under App Engine\Search.
       * `search`-metoden må endres slik at den kaller riktige metoder for å fylle inn søkeresultatene som
       skal returneres.
2. Rulle ut versjonen til Google Cloud Platform.
   * Endre service-navn i filen `app.yaml`
   * Rulle ut ut ved å kjøre `gcloud app deploy` fra kommandolinjen
3. Test søkemotoren ved å gå til `https://<ditt-servicenavn>-dot-sinuous-tine-156112.appspot.com` og søke
etter noe du tror eller vet står på hjemmesiden til Computas. 