from rest_framework.response import Response
from rest_framework import status


class BaseResponse:

    @staticmethod
    def success(message="Operação realizada com sucesso", data=None, status_code=status.HTTP_200_OK):
        return Response(
            {
                "success": True,
                "message": message,
                **data
            },
            status=status_code
        )

    @staticmethod
    def error(message="Ocorreu um erro", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(
            {
                "success": False,
                "message": message,
                "errors": errors
            },
            status=status_code
        )
