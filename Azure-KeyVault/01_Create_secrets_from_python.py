from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Replace with your Key Vault URL
key_vault_url = "https://<your-key-vault-name>.vault.azure.net/"

# Initialize the SecretClient with DefaultAzureCredential
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Create a new secret
secret_name = "MySecretKey"
secret_value = "SuperSecretValue123!"

try:
    # Add the secret to Key Vault
    created_secret = secret_client.set_secret(secret_name, secret_value)
    print(f"Secret '{created_secret.name}' created successfully with value '{created_secret.value}'")
except Exception as e:
    print(f"An error occurred: {e}")

