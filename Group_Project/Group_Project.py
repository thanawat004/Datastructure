def convert_seconds(total_seconds):
    # 1 ชั่วโมง = 3600 วินาที
    hours = total_seconds // 3600

    # หาเศษวินาทีที่เหลือจากการตัดแบ่งชั่วโมง
    remaining_seconds = total_seconds % 3600

    # 1 นาที = 60 วินาที
    minutes = remaining_seconds // 60

    # เศษที่เหลือจากนาทีคือวินาที
    seconds = remaining_seconds % 60

    return hours, minutes, seconds


try:
    user_input = input("กรุณาป้อนจำนวนวินาทีที่ต้องการแปลง: ")
    input_seconds = int(user_input)

    # เรียกใช้ฟังก์ชัน
    h, m, s = convert_seconds(input_seconds)

    print(f"ผลลัพธ์: {input_seconds} วินาที = {h} ชั่วโมง {m} นาที {s} วินาที")

except ValueError:
    # เมื่อกรอกค่าไม่ใช่ตัวเลขจะเกิด Error
    print("❌ ไม่ถูกต้อง! กรุณาป้อนเฉพาะตัวเลขเท่านั้น")