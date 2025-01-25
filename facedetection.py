import cv2
import face_recognition
import os

def encode_known_faces(known_faces_dir):
    known_encodings = []
    known_names = []

    for file_name in os.listdir(known_faces_dir):
        file_path = os.path.join(known_faces_dir, file_name)
        image = face_recognition.load_image_file(file_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(file_name)[0])

    return known_encodings, known_names

def detect_and_recognize_faces(video_source, known_encodings, known_names):
    video_capture = cv2.VideoCapture(video_source)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    
        cv2.imshow("Video Feed", frame)

    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    known_faces_dir = "known_faces"

    print("Encoding known faces...")
    known_encodings, known_names = encode_known_faces(known_faces_dir)

    print(f"Encoded {len(known_names)} known faces.")

    print("Starting video feed...")
    detect_and_recognize_faces(0, known_encodings, known_names)
