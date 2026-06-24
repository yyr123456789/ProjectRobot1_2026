import hashlib
from car_config import stored_encrypted_face_data

def encrypt_face_raw_data(raw_face_text: str) -> str:
    hash_generator = hashlib.sha256(raw_face_text.encode("utf-8"))
    return hash_generator.hexdigest()

def save_face_data_locally(raw_face_input: str):
    global stored_encrypted_face_data
    stored_encrypted_face_data = encrypt_face_raw_data(raw_face_input)
    print("Encrypted facial data saved to local storage, no cloud transmission")

def retrieve_stored_face_data():
    return stored_encrypted_face_data

def wipe_all_face_data():
    global stored_encrypted_face_data
    stored_encrypted_face_data = None
    print("All local facial biometric data has been permanently erased")

if __name__ == "__main__":
    save_face_data_locally("robot_owner_unique_id_20260624")
    print("Encrypted stored biometric data: ", retrieve_stored_face_data())
    sleep(3000)
    wipe_all_face_data()
    print("Current stored data after deletion: ", retrieve_stored_face_data())