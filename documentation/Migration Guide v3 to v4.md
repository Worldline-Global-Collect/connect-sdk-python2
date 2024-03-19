# Migrating from version 3.x.x to 4.0.0

## Imports

All package names have been renamed, and some classes have moved to different packages. Each API version now has its own package structure that contains all classes specific for that version, including classes like `APIError`, exceptions and webhooks classes.

You need to change your imports as follows:

| Previous package                     | Class                        | New package                          | Notes |
|--------------------------------------|------------------------------|--------------------------------------|-------|
| ingenico.connect.sdk                 | ApiException                 | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | Authenticator                | worldline.connect.sdk.authentication |
| ingenico.connect.sdk                 | AuthorizationException       | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | CommunicationException       | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | Connection                   | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | DataObject                   | worldline.connect.sdk.domain         |
| ingenico.connect.sdk                 | DeclinedPaymentException     | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | DeclinedPayoutException      | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | DeclinedRefundException      | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | DeclinedTransactionException | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | GlobalCollectException       | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | IdempotenceException         | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | Marshaller                   | worldline.connect.sdk.json           |
| ingenico.connect.sdk                 | MarshallerSyntaxException    | worldline.connect.sdk.json           |
| ingenico.connect.sdk                 | MetaDataProvider             | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | MultipartFormDataObject      | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | MultipartFormDataRequest     | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | NotFoundException            | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | ParamRequest                 | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | PooledConnection             | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | ReferenceException           | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | RequestHeader                | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | RequestParam                 | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | ResponseException            | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | ResponseHeader               | worldline.connect.sdk.communication  |
| ingenico.connect.sdk                 | UploadableFile               | worldline.connect.sdk.domain         |
| ingenico.connect.sdk                 | ValidationException          | worldline.connect.sdk.v1             |
| ingenico.connect.sdk                 | All other classes            | worldline.connect.sdk                |
| ingenico.connect.sdk.defaultimpl     | AuthorizationType            | worldline.connect.sdk.authentication |
| ingenico.connect.sdk.defaultimpl     | DefaultAuthenticator         | worldline.connect.sdk.authentication |
| ingenico.connect.sdk.defaultimpl     | DefaultConnection            | worldline.connect.sdk.communication  |
| ingenico.connect.sdk.defaultimpl     | DefaultMarshaller            | worldline.connect.sdk.json           |
| ingenico.connect.sdk.domain.metadata | ShoppingCartExtension        | worldline.connect.sdk.domain         |
| ingenico.connect.sdk.domain.*        | All other domain classes     | worldline.connect.sdk.v1.domain      | All domain classes for version 1 of the API are now in the same package |
| ingenico.connect.sdk.log             | All classes                  | worldline.connect.sdk.log            |
| ingenico.connect.sdk.merchant.*      | All classes                  | worldline.connect.sdk.v1.merchant.*  | The same package structure is used |
| ingenico.connect.sdk.webhooks        | WebhooksHelper               | worldline.connect.sdk.v1.webhooks    |
| ingenico.connect.sdk.webhooks        | All other classes            | worldline.connect.sdk.webhooks       |

In addition, all modules containing webhooks related classes have been renamed to use `webhooks` instead of `web_hooks`. You need to replace all occurrences in your code.

## API calls

Method `merchant` of class `Client` has moved to new class `V1Client`. Instances of this class are available through method `v1` of class `Client`. You need to replace all occurrences of `.merchant` with `.v1().merchant` in your code. For instance:

```python
response = client.v1().merchant(merchantId).services().testconnection()
```

## API version

Method `API_VERSION` of class `Client` has been removed. You need to replace all occurrences in your code with string literal `"v1"`.

## ApiResource

The `arg` parameter of the constructor of class `ApiResource` has been split into separate `parent` and `communicator` parameters, to make it clear what it means. At least one of the two must be given. The following shows what changes to constructor calls you need to make:

| Previous arguments                             | New arguments                                                                             |
|------------------------------------------------|-------------------------------------------------------------------------------------------|
| (parent)                                       | (parent=parent)                                                                           |
| (parent, path_context)                         | (parent=parent, path_context=path_context)                                                |
| (parent, path_context, client_meta_info)       | (parent=parent, path_context=path_context, client_meta_info=client_meta_info)             |
| (communicator)                                 | (communicator=communicator)                                                               |
| (communicator, path_context)                   | (communicator=communicator, path_context=path_context)                                    |
| (communicator, path_context, client_meta_info) | (communicator=communicator, path_context=path_context, client_meta_info=client_meta_info) |

Method `_create_exception` has been removed. You need to replace all occurrences in your code with calls to function `create_exception` in module `worldline.connect.sdk.v1.exception_factory`. Note that this function is specific for version 1 of the API.

## Factory

Parameters `api_key_id` and `secret_api_key` of methods of class `Factory` have been replaced with more generic parameters `authorization_id` and `authorization_secret`. If you use named parameters you need to need to replace all occurrences in your code with the new names. Alternatively you can use positional parameters instead. For instance:

```python
configuration = Factory.create_configuration("configuration", "api_key_id", "secret_api_key")
```

## GlobalCollectException

Class `GlobalCollectException` has been renamed to `PlatformException`. You need to replace all occurrences in your code with the new name.

## Session

Class `Session` has been integrated into class `Communicator`. Because class `Session` no longer exists, methods `create_session_from_configuration`, `create_session_from_file`, `create_communicator_from_session` and `create_client_from_session` of class `Factory` have been removed as well. The `create_communicator_from_configuration`, `create_communicator_from_file`, `create_client_from_configuration` and `create_client_from_file` of class `Factory` all have additional optional parameters for the `MetadataProvider`, `Connection`, `Authenticator` and `Marshaller` to make it easier to create `Communicator` or `Client` instances with non-default values for some of the `Communicator` components.

If you used class `Factory` to instantiate class `Session` you need to use method `create_communicator_from_configuration` or `create_communicator_from_file` instead. For instance:

```python
communicator = Factory.create_communicator_from_file("configuration.ini", "api_key_id", "secret_api_key", connection=connection)
client = Factory.create_client_from_communicator(communicator)
```

If you instantiated class `Session` directly you can need to instantiate class `Communicator` instead. The constructor now has the same parameters that the `Session` constructor did, plus the already present parameter for the `Marshaller`. For instance:

```python
communicator = Communicator(api_endpoint, connection, authenticator, metadata_provider, marshaller)
```

## Authentication

### Authenticator

The `create_simple_authentication_signature` method of class `Authenticator` has been renamed to `get_authorization`. You need to replace all occurrences in your code with the new name.

### DefaultAuthenticator

Class `DefaultAuthenticator` has been renamed to `V1HMACAuthenticator`. You need to replace all occurrences in your code with the new name.

The `authorization_type` parameter has been dropped from the constructor, as it should always be `"v1HMAC"`. You need to remove the first argument for all calls to the constructor in your code.

## Communication

### Connection

Class `Connection` now extends class `ObfuscationCapable`. You need to implement the `set_body_obfuscator` and `set_header_obfuscator` methods in all custom implementations.

## JSON marshalling

### DefaultMarshaller

Method `INSTANCE` of class `DefaultMarshaller` has been renamed to `instance`. You need to replace all occurrences in your code with the new name.

## Metadata

### MetaDataProvider

Class `MetaDataProvider` and its `meta_data_headers` property used incorrect capitalization. These have been renamed to `MetadataProvider` and `metadata_headers` respectively. You need to replace all occurrences in your code with the new names.

### Integrator

The integrator is now required. When using a configuration file to initialize the SDK, you need to make sure that key `connect.api.integrator` inside the `ConnectSDK` section is present with a non-empty value. Otherwise, you need to make sure a non-empty integrator is set on any `CommunicatorConfiguration` or `MetadataProvider` instance you create.

## Logging

### SysOutCommunicatorLogger

Method `INSTANCE` of class `SysOutCommunicatorLogger` has been renamed to `instance`. You need to replace all occurrences in your code with the new name.

## Webhooks

### Creating webhooks helpers

Method `create_helper`  of class `Webhooks` has moved to new class `V1WebhooksFactory`. Instances of this class are available through method `v1` of class `Webhooks`. You need to include `.v1()` for all occurrences of `Webhooks.create_helper` in your code. For instance:

```python
helper = Webhooks.v1().create_helper(InMemorySecretKeyStore.instance())
```

### WebhooksHelper

Method `_validate` of class `WebhooksHelper` has been removed. You need to replace all occurrences in your code with a `SignatureValidator`.

### WebhooksHelperBuilder

Class `WebhooksHelperBuilder` and method `create_helper_builder` of class `Webhooks` have been removed. You need to replace all occurrences in your code with calls to method `create_helper` of class `V1WebhooksFactory`. For instance

```python
helper = Webhooks.v1().create_helper(InMemorySecretKeyStore.instance(), marshaller)
```

### InMemorySecretKeyStore

Method `INSTANCE` of class `InMemorySecretKeyStore` has been renamed to `instance`. You need to replace all occurrences in your code with the new name.

### SecretKeyNotAvailableException

The parameters of the constructor of class `SecretKeyNotAvailableException` have been reordered and renamed to make it clear what each means. The required `key_id` parameter now comes first. The following shows what changes to constructor calls you need to make:

| Previous arguments       | New arguments                          |
|--------------------------|----------------------------------------|
| (message, key_id)        | (key_id, message=message)              |
| (key_id, cause)          | (key_id, cause=cause)                  |
| (message, key_id, cause) | (key_id, message=message, cause=cause) |

### SignatureValidationException

The parameters of the constructor of class `SignatureValidationException` have been renamed to make it clear what each means. The following shows what changes to constructor calls you need to make:

| Previous arguments | New arguments                  |
|--------------------|--------------------------------|
| (message)          | (message=message)              |
| (cause)            | (cause=cause)                  |
| (message, cause)   | (message=message, cause=cause) |
