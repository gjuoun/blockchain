import hashlib
import os
import ecdsa

class Address:
    """Represents a blockchain address with public/private key pair"""
    
    def __init__(self, private_key: bytes = None):
        """
        Initialize an address with optional private key.
        If no private key is provided, generates a new one.
        """
        if private_key is None:
            self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        else:
            self.private_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
            
        self.public_key = self.private_key.get_verifying_key()
        self.address = self._generate_address()
    
    def _generate_address(self) -> str:
        """Generate the address from the public key"""
        # Hash the public key using SHA-256
        sha256_hash = hashlib.sha256(self.public_key.to_string()).hexdigest()
        # Hash the result with RIPEMD-160
        ripemd160_hash = hashlib.new('ripemd160', sha256_hash.encode()).hexdigest()
        return ripemd160_hash
    
    def sign(self, data: bytes) -> bytes:
        """Sign data using the private key"""
        return self.private_key.sign(data)
    
    def verify(self, signature: bytes, data: bytes) -> bool:
        """Verify a signature using the public key"""
        return self.public_key.verify(signature, data)
    
    def get_private_key(self) -> bytes:
        """Get the private key as bytes"""
        return self.private_key.to_string()
    
    def get_public_key(self) -> bytes:
        """Get the public key as bytes"""
        return self.public_key.to_string()
    
    def get_address(self) -> str:
        """Get the address string"""
        return self.address
