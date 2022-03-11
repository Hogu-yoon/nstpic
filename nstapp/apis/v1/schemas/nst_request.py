from ninja import Schema


# 우리가 받을 형식은 파일 제목 / 이미지 파일 그 자체
class NstRequest(Schema):
    key: str  # str => 문자열 타입
