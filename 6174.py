import streamlit as st
import pandas as pd
import numpy as np
import time


ck = None
f_finished = None

st.title('不可思议的游戏：数字陷阱')

''
''
st.markdown('''
##### 游戏规则：
1. 挑选一个大于等于10的正整数（44， 6666666666这种全重复的整数除外）。
2. 将各个数字从大到小排列得到一个最大的数。
3. 再将各个数字从小到大排列得到一个最小的数。
4. 两数相减得到一个新的数。
5. 重复以上第2到第4步, 最终一定会掉进一个“数字陷阱”里，你相信吗？ -:)
''')


''
''

# st.markdown('##### 举几个栗子')
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown('''
    ##### 例子1
    1. 挑个4位数：2022
    2. 2220 - 0222 = 1998
    3. 9981 - 1899 = 8082
    4. 8820 - 0288 = 8532
    5. 8532 - 2358 = 6174
    6. 7141 - 1467 = 6174
    7. ............
    8. 陷在 6174 这个陷阱里了
    ''')
    
with c2:
    st.markdown('''
    ##### 例子2
    1. 挑个6位数：100174
    2. 741100 - 1147 = 739953
    3. 997533 - 335799 = 661734
    4. 766431 - 134667 = 631764
    5. 766431 - 134667 = 631764
    6. ............
    7. 陷在 631764 这个陷阱里了
    ''')

with c3:
    st.markdown('''
    ##### 例子3
    1. 挑个2位数：17
    2. 71 - 17 = 54
    3. 54 - 45 = 9
    4. 90 - 09 = 81
    5. 81 - 18 = 63
    6. 63 - 36 = 27
    7. 72 - 27 = 45
    8. 54 - 45 = 9
    9. ............
    10. 陷在 9->81->63->27->45再到9的循环这个陷阱圈里了
    ''')


st.markdown('''
##### 例子4，来个10位数试试
1. 挑个10位数：9931319652
2. 9996533211 - 1123356999 = 8873176212
3. 8877632211 - 1122367788 = 7755264423
4. 7765544322 - 2234455677 = 5531088645
5. 8865554310 - 134555688 = 8730998622
6. 9988763220 - 223678899 = 9765084321
7. 9876543210 - 123456789 = 9753086421
8. 9876543210 - 123456789 = 9753086421
9. ............
10. 陷在 9753086421 这个陷阱数里了
''')

# st.markdown('''
# ##### 例子4，来个30位数试试
# 1. 挑个10位数：377372902432111357296702806990 
# 2. 999987777766543333222221110000 - 11122222333345667777789999 = 999976655544209987554443320001
# 3. 999999877665555544444332210000 - 12233444445555566778999999 = 999987644221109988877553210001
# 4. 999999888877765544322211110000 - 11112223445567778888999999 = 999988776654319976543322110001
# 5. 999999887776665544333221111000 - 111122333445566677788999999 = 999888765443219977655432111001
# 6. 999998887776655544433221111100 - 1111122334445556677788899999 = 998887765442209987755432211101
# 7. 999988887777655544432222111100 - 1111222234445556777788889999 = 998877665543209987654433221101
# 8. 999988877766655544433322211100 - 1112223334445556667778889999 = 998876654432209987765543321101
# 9. 999988877766655544433322211100 - 1112223334445556667778889999 = 998876654432209987765543321101
# 9. ............
# 10. 陷在 998876654432209987765543321101 这个陷阱数里了
# ''')

''
''
''
st.header('轮到你来试试了')
number = st.text_input('请挑选个整数试试看')
# st.write(type(number))

if number != '':
    try:
        number = eval(number)
        if not isinstance(number, int):
            st.write('你输入的不是整数，请重新输入')
        elif number < 10:
                st.write('不能小于10，请重新输入')
        else:
            k = len(str(number))
            if number % int('1' * k) == 0:
                st.write('不能所有位置上的数字都一样，请重新输入')
            else:
                st.write('收到你的数字了，准备好了就开始吧')
                ck = st.button('我准备好了，让我掉到陷阱里吧')        
    except:
        st.write('你输入的不是数值，请重新输入')
    

if ck:
    # Add a placeholder
    '努力计算中...'
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'{i+1}% completed' )
      bar.progress(i + 1)
      time.sleep(0.01)
    
    '...and now we\'re done!'
    f_finished = 1

if f_finished:
    digits = len(str(number))
    steps = 0
    x = number
    history = [x]
    
    while steps < 1000:
        lst = list(str(x))
        lst = [int(x) for x in lst]
        while len(lst) < digits:
            lst.append(0)
    
        lst.sort()
        number_small, number_large = 0, 0
        for i in range(digits):
            number_small = number_small + lst[i] * 10 ** (digits - i - 1)
            number_large = number_large + lst[i] * 10 ** i
    
        diff = number_large - number_small
        steps = steps + 1
        st.write('step', steps, ':', x, '==>', number_large, '-', number_small, '=', diff)
        
        if diff == x:
            st.write('我掉进陷阱数里了啦！ 陷阱数是' + str(diff))
            break
        elif diff in history:
            trap = history[history.index(diff):]
            for i in history:
                if i in trap:
                    steps = history.index(i)
                    break
            # st.write('我掉进陷阱圈里了啦！ 陷阱圈是', trap, '步数：', steps)
            tt = str(trap[0])
            for t in trap[1:]:
                tt = tt + ' --> ' + str(t)
            st.write('我掉进陷阱圈里了啦！ 陷阱圈是' + tt)
            break
        else:
            x = diff
            history.append(diff)
