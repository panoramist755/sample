import random

hands = ["�O�[","�`���L","�p�["]
results = {"win":"����", "lose":"����","draw":"������"}

def start_message():
    print("����񂯂�Q�[���X�^�[�g")
    
def get_my_hand():
    print("�����̎����͂��ĉ�����", end="")

    input_message = ""
    index = 0
    for hand in hands:
        input_message += str(index) + ":" + hand
        if index < 2:
            input_message += ","
        index += 1
        
    tmp = int(input(input_message))
    
    is_hand(tmp)
    
    return tmp

def is_hand(number):
    while (number < 0) or (number > 2):
        print("Error: ���l���͈͊O")
        get_my_hand()

def get_your_hand():
    return random.randint(0,2)

def get_hand_name(hand_number):
    return hands[hand_number]

def view_hand(my_hand, your_hand):
    print("���� : " + hands[my_hand])
    print("����� : " + hands[your_hand])

def get_result(hand_diff):
    if (hand_diff == -1) or (hand_diff == 2):
        return "win"
    elif hand_diff == 0:
        return "draw"
    else:
        return "lose"

def view_result(result):
    print(results[result])
    
def play():
    my_hand = get_my_hand() # 0�`2 ���߂�l
    your_hand = get_your_hand() # 0�`2 ���߂�l
    view_hand(my_hand, your_hand) #���҂̎������
    hand_diff = my_hand - your_hand # ���ʔ���
    result = get_result(hand_diff) # win�Ƃ��̕������Ԃ�
    view_result(result) # ��������������
    
    if result == "draw":
        play()
    

start_message()
play()
#my_hand = get_my_hand()
#your_hand = get_your_hand()
#view_hand(my_hand, your_hand)
#hand_diff = my_hand - your_hand
#print(results[get_result(hand_diff)])