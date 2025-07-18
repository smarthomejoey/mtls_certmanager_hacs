from homeassistant import config_entries

class MtlsCertManagerFlowHandler(config_entries.ConfigFlow, domain="mtls_certmanager"):
    async def async_step_user(self, user_input=None):
        return self.async_create_entry(title="mTLS Cert Manager", data={})
