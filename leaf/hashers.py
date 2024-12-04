from django.contrib.auth.hashers import BasePasswordHasher, mask_hash
from django.utils.crypto import constant_time_compare, get_random_string
import hashlib

class CustomPasswordHasher(BasePasswordHasher):
    algorithm = "custom_algorithm"
    
    def encode(self, password, salt):
        hash = hashlib.sha256(f"{password}{salt}".encode()).hexdigest()
        return f"{self.algorithm}${salt}${hash}"
    
    def verify(self, password, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded_2)
    
    def safe_summary(self, encoded):
        algorithm, salt, hash = encoded.split('$', 2)
        return {
            'algorithm': algorithm,
            'salt': mask_hash(salt),
            'hash': mask_hash(hash),
        }
    
    def salt(self):
        return get_random_string(8)
