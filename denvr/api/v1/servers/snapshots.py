from __future__ import annotations

from denvr.validate import validate_kwargs

from typing import TYPE_CHECKING, Any  # noqa: F401

if TYPE_CHECKING:
    from denvr.session import Session


class Client:
    def __init__(self, session: Session):
        self.session = session

    def get_snapshots(self, cluster: str | None = None) -> dict:
        """
        Get list of snapshots. ::

            client.get_snapshots(cluster="Cluster")

        Keyword Arguments:
            cluster (str):

        Returns:
            items (list):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {"Cluster": config.getkwarg("cluster", cluster)}
        }

        kwargs = validate_kwargs(
            "get", "/api/v1/servers/snapshots/GetSnapshots", parameters, {}
        )

        return self.session.request("get", "/api/v1/servers/snapshots/GetSnapshots", **kwargs)

    def get_snapshot(
        self, id: str | None = None, namespace: str | None = None, cluster: str | None = None
    ) -> dict:
        """
        Get detailed information on specific snapshot. ::

            client.get_snapshot(id="Id", namespace="Namespace", cluster="Cluster")

        Keyword Arguments:
            id (str): Name of snapshot
            namespace (str): The namespace/vpc.
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
            namespace (str):
            source_name (str):
            os_image (str):
            custom_package (str):
            root_disk_size (str):
            creation_date (str):
            username (str):
            tenancy_name (str):
            ready_to_use (bool):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Namespace": config.getkwarg("namespace", namespace),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "get",
            "/api/v1/servers/snapshots/GetSnapshot",
            parameters,
            {"Id", "Namespace", "Cluster"},
        )

        return self.session.request("get", "/api/v1/servers/snapshots/GetSnapshot", **kwargs)

    def create_snapshot(
        self,
        name: str | None = None,
        namespace: str | None = None,
        cluster: str | None = None,
        source_v_m_name: str | None = None,
    ) -> dict:
        """
        Create a new snapshot from an existing virtual machine. ::

            client.create_snapshot(
                name="string", namespace="string", cluster="string", source_v_m_name="string"
            )

        Keyword Arguments:
            name (str):
            namespace (str):
            cluster (str):
            source_v_m_name (str):

        Returns:
            id (str):
            namespace (str):
            source_name (str):
            os_image (str):
            custom_package (str):
            root_disk_size (str):
            creation_date (str):
            username (str):
            tenancy_name (str):
            ready_to_use (bool):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "json": {
                "name": config.getkwarg("name", name),
                "namespace": config.getkwarg("namespace", namespace),
                "cluster": config.getkwarg("cluster", cluster),
                "sourceVMName": config.getkwarg("source_v_m_name", source_v_m_name),
            }
        }

        kwargs = validate_kwargs(
            "post",
            "/api/v1/servers/snapshots/CreateSnapshot",
            parameters,
            {"cluster", "namespace"},
        )

        return self.session.request(
            "post", "/api/v1/servers/snapshots/CreateSnapshot", **kwargs
        )

    def delete_snapshot(
        self, id: str | None = None, namespace: str | None = None, cluster: str | None = None
    ) -> dict:
        """
        Delete snapshot. ::

            client.delete_snapshot(id="Id", namespace="Namespace", cluster="Cluster")

        Keyword Arguments:
            id (str): Name of snapshot
            namespace (str): The namespace/vpc.
            cluster (str): The cluster you're operating on

        Returns:
            id (str):
        """
        config = self.session.config  # noqa: F841

        parameters: dict[str, dict] = {
            "params": {
                "Id": config.getkwarg("id", id),
                "Namespace": config.getkwarg("namespace", namespace),
                "Cluster": config.getkwarg("cluster", cluster),
            }
        }

        kwargs = validate_kwargs(
            "delete",
            "/api/v1/servers/snapshots/DeleteSnapshot",
            parameters,
            {"Id", "Namespace", "Cluster"},
        )

        return self.session.request(
            "delete", "/api/v1/servers/snapshots/DeleteSnapshot", **kwargs
        )
