# mtls_certmanager
Home Assistant Integration zum Erstellen von CA & Client-Zertifikaten für mTLS und automatischem Sync zur Nginx Proxy Manager Instanz per SSH.

## Funktionen
- Eigene CA generieren (10 Jahre)
- Client-Zertifikate ausstellen
- CRL verwalten
- Service: sync_ca → überträgt ca.crt + ca.crl per SSH und startet NPM neu

## Installation
1. Repository in HACS hinzufügen
2. Integration installieren
3. In Home Assistant konfigurieren (NPM Host, User, Passwort, Zielpfad)

## Verwendung
service: mtls_certmanager.sync_ca
data:
  npm_host: "192.168.1.10"
  user: "user"
  password: "supersecure"
  remote_path: "/data/ssl"
