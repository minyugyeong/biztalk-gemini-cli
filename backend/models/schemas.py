from enum import Enum
from pydantic import BaseModel, Field

class TargetAudience(str, Enum):
    """
    수신 대상 페르소나 정의
    """
    BOSS = "boss"
    COLLEAGUE = "colleague"
    CLIENT = "client"
    TEAM = "team"

class ConvertRequest(BaseModel):
    """
    말투 변환 요청을 위한 데이터 모델
    """
    text: str = Field(..., description="변환할 원문 텍스트", example="오늘 회의 늦을 것 같아.")
    target_audience: TargetAudience = Field(..., description="수신 대상 (boss, colleague, client, team)")

class ConvertResponse(BaseModel):
    """
    말투 변환 응답을 위한 데이터 모델
    """
    converted_text: str = Field(..., description="변환된 결과 텍스트")
    target_audience: TargetAudience = Field(..., description="적용된 수신 대상")
    original_text: str = Field(..., description="사용자가 입력한 원문 텍스트")
