from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING, Any  # noqa: F401

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_vpcs(self, cluster: str | None = None) -> dict:
        """
        Get a list of VPCs ::

            client.get_vpcs(cluster="cluster")

        Keyword Arguments:
            cluster (str):

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {"cluster": config.getkwarg("cluster", cluster)}
        }

        kwargs = validate_kwargs("get", "/api/v1/vpcs/GetVpcs", parameters, {})

        return self.session.request("get", "/api/v1/vpcs/GetVpcs", **kwargs)
