from Crypto.PublicKey import RSA # Import the RSA class to generate public and private keys
from Crypto.Cipher import PKCS1_OAEP # Import PKCS1_OAEP for RSA encryption
from Crypto.Cipher import AES # Import AES for symmetric encryption
import os

def generate_RSA_keys():
    RSA_key=RSA.generate(2048) # Generates an RSA key pair with a 2048-bit length
    private_RSA_key=RSA_key.export_key() # Exports the private key
    public_RSA_key=RSA_key.publickey().export_key() # Exports the public key
    return private_RSA_key, public_RSA_key

def indicate_number_network_nodes():
    global number_network_nodes
    number_network_nodes=int(input("Enter the number of network nodes (layers) you want to use (remember, Tor usually only uses 3 nodes in most cases): "))
    print(f"The number of network nodes (layers) chosen is: {number_network_nodes}")
    confirm_message=input(f"Is '{number_network_nodes}' the correct number chosen (answer only with Y/N)? ").upper()
    if confirm_message=="Y":
        print("Answer Y has been selected. Then the program will proceed with the other necessary questions.")
    elif confirm_message=="N":
        print("Answer N has been selected. So, is possible rewrite the number of network nodes (layers) you want to use in the Tor network.")
        indicate_number_network_nodes()
    else:
        print("Invalid response. You can only respond with Y/N. Then the program will ask you to re-enter the number of network nodes (layers) you want to send in the Tor network.")
        indicate_number_network_nodes()
indicate_number_network_nodes()

network_nodes=[generate_RSA_keys() for _ in range(number_network_nodes)] # Create 3 network nodes with different keys

public_RSA_key=[network_node[1] for network_node in network_nodes] # Extract only the public keys
private_RSA_key=[network_node[0] for network_node in network_nodes] # Extract only the private keys

def generate_AES_key():
    return os.urandom(16) # Generates a random AES key (128 bits = 16 bytes)

def encrypt_with_AES(data, AES_key):
    cipher=AES.new(AES_key, AES.MODE_EAX)
    cipher_text, cipher_tag=cipher.encrypt_and_digest(data) # Encrypts the data and generates an authentication tag
    return cipher.nonce, cipher_text, cipher_tag

def decrypt_with_AES(nonce, cipher_text, cipher_tag, AES_key):
    cipher=AES.new(AES_key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(cipher_text, cipher_tag) # Decrypts the data and verifies the authentication tag

def encrypt_with_RSA(data, public_RSA_key):
    RSA_key=RSA.import_key(public_RSA_key) # Imports the RSA public key
    cipher=PKCS1_OAEP.new(RSA_key)
    return cipher.encrypt(data) # Encrypts the data with the public key

def decrypt_with_RSA(encrypted_data, private_RSA_key):
    RSA_key=RSA.import_key(private_RSA_key) # Imports the RSA private key
    cipher=PKCS1_OAEP.new(RSA_key)
    return cipher.decrypt(encrypted_data) # Decrypts the data with the private key

def create_onion_message(message, public_keys):
    # Generate an AES key for each node based on the number of public keys
    AES_keys=[generate_AES_key() for _ in public_keys]
    data=message.encode() # Convert the message to bytes
    # Iterate over the public keys in reverse order to apply onion encryption
    for i in reversed(range(len(public_keys))):
        # Encrypt the data using AES with the current key
        nonce, cipher_text, cipher_tag=encrypt_with_AES(data, AES_keys[i])
        # Encrypt the AES key using RSA with the current public key
        encrypted_AES_key=encrypt_with_RSA(AES_keys[i], public_keys[i])
        # Concatenate the encrypted AES key, nonce, ciphertext, and tag to form the onion message
        data=encrypted_AES_key+nonce+cipher_text+cipher_tag
    return data # Return the fully encrypted onion message

def process_onion_message(onion_message, private_keys):
    data=onion_message
    hexadecimal_data=data.hex()
    print()
    print(f"[START NODE] The initial encrypted message is: {hexadecimal_data}")
    print()
    for i in range(len(private_keys)): # Iterate (extracting) over the private keys to decrypt each layer of the onion network
        print(f"[STEP {i+1}] Decrypting layer {i+1}...")
        encrypted_AES_key=data[:256]
        hexadecimal_encrypted_AES_key=encrypted_AES_key.hex()
        print(f"[STEP {i+1}] Layer {i+1} - Extracted AES key (encrypted): {hexadecimal_encrypted_AES_key}")
        nonce=data[256:272]
        hexadecimal_nonce=nonce.hex()
        print(f"[STEP {i+1}] Layer {i+1} - Extracted nonce: {hexadecimal_nonce}")
        cipher_text=data[272:-16]
        hexadecimal_cipher_text=cipher_text.hex()
        print(f"[STEP {i+1}] Layer {i+1} - Extracted text: {hexadecimal_cipher_text}")
        cipher_tag=data[-16:]
        hexadecimal_cipher_tag=cipher_tag.hex()
        print(f"[STEP {i+1}] Layer {i+1} - Extracted tag: {hexadecimal_cipher_tag}")
        # Decrypt the AES key using the current private key
        AES_key=decrypt_with_RSA(encrypted_AES_key, private_keys[i])
        hexadecimal_AES_key=AES_key.hex()
        print(f"[STEP {i+1}] Layer {i+1} - Decrypted AES key: {hexadecimal_AES_key}")
        # Decrypt the message using the decrypted AES key
        data=decrypt_with_AES(nonce, cipher_text, cipher_tag, AES_key)
        hexadecimal_data=data.hex()
        print(f"[STEP {i+1}] Layer {i+1} - Decrypted data (layer {i+1} removed): {hexadecimal_data}")
        print()
    decoded_data=data.decode() # Decode the final decrypted message to string
    print(f"[FINAL NODE] The original message decrypted received is: {decoded_data}")

def writing_message():
    global message
    message=input("Enter your secret message to send with Tor network (e.g. 'The secret meeting is scheduled for March 25 at 10:00 AM in the underground bunker. The access code is 47A9X.'): ")
    print(f"The secret message that will be sent in the Tor network is the following: {message}")
    confirm_message=input(f"Is the written message '{message}' correct (reply with Y/N only)? ").upper()
    if confirm_message=="Y":
        print("Answer Y has been selected. Then the program will proceed to send the message to the Tor network.")
    elif confirm_message=="N":
        print("Answer N has been selected. So, is possible rewrite the message you want to send in the Tor network.")
        writing_message()
    else:
        print("Invalid response. You can only respond with Y/N. Then the program will ask you to re-enter the message you want to send to the Tor network.")
        writing_message()
writing_message()

onion_message=create_onion_message(message, public_RSA_key) # Create the onion message (apply onion routing encryption)
process_onion_message(onion_message, private_RSA_key) # Decrypt the onion message layer by layer using the private key
print()
program_exit=input("Press ENTER to exit the program...")