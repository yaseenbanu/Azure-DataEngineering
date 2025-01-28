import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "keyvaultname"
KVUri = f"https://keyvaultname.vault.azure.net/"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = 'azurestoragedatasets-connection-strings'
s_Value = 'value'

print(f"Creating a secret in KV_NAME called '{secretName}' with the value '{s_Value}' ...")

client.set_secret(secretName, s_Value)

print(" done.")

