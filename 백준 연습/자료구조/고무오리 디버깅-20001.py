input_word = input()

# 문제 목록 넣을 리스트 생성
st = []

# '고무오리 디버깅 끝'이 나올 때까지 input 반복
while input_word != '고무오리 디버깅 끝':
    input_word = input()

    # input값에 따라 실행
    if input_word == '문제':
        st.append(False)
    elif input_word == '고무오리':
        if len(st) == 0:
            # 비어있다면 벌칙
            st.append(False)
            st.append(False)
        elif len(st) > 0:
            # 문제 해결
            st.pop()
    elif input_word == '고무오리 디버깅 끝':
        break

if len(st) == 0:
    print('고무오리야 사랑해')
elif len(st) > 0:
    print('힝구')


