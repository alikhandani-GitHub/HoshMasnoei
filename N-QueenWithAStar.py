import time
from queue import PriorityQueue

# تابع تشکیل و تخمین هزینه برای هر حالت
def heuristic(state):
    # محاسبه تعداد تهدیدهای هر وزیر
    threats = 0
    n = len(state)
    
    for i in range(n):
        for j in range(i+1, n):
            # بررسی تهدید در سطرها و قطرها
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                threats += 1
    
    return threats

# تابع حل مسئله با استفاده از الگوریتم A*
def solve_n_queen_a_star(n):
    start_state = tuple([0] * n)  # حالت شروع با همه وزیر در ستون اول
    
    # اولویت بندی صف با استفاده از تابع ارزیابی (تخمین هزینه)
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic(start_state), start_state))
    
    while not priority_queue.empty():
        # استخراج حالت با کمترین تخمین هزینه از صف
        current_state = priority_queue.get()[1]
        
        if heuristic(current_state) == 0:
            # یافتن راه حل
            return current_state
        
        # تولید حالت‌های فرزند
        for i in range(n):
            for j in range(n):
                if current_state[i] != j:
                    new_state = list(current_state)
                    new_state[i] = j
                    priority_queue.put((heuristic(new_state), tuple(new_state)))
    
    # در صورت عدم یافتن راه حل
    return None



# تست کد با 5 وزیر
n = 5

start_time = time.time()  # زمان شروع
solution = solve_n_queen_a_star(n)
end_time = time.time()  # زمان پایان

if solution is None:
    print("هیچ راه حلی وجود ندارد")
else:
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += "- "
        print(line)

execution_time = end_time - start_time
execution_time_seconds = execution_time % 60
execution_time_minutes = (execution_time // 60) % 60
execution_time_hours = execution_time // 3600

print("زمان مصرفی الگوریتم: {} ساعت {} دقیقه {} ثانیه".format(execution_time_hours, execution_time_minutes, execution_time_seconds))
