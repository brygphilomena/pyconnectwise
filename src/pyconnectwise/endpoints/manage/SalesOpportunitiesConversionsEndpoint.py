from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesConversionsIdEndpoint import (
    SalesOpportunitiesConversionsIdEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class SalesOpportunitiesConversionsEndpoint(
    ConnectWiseEndpoint,
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "conversions", parent_endpoint=parent_endpoint)

    def id(self, _id: int) -> SalesOpportunitiesConversionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SalesOpportunitiesConversionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            SalesOpportunitiesConversionsIdEndpoint: The initialized SalesOpportunitiesConversionsIdEndpoint object.
        """
        child = SalesOpportunitiesConversionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
