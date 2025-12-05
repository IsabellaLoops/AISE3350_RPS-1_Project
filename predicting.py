from ultralytics import YOLO
import cv2
import os
import decisions

# Folders to store the images captured by the webcam
team_folder = "Data/team"
opponent_folder = "Data/opponent"

# Helper function to capture N photos
def capture_images(n, save_folder, label):
    cap = cv2.VideoCapture(0)
    print(f"\n--- Capturing {n} images for: {label} ---")
    print("Press SPACE to take a photo. Press Q to quit early.\n")

    img_num = 1
    while img_num <= n:
        ret, frame = cap.read()
        if not ret:
            print("Error reading frame.")
            break

        cv2.imshow("Press SPACE to Capture", frame)
        key = cv2.waitKey(1) & 0xFF

        # Capture image if space is pressed
        if key == ord(' '):
            filename = f"{label}_{img_num}.jpg"
            filepath = os.path.join(save_folder, filename)
            cv2.imwrite(filepath, frame)
            img_num += 1

        # Quit early
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Capture team hands
capture_images(2, team_folder, "team")

# Capture opponent hands
capture_images(2, opponent_folder, "opponent")



# Load the model
model = YOLO("runs/classify/train2/weights/best.pt")

# Predict all the hands; connect to where the webcam images are being stored
teamHand1 = model("Data/team/team_1.jpg")[0]
teamHand1Index = teamHand1.probs.top1
teamHand1Label = teamHand1.names[teamHand1Index]
teamHand1Conf  = teamHand1.probs.top1conf

teamHand2 = model("Data/team/team_2.jpg")[0]
teamHand2Index = teamHand2.probs.top1
teamHand2Label = teamHand2.names[teamHand2Index]
teamHand2Conf  = teamHand2.probs.top1conf

oppHand1 = model("Data/opponent/opponent_1.jpg")[0]
oppHand1Index = oppHand1.probs.top1
oppHand1Label = oppHand1.names[oppHand1Index]
oppHand1Conf  = oppHand1.probs.top1conf

oppHand2 = model("Data/opponent/opponent_2.jpg")[0]
oppHand2Index = oppHand2.probs.top1
oppHand2Label = oppHand2.names[oppHand2Index]
oppHand2Conf  = oppHand2.probs.top1conf

# turn all the hands into a combination
if (teamHand1Label == "rock" and teamHand2Label == "paper") or (teamHand1Label == "paper" and teamHand2Label == "rock"):
    our_move = "rock_paper"
elif (teamHand1Label == "rock" and teamHand2Label == "scissors") or (teamHand1Label == "scissors" and teamHand2Label == "rock"):
    our_move = "rock_scissors"
elif (teamHand1Label == "paper" and teamHand2Label == "scissors") or (teamHand1Label == "scissors" and teamHand2Label == "paper"):
    our_move = "paper_scissors"
else: # we play the same thing (not recommended)
    our_move = teamHand1Label + "_" + teamHand2Label

if (oppHand1Label == "rock" and oppHand2Label == "paper") or (oppHand1Label == "paper" and oppHand2Label == "rock"):
    opponent_move = "rock_paper"
elif (oppHand1Label == "rock" and oppHand2Label == "scissors") or (oppHand1Label == "scissors" and oppHand2Label == "rock"):
    opponent_move = "rock_scissors"
elif (oppHand1Label == "paper" and oppHand2Label == "scissors") or (oppHand1Label == "scissors" and oppHand2Label == "paper"):
    opponent_move = "paper_scissors"
else: # they play the same thing
    opponent_move = oppHand1Label + "_" + oppHand2Label

print(our_move)
print(opponent_move)


if our_move == "rock_paper":
    play = decisions.rock_paper_chosen(opponent_move)
elif our_move == "rock_scissors":
    play = decisions.We_Play_RS(opponent_move)
elif our_move == "paper_scissors":
    play = decisions.we_play_scissors_paper(opponent_move)
else: # In case we play two of the same
    play = teamHand1

print()
print("Play " + play)