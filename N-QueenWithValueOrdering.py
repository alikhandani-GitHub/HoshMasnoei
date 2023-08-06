#با استفاده از روش ترتیب مقادیر، کد حل مسئله N-Queen به صورت زیر است:
import random

def TadaKholeVazir(board, row, col, n):
    # بررسی تهدید شدن وزیر با وزیرهای قبلی در سطرها و قطرها
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def Hale(board, col, n):
    # شرط پایانی: تمام وزیرها قرار گرفته‌اند
    if col >= n:
        return True

    # ترتیب مقادیر را تصادفی تعیین می‌کنیم
    values = list(range(n))
    random.shuffle(values)

    for i in values:
        # بررسی امکان قرار دادن وزیر در سطر فعلی
        if TadaKholeVazir(board, i, col, n):
            # قرار دادن وزیر در سطر فعلی
            board[i][col] = 1

            # حل مسئله به صورت بازگشتی برای ستون بعدی
            if Hale(board, col + 1, n):
                return True

            # اگر قرار دادن وزیر در سطر فعلی به حل مسئله منجر نشود، آن را برمی‌گردانیم به صورت 0
            board[i][col] = 0

    # اگر هیچ سطری برای قرار دادن وزیر در ستون فعلی وجود نداشته باشد، مسئله حل نشده است
    return False

def HaleMasale(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if Hale(board, 0, n):
        # چاپ راه حل
        for row in board:
            print(row)
    else:
        print("هیچ راه حلی وجود ندارد")

# تست کد با 8 وزیر
HaleMasale(8)