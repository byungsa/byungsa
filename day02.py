empno = "2026001"
name = "김철수"
department = "정보전산팀"
role = "ADMIN"

if department == "정보전산팀" and role == "ADMIN":
    print(f"{name}님은 시스템 관리자입니다.")

elif department == "정보전산팀":
    print(f"{name}님은 일반 사용자입니다.")

else:
    print(f"{name}님은 타부서 사용자입니다.")