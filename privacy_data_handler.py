import hashlib
from car_config import stored_encrypted_face_data

def encrypt_raw_data(raw_text: str) -> str:
    digest = hashlib.sha256(raw_text.encode("utf-8"))
    return digest.hexdigest()

def store_face_data(raw_input: str):
    global stored_encrypted_face_data
    stored_encrypted_face_data = encrypt_raw_data(raw_input)
    print("Encrypted facial data stored locally, no cloud upload")

def get_stored_data():
    return stored_encrypted_face_data

def clear_all_data():
    global stored_encrypted_face_data
    stored_encrypted_face_data = None
    print("All local facial biometric data erased permanently")

if __name__ == "__main__":
    store_face_data("robot_owner_id_20260624")
    print("Encrypted data: ", get_stored_data())
    sleep(3000)
    clear_all_data()
    print("Data after wipe: ", get_stored_data())
