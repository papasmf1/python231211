# 정규 표현식 패턴을 정의합니다.
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# 이메일 주소 샘플 리스트를 만듭니다.
email_samples = [
    "user@example.com",               # 유효한 이메일 주소입니다.
    "first.last@example.co.jp",       # 유효한 이메일 주소입니다.
    "john.doe123@sub.domain.co.uk",   # 유효한 이메일 주소입니다.
    "invalid-email",                  # 유효하지 않은 이메일 주소입니다.
    "not_an_email@",                  # 유효하지 않은 이메일 주소입니다.
    "@missing_username.com",           # 유효하지 않은 이메일 주소입니다.
    "user@.com",                      # 유효하지 않은 이메일 주소입니다.
    "user@sub@domain.com",            # 유효하지 않은 이메일 주소입니다.
    "user@domain",                    # 유효하지 않은 이메일 주소입니다.
    "user@123.45",                    # 유효하지 않은 이메일 주소입니다.
]

# 각 샘플에 대해 이메일 주소를 체크합니다.
for email in email_samples:
    match = re.search(email_pattern, email)  # 정규 표현식을 사용하여 이메일 주소를 찾습니다.
    if match:
        print(f"'{email}'은(는) 유효한 이메일 주소입니다.")  # 유효한 이메일 주소일 경우 출력합니다.
    else:
        print(f"'{email}'은(는) 유효하지 않은 이메일 주소입니다.")  # 유효하지 않은 이메일 주소일 경우 출력합니다.
