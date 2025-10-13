import hashlib


def sha1(input_string: str) -> str:
    sha1_hash = hashlib.sha1(input_string.encode("utf-8"))
    return sha1_hash.hexdigest()


def calculate_file_hash(path, blocksize=65536):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            data = f.read(blocksize)
            if not data:
                break
            h.update(data)
    return h.hexdigest()
