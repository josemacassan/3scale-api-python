import pytest
import backoff

from tests.integration.conftest import account
from threescale_api.errors import ApiClientError

from tests.integration import asserts

def test_list_service_subscriptions(account, service_subscription):
    resource = account.service_subscriptions.list()
    assert len(resource) >= 1

def test_should_create_service_subscription(account, service_subscription, service_subscription_params):
    asserts.assert_resource(service_subscription)
    asserts.assert_resource_params(service_subscription, service_subscription_params)

def test_should_read_service_subscription(account, service_subscription, service_subscription_params):
    resource = account.service_subscriptions.read(service_subscription.entity_id)
    asserts.assert_resource(resource)
    asserts.assert_resource_params(service_subscription,service_subscription_params)



