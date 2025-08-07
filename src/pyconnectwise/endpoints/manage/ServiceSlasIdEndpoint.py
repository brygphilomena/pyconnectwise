from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdInfoEndpoint import ServiceSlasIdInfoEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdPrioritiesEndpoint import ServiceSlasIdPrioritiesEndpoint
from pyconnectwise.interfaces import IGettable
from pyconnectwise.models.manage import SLA
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceSlasIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SLA], ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[SLA])

        self.info = self._register_child_endpoint(ServiceSlasIdInfoEndpoint(client, parent_endpoint=self))
        self.priorities = self._register_child_endpoint(ServiceSlasIdPrioritiesEndpoint(client, parent_endpoint=self))

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[SLA]:
        """
        Performs a GET request against the /service/SLAs/{id}/priorities endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SLA]: The parsed response data.
        """
        return self._parse_one(SLA, super()._make_request("GET", data=data, params=params).json())
