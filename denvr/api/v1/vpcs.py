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

    def get_vpc(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Get detailed information about a specific VPC ::

            client.get_vpc(id="Id", cluster="Msc1")

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            name (str):
            cluster (str):
            tenancy_name (str):
            ip_range (str):
            created_at (str):
            block_intra_vpc_comms (bool):
            is_default (bool):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs("get", "/api/v1/vpcs/GetVpc", parameters, {"Id", "Cluster"})

        return self.session.request("get", "/api/v1/vpcs/GetVpc", **kwargs)

    def create_vpc(
        self,
        name: str | None = None,
        block_intra_vpc_comms: bool | None = None,
        is_default: bool | None = None,
        cluster: str | None = None,
    ) -> dict:
        """
        Create a new VPC ::

            client.create_vpc(name="string", block_intra_vpc_comms=False, is_default=False, cluster="Msc1")

        Keyword Arguments:
            name (str): name of the VPC. should start with {tenancyName}-  in case of creating default VPC, name should...
            block_intra_vpc_comms (bool): if set to true, this VPC will block any intra-VPC communications if ommited, default is false
            is_default (bool): if set to true, this VPC will be the default VPC for the cluster only one VPC can be default per...
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            name (str):
            cluster (str):
            tenancy_name (str):
            ip_range (str):
            created_at (str):
            block_intra_vpc_comms (bool):
            is_default (bool):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "name": config.getkwarg("name", name),
                "blockIntraVpcComms": config.getkwarg(
                    "block_intra_vpc_comms", block_intra_vpc_comms
                ),
                "isDefault": config.getkwarg("is_default", is_default),
                "cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "post", "/api/v1/vpcs/CreateVpc", parameters, {"cluster", "name"}
        )

        return self.session.request("post", "/api/v1/vpcs/CreateVpc", **kwargs)

    def destroy_vpc(self, id: str | None = None, cluster: str | None = None) -> dict:
        """
        Destroy a VPC ::

            client.destroy_vpc(id="Id", cluster="Msc1")

        Keyword Arguments:
            id (str): Unique identifier for a resource within the cluster
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            name (str):
            cluster (str):
            tenancy_name (str):
            ip_range (str):
            created_at (str):
            block_intra_vpc_comms (bool):
            is_default (bool):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "delete", "/api/v1/vpcs/DestroyVpc", parameters, {"Id", "Cluster"}
        )

        return self.session.request("delete", "/api/v1/vpcs/DestroyVpc", **kwargs)
