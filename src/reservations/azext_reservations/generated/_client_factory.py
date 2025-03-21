# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_quota_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_reservations.vendored_sdks.quota import AzureReservationAPI
    return get_mgmt_service_client(cli_ctx,
                                   AzureReservationAPI,
                                   subscription_bound=False)


def cf_reservation(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).reservation


def cf_reservation_order(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).reservation_order


def cf_operation(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).operation


def cf_calculate_exchange(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).calculate_exchange


def cf_exchange(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).exchange


def cf_quota(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).quota


def cf_quota_request_status(cli_ctx, *_):
    return cf_quota_cl(cli_ctx).quota_request_status
