# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


helps['keyvault'] = """
    type: group
    short-summary: Safeguard and maintain control of keys, secrets, and certificates.
"""

helps['keyvault create'] = """
    type: command
    short-summary: Create a key vault.
    long-summary: Default permissions are created for the current user or service principal unless the `--no-self-perms` flag is specified.
"""

helps['keyvault delete'] = """
    type: command
    short-summary: Delete a key vault.
"""

helps['keyvault list'] = """
    type: command
    short-summary: List key vaults.
"""

helps['keyvault show'] = """
    type: command
    short-summary: Show details of a key vault.
"""

helps['keyvault update'] = """
    type: command
    short-summary: Update the properties of a key vault.
"""

helps['keyvault recover'] = """
    type: command
    short-summary: Recover a key vault.
    long-summary: Recovers a previously deleted key vault for which soft delete was enabled.
"""

helps['keyvault key'] = """
    type: group
    short-summary: Manage keys.
"""

helps['keyvault secret'] = """
    type: group
    short-summary: Manage secrets.
"""

helps['keyvault certificate'] = """
    type: group
    short-summary: Manage certificates.
"""

helps['keyvault storage'] = """
    type: group
    short-summary: Manage storage accounts.
"""

helps['keyvault storage sas-definition'] = """
    type: group
    short-summary: Manage storage account SAS definitions.
"""

helps['keyvault network-rule'] = """
    type: group
    short-summary: Manage vault network ACLs.
"""

helps['keyvault certificate download'] = """
    type: command
    short-summary: Download the public portion of a Key Vault certificate.
    long-summary: The certificate formatted as either PEM or DER. PEM is the default.
    examples:
        - name: Download a certificate as PEM and check its fingerprint in openssl.
          text: >
            az keyvault certificate download --vault-name vault -n cert-name -f cert.pem && \\
            openssl x509 -in cert.pem -inform PEM  -noout -sha1 -fingerprint
        - name: Download a certificate as DER and check its fingerprint in openssl.
          text: >
            az keyvault certificate download --vault-name vault -n cert-name -f cert.crt -e DER && \\
            openssl x509 -in cert.crt -inform DER  -noout -sha1 -fingerprint
"""

helps['keyvault certificate get-default-policy'] = """
    type: command
    short-summary: Get the default policy for self-signed certificates.
    long-summary: >
        This default policy can be used in conjunction with `az keyvault create` to create a self-signed certificate.
        The default policy can also be used as a starting point to create derivative policies.\n

        For more details, see: https://docs.microsoft.com/en-us/rest/api/keyvault/certificates-and-policies
    examples:
        - name: Create a self-signed certificate with the default policy
          text: >
            az keyvault certificate create --vault-name vaultname -n cert1 \\
              -p "$(az keyvault certificate get-default-policy)"
"""

helps['keyvault certificate create'] = """
    type: command
    short-summary: Create a Key Vault certificate.
    long-summary: Certificates can be used as a secrets for provisioned virtual machines.
    examples:
        - name: Create a self-signed certificate with the default policy and add it to a virtual machine.
          text: >
            az keyvault certificate create --vault-name vaultname -n cert1 \\
              -p "$(az keyvault certificate get-default-policy)"

            secrets=$(az keyvault secret list-versions --vault-name vaultname \\
              -n cert1 --query "[?attributes.enabled].id" -o tsv)

            vm_secrets=$(az vm secret format -s "$secrets") \n

            az vm create -g group-name -n vm-name --admin-username deploy  \\
              --image debian --secrets "$vm_secrets"
"""

helps['keyvault certificate import'] = """
    type: command
    short-summary: Import a certificate into KeyVault.
    long-summary: Certificates can also be used as a secrets in provisioned virtual machines.
    examples:
        - name: Create a service principal with a certificate, add the certificate to Key Vault and provision a VM with that certificate.
          text: >
            service_principal=$(az ad sp create-for-rbac --create-cert) \n

            cert_file=$(echo $service_principal | jq .fileWithCertAndPrivateKey -r) \n

            az keyvault create -g my-group -n vaultname \n

            az keyvault certificate import --vault-name vaultname -n cert_file \n

            secrets=$(az keyvault secret list-versions --vault-name vaultname \\
              -n cert1 --query "[?attributes.enabled].id" -o tsv)

            vm_secrets=$(az vm secret format -s "$secrets") \n

            az vm create -g group-name -n vm-name --admin-username deploy  \\
              --image debian --secrets "$vm_secrets"
"""

helps['keyvault certificate pending'] = """
    type: group
    short-summary: Manage pending certificate creation operations.
"""

helps['keyvault certificate contact'] = """
    type: group
    short-summary: Manage contacts for certificate management.
"""

helps['keyvault certificate issuer'] = """
    type: group
    short-summary: Manage certificate issuer information.
"""

helps['keyvault certificate issuer admin'] = """
    type: group
    short-summary: Manage admin information for certificate issuers.
"""
