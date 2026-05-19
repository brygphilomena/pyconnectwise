from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IGettable
from pyconnectwise.models.manage import OpportunityConversion
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesOpportunitiesConversionsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[OpportunityConversion, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, OpportunityConversion)

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> OpportunityConversion:
        """
        Performs a GET request against the /sales/opportunities/conversions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            OpportunityConversions: The parsed response data.
        """
        return self._parse_many(OpportunityConversion, super()._make_request("GET", data=data, params=params).json())
