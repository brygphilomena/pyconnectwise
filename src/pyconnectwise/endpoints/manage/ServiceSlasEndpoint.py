from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasIdEndpoint import ServiceSlasIdEndpoint
from pyconnectwise.endpoints.manage.ServiceSlasInfoEndpoint import ServiceSlasInfoEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable
from pyconnectwise.models.manage import SLA
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceSlasEndpoint(
    ConnectWiseEndpoint,
    IGettable[SLA, ConnectWiseManageRequestParams],
    IPaginateable[SLA, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "slas", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, SLA)
        IPaginateable.__init__(self, SLA)

        self.info = self._register_child_endpoint(ServiceSlasInfoEndpoint(client, parent_endpoint=self))

    def id(self, _id: int) -> ServiceSlasIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSlasIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ServiceSlasIdEndpoint: The initialized ServiceSlasIdEndpoint object.
        """
        child = ServiceSlasIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[SLA]:
        """
        Performs a GET request against the /service/slas/{id}/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SLA]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), SLA, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> SLA:
        """
        Performs a GET request against the /service/slas/{id}/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SLA: The parsed response data.
        """
        return self._parse_many(SLA, super()._make_request("GET", data=data, params=params).json())
