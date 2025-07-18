
class MtlsCertManagerCard extends HTMLElement {
  set hass(hass) {
    this.innerHTML = `
      <ha-card header="mTLS Zertifikate">
        <div class="card-content">
          <b>Neue CA erstellen</b><br>
          Name: <input id="ca_name"> <br>
          Subject: <input id="ca_subject" value="/CN=HomeCA"><br>
          <button onclick="createCA()">Erstellen</button><br><br>

          <b>Neues Zertifikat ausstellen</b><br>
          CA: <input id="cert_ca"> <br>
          Gerät: <input id="device_name"> <br>
          Tage: <input id="valid_days" value="365"> <br>
          Passwort: <input id="p12_password" type="password"><br>
          <button onclick="issueCert()">Ausstellen</button><br><br>

          <b>CRL generieren</b><br>
          CA: <input id="crl_ca"><br>
          <button onclick="genCrl()">Generieren</button><br><br>
        </div>
      </ha-card>
      <script>
        function createCA() {
          const ca = document.getElementById('ca_name').value;
          const subj = document.getElementById('ca_subject').value;
          fetch('/api/services/mtls_certmanager/create_ca', {
            method: 'POST', body: JSON.stringify({ ca_name: ca, subject: subj }),
            headers: {'Content-Type':'application/json'}
          });
        }
        function issueCert() {
          const ca = document.getElementById('cert_ca').value;
          const dev = document.getElementById('device_name').value;
          const days = parseInt(document.getElementById('valid_days').value);
          const pwd = document.getElementById('p12_password').value;
          fetch('/api/services/mtls_certmanager/issue_certificate', {
            method: 'POST',
            body: JSON.stringify({ ca_name: ca, device_name: dev, valid_days: days, p12_password: pwd }),
            headers: {'Content-Type':'application/json'}
          });
        }
        function genCrl() {
          const ca = document.getElementById('crl_ca').value;
          fetch('/api/services/mtls_certmanager/generate_crl', {
            method: 'POST',
            body: JSON.stringify({ ca_name: ca }),
            headers: {'Content-Type':'application/json'}
          });
        }
      </script>
    `;
  }
  setConfig(config) { this.config = config; }
  getCardSize() { return 3; }
}
customElements.define('mtls-certmanager-card', MtlsCertManagerCard);
