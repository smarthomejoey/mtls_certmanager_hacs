
import logging
from homeassistant.core import HomeAssistant, ServiceCall

from . import api

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: dict):
    async def handle_create_ca(call: ServiceCall):
        ca_name = call.data.get("ca_name")
        subject = call.data.get("subject")
        path = api.create_ca(ca_name, subject)
        _LOGGER.info(f"CA created at {path}")

    async def handle_issue_cert(call: ServiceCall):
        ca_name = call.data.get("ca_name")
        device_name = call.data.get("device_name")
        valid_days = call.data.get("valid_days", 365)
        p12_password = call.data.get("p12_password")
        path = api.issue_certificate(ca_name, device_name, valid_days, p12_password)
        _LOGGER.info(f"Cert created at {path}")

    async def handle_revoke(call: ServiceCall):
        ca_name = call.data.get("ca_name")
        device_name = call.data.get("device_name")
        api.revoke_certificate(ca_name, device_name)
        _LOGGER.info(f"Cert revoked: {device_name}")

    async def handle_crl(call: ServiceCall):
        ca_name = call.data.get("ca_name")
        crl = api.generate_crl(ca_name)
        _LOGGER.info(f"New CRL generated at {crl}")

    hass.services.async_register("mtls_certmanager", "create_ca", handle_create_ca)
    hass.services.async_register("mtls_certmanager", "issue_certificate", handle_issue_cert)
    hass.services.async_register("mtls_certmanager", "revoke_certificate", handle_revoke)
    hass.services.async_register("mtls_certmanager", "generate_crl", handle_crl)

    return True
