# Strade di Trento colorate in base al prefisso

Basato sulle seguenti idee:

- [Madrid's roads, colored by designation](https://www.reddit.com/r/DataArt/comments/d7rqbb/madrids_roads_colored_by_designation/)
- [Coloring Milan's streets by prefix](https://www.reddit.com/r/dataisbeautiful/comments/d7eq0q/coloring_milans_streets_by_prefix_oc/)

Requisiti:

- [Stradario del comune di Trento](https://dati.trentino.it/dataset/stradario-open-data), file in formato `.gml`
- [qgis](https://qgis.org/en/site/) per visualizzare i dati
- Python

Nota: ho omesso molti prefissi. La lista completa è:

```
[Prefisso]: [Occorrenze]
VIA: 4186
PIAZZA: 243
VIALE: 74
PIAZZETTA: 23
VICOLO: 69
LOCALITA: 88
SALITA: 47
STRADA: 348
P.ZZA: 16
LARGO: 39
GIARDINO: 51
CORSO: 34
LUNGADIGE: 26
VIC.: 8
L.GO: 4
TANGENZIALE: 123
PIAZZALE: 25
I: 2
PASSEGGIATA: 4
RIONE: 11
VIGOLO: 1
V.: 5
MONTEVIDEO: 1
MAGNETE: 1
BIG: 1
SAN: 4
LOCALITA: 4
ANDRONA: 4
PASSAGGIO: 15
BOSCO: 1
STR.: 17
II: 1
TRIDENTE: 1
PONTE: 18
COSTA: 1
PARCO: 6
FINESTRA: 1
MILLENNIUM: 1
MARNIGHE: 1
CENTRO: 1
SPONDA: 8
RACCORDO: 7
P.TTA: 7
CORALLO: 1
MASO: 2
CELVA: 1
MORONAR: 1
CIMA: 1
P.GGIO: 4
POVO: 1
CRISTO: 1
BRUSAFER: 1
GALLERIA: 4
SANTA: 1
BREN: 1
LE: 1
NORD: 1
LUNGAVISIO: 2
BELVEDERE: 1
DOS: 1
PAVIONE: 1
PZ.: 7
CAMPRA: 1
TOP: 1
PORTAQUILA: 1
BOLGHERA: 1
GALL.: 1
VILLAZZANO: 2
ZONA: 2
S.: 1
P.LE: 1
SANTANNA: 1
SOTTOPORTICO: 1
BELLEVUE: 1
PORTICO: 1
```

