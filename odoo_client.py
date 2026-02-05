# odoo_client.py
import xmlrpc.client
import logging
import os
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OdooClient:
    def __init__(
        self,
        url=os.getenv("ODOO_URL"),
        db=os.getenv("ODOO_DATABASE"),
        username=os.getenv("USERNAME_OR_EMAIL"),
        api_key=os.getenv("API_KEY_FROM_ODOO"),
    ):
        self.url = url.rstrip("/")
        self.db = db
        self.username = username
        self.api_key = api_key

        # allow_none=True para evitar errores al serializar valores nulos
        self.common = xmlrpc.client.ServerProxy(
            f"{self.url}/xmlrpc/2/common",
            allow_none=True
        )
        self.models = xmlrpc.client.ServerProxy(
            f"{self.url}/xmlrpc/2/object",
            allow_none=True
        )

        self.uid = self.authenticate()

    def authenticate(self):
        uid = self.common.authenticate(
            self.db,
            self.username,
            self.api_key,
            {}
        )
        if not uid:
            raise Exception("Autenticación fallida en Odoo")
        return uid

    def _clean_kwargs(self, kwargs):
        """
        Remove None values from kwargs recursively (only top-level keys used).
        XML-RPC cannot marshal None in many positions.
        """
        if not kwargs:
            return {}
        return {k: v for k, v in kwargs.items() if v is not None}

    def execute(self, model, method, *args, **kwargs):
        """
        Central point to call execute_kw. Cleans kwargs so no None is sent.
        """
        cleaned = self._clean_kwargs(kwargs)
        # DEBUG: descomentar para ver exactamente qué se envía (útil solo en desarrollo)
        logger.debug("RPC CALL -> model=%s method=%s args=%s kwargs=%s", model, method, args, cleaned)
        return self.models.execute_kw(
            self.db,
            self.uid,
            self.api_key,
            model,
            method,
            args,
            cleaned
        )

    def search(self, model, domain):
        return self.execute(model, "search", domain)

    def read(self, model, ids, fields=None):
        kwargs = {}
        if fields:
            kwargs["fields"] = fields

        return self.execute(
            model,
            "read",
            [ids],
            **kwargs
        )

    def search_read(self, model, domain, fields=None, limit=None, offset=None):
        """
        Wrapper safe para search_read:
        - solo incluye keys si no son None
        - evita enviar 'fields': None u otras claves con valor None
        """
        kwargs = {}
        if fields:
            kwargs["fields"] = fields
        if limit is not None:
            kwargs["limit"] = limit
        if offset is not None and offset != 0:
            kwargs["offset"] = offset

        return self.execute(
            model,
            "search_read",
            domain,
            **kwargs
        )
