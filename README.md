
# mTLS Cert Manager (Custom Component)

Verwalte mTLS Client-Zertifikate direkt in Home Assistant.

## Funktionen
✅ Eigene CA erstellen (10 Jahre)  
✅ Client-Zertifikate ausstellen (.crt, .key, .p12)  
✅ CRL generieren & Widerruf  
✅ Lovelace Card zum Steuern

## Installation
1. Kopiere `custom_components/mtls_certmanager/` nach `/config/custom_components/`
2. Kopiere `mtls_certmanager.js` nach `/config/www/`
3. `configuration.yaml` → optional Panel:
```yaml
panel_custom:
  - name: mtls_certmanager
    sidebar_title: "mTLS Zertifikate"
    sidebar_icon: "mdi:certificate"
    url_path: mtls_certmanager
    config: {}
```
4. Lovelace Card:
```yaml
type: 'custom:mtls-certmanager-card'
```

## Alle Zertifikate werden unter `/config/ssl-ca/` gespeichert.
