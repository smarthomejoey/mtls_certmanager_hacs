
import subprocess
from pathlib import Path

BASE_PATH = Path("/config/ssl-ca")

def create_ca(ca_name, subject):
    ca_path = BASE_PATH / ca_name
    ca_path.mkdir(parents=True, exist_ok=True)

    subprocess.run(["openssl", "genrsa", "-out", f"{ca_path}/ca.key", "4096"], check=True)
    subprocess.run(["openssl", "req", "-x509", "-new", "-nodes",
        "-key", f"{ca_path}/ca.key", "-sha256", "-days", "3650",
        "-subj", subject, "-out", f"{ca_path}/ca.crt"], check=True)

    (ca_path / "index.txt").touch()
    (ca_path / "serial").write_text("1000\n")

    return str(ca_path)

def issue_certificate(ca_name, device_name, valid_days, p12_password):
    ca_path = BASE_PATH / ca_name
    device_path = ca_path / device_name
    device_path.mkdir(parents=True, exist_ok=True)

    subprocess.run(["openssl", "genrsa", "-out", f"{device_path}/client.key", "2048"], check=True)
    subprocess.run(["openssl", "req", "-new", "-key", f"{device_path}/client.key",
        "-out", f"{device_path}/client.csr", "-subj", f"/CN={device_name}"], check=True)
    subprocess.run(["openssl", "x509", "-req", "-in", f"{device_path}/client.csr",
        "-CA", f"{ca_path}/ca.crt", "-CAkey", f"{ca_path}/ca.key", "-CAcreateserial",
        "-out", f"{device_path}/client.crt", "-days", str(valid_days), "-sha256"], check=True)
    subprocess.run(["openssl", "pkcs12", "-export", "-inkey", f"{device_path}/client.key",
        "-in", f"{device_path}/client.crt", "-out", f"{device_path}/client.p12",
        "-passout", f"pass:{p12_password}"], check=True)

    return str(device_path)

def revoke_certificate(ca_name, device_name):
    ca_path = BASE_PATH / ca_name
    device_path = ca_path / device_name

    subprocess.run(["openssl", "ca", "-revoke", f"{device_path}/client.crt",
        "-keyfile", f"{ca_path}/ca.key", "-cert", f"{ca_path}/ca.crt",
        "-config", "/etc/ssl/openssl.cnf"], check=True)

    return True

def generate_crl(ca_name):
    ca_path = BASE_PATH / ca_name
    crl_path = ca_path / "ca.crl"

    subprocess.run(["openssl", "ca", "-gencrl", "-out", str(crl_path),
        "-keyfile", f"{ca_path}/ca.key", "-cert", f"{ca_path}/ca.crt",
        "-config", "/etc/ssl/openssl.cnf"], check=True)

    return str(crl_path)
