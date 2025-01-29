Deel 1 opdr 3:
Schrijf een programma waarmee je een PDF kunt genereren. 

Het programma moet als volgt werken: 

De gebruiker voert via de commandline (input) een stukje tekst in. (bijv.: 'Hallo, dit is mijn eerste PDF’)
Het programma genereert een PDF ter grootte van 1 A4tje, volledig wit met de tekst die is ingevoerd.
De PDF word opgeslagen in de map: PDF_INVOICE

Deel 2 opdr 1:
Maak (via een Python programma) een PDF die er net zo uit ziet als je ontwerp maar zonder data (dus factuurregels en bedragen).

Deze PDF moet dan opgeslagen worden in de map PDF_INVOICE.

Deel 2 opdr 2: 
Maak een programma die de JSON uitleest en de relevante data voor je factuur in een ander JSON bestand opslaat.

Let hierbij op de volgende dingen:

Een order is nog geen factuur. Je zult dus dingen moeten uitrekenen/ toevoegen.
Dit betreft dummy data en er kunnen dus onrealistische gegevens in voorkomen. Trek je daar niets van aan een programma wat met onrealistische data kan werken kan dat ook met echte data!
Kijk ook eens naar: Btw-bedrag afronden (belastingdienst.nl)

Deel 3 opdr 1:
Met de code uit het vorige deel ga je nu de pdf vullen met de gegenereerde JSON factuur.

Alle data is al verzameld het enige is dat het nog op de juiste plek moet komen.

Als het blijkt dat het factuur JSON bestand variabelen/gegevens mist dat dan moet je natuurlijk je programma aanpassen voordat je door gaat. Dit is niet erg, want dat ga je in de praktijk ook tegenkomen, soms moet je terug in het proces en niet door modderen!

Deel 3 opdr 2:
Maak drie mappen aan op de plek waar je Python programma staat:

JSON_ORDER
JSON_PROCESSED
JSON_INVOICE
Plaats de inhoud van de bijgeleverde zip in JSON_ORDER

 

Programmeer nu het volgende:

Haal alle bestanden in de map JSON_ORDER op
Genereer voor ieder bestand (met de code die je al hebt gemaakt) een factuur JSON en sla deze op in JSON_INVOICE.
Verplaatst de verwerkte order JSON naar JSON_PROCESSED

Deel 4 opdr 1:
Het laatste onderdeel van je programma is het bulk genereren van PDF’s vanuit order JSON bestanden. We hebben voor je een hele stapel orders toegevoed aan deze opdracht.

Hergebruik hiervoor zoveel mogelijk code die al geschreven is.

Mocht je een fout in een order bestand tegenkomen sla deze dan op in een nieuwe map genaamd: JSON_ORDER_ERROR

Deel 4 opdr 2:
Je maakt een presentatie van minimaal 5 en maximaal 15 minuten met daarin minimaal de volgende onderwerpen:

Stukjes code waar jullie trots op zijn
De libraries die je hebt gebruikt en waarom
Een korte demo van het project
