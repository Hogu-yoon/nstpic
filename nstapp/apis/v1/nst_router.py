from .schemas import NstRequest, NstResponse
from ninja.files import UploadedFile
from ninja import Router, File, Form
from django.http import HttpRequest

from nstapp.service.nst_service import nst_apply

router = Router()


@router.post("/", response=NstResponse)
def nst(request: HttpRequest, nst_request: NstRequest = Form(...), img: UploadedFile = File(...)) -> dict:
    # 서비스 함수
    # nst 변환 적용 후에 s3 업로드 해주는 서비스

    file_url = nst_apply(nst_request.key, img)
    print("최종 response :", file_url)
    return {"file_url": file_url}
