# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ReservationOrderOperations:
    """ReservationOrderOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure_reservation_api.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def calculate(
        self,
        body: "models.PurchaseRequest",
        **kwargs
    ) -> "models.CalculatePriceResponse":
        """Calculate price for a ``ReservationOrder``.

        Calculate price for placing a ``ReservationOrder``.

        :param body: Information needed for calculate or purchase reservation.
        :type body: ~azure_reservation_api.models.PurchaseRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CalculatePriceResponse, or the result of cls(response)
        :rtype: ~azure_reservation_api.models.CalculatePriceResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CalculatePriceResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.calculate.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PurchaseRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CalculatePriceResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    calculate.metadata = {'url': '/providers/Microsoft.Capacity/calculatePrice'}  # type: ignore

    def list(
        self,
        **kwargs
    ) -> AsyncIterable["models.ReservationOrderList"]:
        """Get all ``ReservationOrder``\ s.

        List of all the ``ReservationOrder``\ s that the user has access to in the current tenant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ReservationOrderList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure_reservation_api.models.ReservationOrderList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReservationOrderList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('ReservationOrderList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.Error, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/Microsoft.Capacity/reservationOrders'}  # type: ignore

    async def _purchase_initial(
        self,
        reservation_order_id: str,
        body: "models.PurchaseRequest",
        **kwargs
    ) -> "models.ReservationOrderResponse":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReservationOrderResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._purchase_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'reservationOrderId': self._serialize.url("reservation_order_id", reservation_order_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'PurchaseRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ReservationOrderResponse', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('ReservationOrderResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _purchase_initial.metadata = {'url': '/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}'}  # type: ignore

    async def begin_purchase(
        self,
        reservation_order_id: str,
        body: "models.PurchaseRequest",
        **kwargs
    ) -> AsyncLROPoller["models.ReservationOrderResponse"]:
        """Purchase ``ReservationOrder``.

        Purchase ``ReservationOrder`` and create resource under the specified URI.

        :param reservation_order_id: Order Id of the reservation.
        :type reservation_order_id: str
        :param body: Information needed for calculate or purchase reservation.
        :type body: ~azure_reservation_api.models.PurchaseRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either ReservationOrderResponse or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure_reservation_api.models.ReservationOrderResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReservationOrderResponse"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._purchase_initial(
                reservation_order_id=reservation_order_id,
                body=body,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('ReservationOrderResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'reservationOrderId': self._serialize.url("reservation_order_id", reservation_order_id, 'str'),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_purchase.metadata = {'url': '/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}'}  # type: ignore

    async def get(
        self,
        reservation_order_id: str,
        expand: Optional[str] = None,
        **kwargs
    ) -> "models.ReservationOrderResponse":
        """Get a specific ``ReservationOrder``.

        Get the details of the ``ReservationOrder``.

        :param reservation_order_id: Order Id of the reservation.
        :type reservation_order_id: str
        :param expand: May be used to expand the planInformation.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ReservationOrderResponse, or the result of cls(response)
        :rtype: ~azure_reservation_api.models.ReservationOrderResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ReservationOrderResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'reservationOrderId': self._serialize.url("reservation_order_id", reservation_order_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ReservationOrderResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}'}  # type: ignore
