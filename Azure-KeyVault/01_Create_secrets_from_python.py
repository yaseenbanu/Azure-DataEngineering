import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "keyvaultname"
KVUri = f"https://keyvaultname.vault.azure.net/"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

print(f"Creating a secret in KV_NAME")

client.set_secret("secretName", "s_Value")

print(" done.")

