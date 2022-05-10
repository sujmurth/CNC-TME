# CNC-NSO-SDK Demo

The objective of this demo is to use a sample L3VPN service package developed on NSO based on legacy features. Attach external plan package to generate plan and notifications to be consumed in CNC for lifecycle management of NSO Service 

Steps : 

1. Load L3VPN package , external plan , juniper ned and iosxrcli NED on NSO
2. Assuming Devices are added on NSO , pick PE and CE nodes from topology .
3. Load topology.txt and vpn.txt from payloads folder to create Service
4. Load bootstrap.xml to mapy plan data to service elements 
5. Perform re-deploy of service 
