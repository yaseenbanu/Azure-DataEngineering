import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "keyvaultname"
KVUri = f"https://keyvaultname.vault.azure.net/"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

# secretName = "azurestoragedatasets-access-key"
# secretValue = "Sg4RwMEpqQd7zL5lV7plrT2bKGR7wrNhf4lRfkCcXgsCZHX8xHzqMkw68gTg4Y0+mX6CYu0QUDY2+AStHK5hsg=="

secretName = 'azurestoragedatasets-connection-strings'
secretValue = 'DefaultEndpointsProtocol=https;AccountName=azurestoragedataset;AccountKey=abcdef;EndpointSuffix=core.windows.net'

print(f"Creating a secret in KV_NAME called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print(" done.")

# print(f"Retrieving your secret from KV_NAME.")

# retrieved_secret = client.get_secret(secretName)

# print(f"Your secret is '{retrieved_secret.value}'.")
# print(f"Deleting your secret from KV_NAME ...")

# poller = client.begin_delete_secret(secretName)
# deleted_secret = poller.result()

# print(" done.")
