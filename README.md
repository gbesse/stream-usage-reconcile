# stream-usage-reconcile

## Français

Réconcilier les consommations cumulées et les deltas de flux.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m stream_usage_reconcile examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Sépare compteurs cumulés et incréments, déduplique par identifiant et conserve un total inconnu pour flux incomplets ou contradictoires. Le témoin naïf expose le double comptage.

### Limites

Traces normalisées, un seul compteur de jetons par flux ; identifiants et mode fournis par collecteur. Ne rapproche pas des factures fournisseur ni les flux représentant le même appel.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Reconcile cumulative usage and streaming deltas.

Synthetic data; no network access or secret required.

```sh
python -m stream_usage_reconcile examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Separates cumulative counters and deltas, deduplicates by ID and preserves unknown totals for incomplete or contradictory streams. Naive witness exposes double counting.

### Limits

Normalized traces, one token counter per stream; collector supplies IDs and mode. Does not reconcile provider invoices or streams representing the same call.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Conciliar consumo acumulado y deltas de flujo.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m stream_usage_reconcile examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Separa contadores acumulados y deltas, deduplica por ID y conserva total desconocido para flujos incompletos o contradictorios. Testigo ingenuo expone doble conteo.

### Límites

Trazas normalizadas, un contador de tokens por flujo; colector aporta ID y modo. No concilia facturas de proveedor ni flujos del mismo llamado.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/yetone/magpie/issues/1874
