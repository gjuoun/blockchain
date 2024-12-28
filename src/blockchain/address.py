import hashlib
import os
import ecdsa
import base58
import bech32

class Address:
    """Represents a blockchain address with public/private key pair"""
    
    def __init__(self, private_key: bytes = None, address_type: str = 'P2PKH'):
        """
        Initialize an address with optional private key and address type.
        If no private key is provided, generates a new one.
        
        Args:
            private_key: Optional private key bytes
            address_type: Address type - 'P2PKH', 'P2SH', or 'Bech32'
        """
        if private_key is None:
            self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        else:
            self.private_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
            
        self.public_key = self.private_key.get_verifying_key()
        self.address_type = address_type
        self.address = self._generate_address()
    
    def _generate_address(self) -> str:
        """Generate the address from the public key based on address type"""
        # Hash the public key using SHA-256
        sha256_hash = hashlib.sha256(self.public_key.to_string()).digest()
        # Hash the result with RIPEMD-160
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
        
        if self.address_type == 'P2PKH':
            return self._generate_p2pkh_address(ripemd160_hash)
        elif self.address_type == 'P2SH':
            return self._generate_p2sh_address(ripemd160_hash)
        elif self.address_type == 'Bech32':
            return self._generate_bech32_address(ripemd160_hash)
        else:
            raise ValueError("Invalid address type. Choose 'P2PKH', 'P2SH', or 'Bech32'")
    
    def _generate_p2pkh_address(self, hash160: bytes) -> str:
        """Generate P2PKH address (starts with 1)"""
        # Add version byte (0x00 for mainnet)
        versioned_payload = b'\x00' + hash160
        # Calculate checksum
        checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
        # Base58 encode
        return base58.b58encode(versioned_payload + checksum).decode()
    
    def _generate_p2sh_address(self, hash160: bytes) -> str:
        """Generate P2SH address (starts with 3)"""
        # Add version byte (0x05 for mainnet)
        versioned_payload = b'\x05' + hash160
        # Calculate checksum
        checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
        # Base58 encode
        return base58.b58encode(versioned_payload + checksum).decode()
    
    def _generate_bech32_address(self, hash160: bytes) -> str:
        """Generate Bech32 address (starts with bc1)"""
        # Convert hash160 to 5-bit words
        converted = bech32.convertbits(hash160, 8, 5)
        # Encode as Bech32
        return bech32.bech32_encode('bc', [0] + converted)
