def bmi_calc(weight, height):
    return weight / (height / 100) ** 2

def bmi_cat(weight, height):
    bmi_value = bmi_calc(weight, height)
    if bmi_value < 18.5:
        text = "ต่ำกว่าเกณฑ์"
    elif 18.5 <= bmi_value <= 25:
        text = "ตามเกณฑ์"
    elif 25 <= bmi_value <= 30:
        text = "เกินเกณฑ์"
    elif bmi_value > 30:
        text = "อ้วน"
    return text

if __name__ == '__main__':
    w, h = 70, 170
    print(f"BMI Value: {bmi_calc(w, h):.2f}")
    print(f"BMI Category: {bmi_cat(w, h)}")