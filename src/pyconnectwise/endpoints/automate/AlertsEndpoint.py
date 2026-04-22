from pyconnectwise.endpoints.automate.AlertsIdEndpoint import AlertsIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import AutomateAlert
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class AlertsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateAlert], ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateAlert, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "Alerts", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[AutomateAlert])
        IPaginateable.__init__(self, AutomateAlert)

    def id(self, id: int) -> AlertsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized AlertsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            AlertsIdEndpoint: The initialized AlertsIdEndpoint object.
        """
        child = AlertsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateAlert]:
        """
        Performs a GET request against the /Alerts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateAlert]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateAlert,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateAlert]:
        """
        Performs a GET request against the /Alerts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateAlert]: The parsed response data.
        """
        return self._parse_many(
            AutomateAlert,
            super()._make_request("GET", data=data, params=params).json(),
        )
