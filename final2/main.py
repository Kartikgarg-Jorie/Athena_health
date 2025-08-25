import json
from get_access_token import get_access_token
from create_open_slot import create_open_slot
from book_appointment import book_appointment
from create_note import create_note
from get_note import get_notes   # import your notes fetch function

def ask_yes_no(question):
    while True:
        ans = input(f"{question} (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please type 'y' or 'n'.")

def main():
    # Ask for patient ID
    patient_id = input("Enter patient ID: ").strip()
    if not patient_id:
        raise ValueError("Patient ID cannot be empty")

    token = None
    appointment_id = None
    open_slot_resp = None
    booking_resp = None
    note_resp = None
    notes_resp = None  # to store fetched notes

    # Step 1: Get token
    if ask_yes_no("Run get_access_token()?"):
        token = get_access_token()
    else:
        print("Skipping token fetch.")

    # Step 2: Create open slot
    if ask_yes_no("Run create_open_slot()?"):
        if not token:
            print("❌ Cannot create open slot without token.")
        else:
            open_slot_resp = create_open_slot(token)
            if "appointmentid" in open_slot_resp:
                appointment_id = open_slot_resp["appointmentid"]
            elif "appointmentids" in open_slot_resp and isinstance(open_slot_resp["appointmentids"], dict):
                appointment_id = list(open_slot_resp["appointmentids"].keys())[0]
            if not appointment_id:
                print("⚠ No appointmentid returned when creating open slot.")
    else:
        print("Skipping create_open_slot.")

    # Step 3: Book appointment
    if ask_yes_no("Run book_appointment()?"):
        if not token or not appointment_id:
            print("❌ Cannot book appointment without token and appointment_id.")
        else:
            booking_resp = book_appointment(token, appointment_id, patient_id)
    else:
        print("Skipping book_appointment.")

    # Step 4: Create note
    if ask_yes_no("Run create_note()?"):
        if not token or not appointment_id:
            print("❌ Cannot create note without token and appointment_id.")
        else:
            note_resp = create_note(token, appointment_id)
    else:
        print("Skipping create_note.")

    # Step 5: Get notes for the appointment
    if ask_yes_no("Run get_notes()?"):
        if not token or not appointment_id:
            print("❌ Cannot get notes without token and appointment_id.")
        else:
            notes_resp = get_notes(token, appointment_id, show_deleted=True)
    else:
        print("Skipping get_notes.")

    # Final Summary
    print("\n=== Summary ===")
    print(json.dumps({
        "open_slot": open_slot_resp,
        "booking": booking_resp,
        "note": note_resp,
        "notes": notes_resp
    }, indent=2))

if __name__ == "__main__":
    main()
