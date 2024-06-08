# Helium Gateway Docker Compose

This repository contains a simple Docker Compose setup for a Helium gateway running on a Raspberry Pi 4 with a RAK2287 concentrator (RAK Hotspot v2). The setup includes two services: `udp-packet-forwarder` and `gateway-rs`. The `gateway-rs` service is operated through a REST API, which allows for starting, stopping, fetching gateway information, and adding a gateway.

## Services

### udp-packet-forwarder

The `udp-packet-forwarder` service forwards LoRaWAN packets from the gateway to the network server using the UDP protocol. It supports the RAK2287 concentrator and is configurable for other concentrators. This service is essential for ensuring that LoRaWAN packets are correctly transmitted from the gateway to the network server.

### gateway-rs

The `gateway-rs` service connects to the Helium network using Semtech's Gateway Messaging Protocol (GWMP). It sends and witnesses Proof of Coverage beacons and routes packets to the Helium Packet Router. The service can be configured to use an ECC608 crypto chip for secure key storage and crypto operations. Additionally, it is operated through a REST API, which allows for starting, stopping, fetching gateway information, and adding a gateway.

#### Start helium_gateway

To start the gateway, make the following POST request to the `/start_gateway` endpoint:

```http
POST http://localhost:8080/start_gateway
```

#### Stop helium_gateway

To stop the gateway, make the following POST request to the `/stop_gateway` endpoint:

```http
POST http://localhost:8080/stop_gateway
```

#### Get gateway info

To get information about the gateway, make the following GET request to the `/get_info` endpoint:

```http
GET http://localhost:8080/get_info
```

This returns a JSON object containing the gateway address, mode, owner, payer, and the transaction, e.g:

```json
{
  "info": "{n  \"key\": \"11JZvAvGTWK4LQUT14W8t9hR1rS8WNGdw8HdZR3yyFTYEMsza97\",\n  \"onboarding\": \"11JZvAvGTWK4LQUT14W8t9hR1rS8WNGdw8HdZR3yyFTYEMsza97\",\n  \"name\": \"ancient-pewter-wolverine\"\n}\n"
}
```

#### Add a gateway

To add a gateway, make the following POST request to the `/add_gateway` endpoint:

```http
POST http://localhost:8080/add_gateway
Content-Type: application/json
{
    "owner": "14GWyFj9FjLHzoN3aX7Tq7PL6fEg4dfWPY8CrK8b9S5ZrcKDz6S",
    "payer": "14GWyFj9FjLHzoN3aX7Tq7PL6fEg4dfWPY8CrK8b9S5ZrcKDz6S",
    "mode": "full"
}
```

The output will be a JSON object containing the gateway address, mode, owner, payer and the transaction, e.g:

```json
{
  "address": "11TL62V8NYvSTXmV5CZCjaucskvNR1Fdar1Pg4Hzmzk5tk2JBac",
  "mode": "full",
  "owner": "14GWyFj9FjLHzoN3aX7Tq7PL6fEg4dfWPY8CrK8b9S5ZrcKDz6S",
  "payer": "14GWyFj9FjLHzoN3aX7Tq7PL6fEg4dfWPY8CrK8b9S5ZrcKDz6S",
  "txn": "CrkBCiEBrlImpYLbJ0z0hw5b4g9isRyPrgbXs9X+RrJ4pJJc9MkSIQA7yIy7F+9oPYCTmDz+v782GMJ4AC+jM+VfjvUgAHflWSJGMEQCIGfugfLkXv23vJcfwPYjLlMyzYhKp+Rg8B2YKwnsDHaUAiASkdxUO4fdS33D7vyid8Tulizo9SLEL1lduyvda9YVRCohAa5SJqWC2ydM9IcOW+IPYrEcj64G17PV/kayeKSSXPTJOMCEPUDo+wM="
}
```
