from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from credit_system.serializers.make_serializer import MakeSerializer
from credit_system.services.credit_application_service import CreditApplicationsService


class MakersListView(APIView):

    def get(self, request, contract_id: int):
        """
        Returns a list of unique makers associated
        Your have to pass contract_id in the url
        """
        try:
            makers = CreditApplicationsService.get_list_maker_for_contract(contract_id)
            if makers:

                serializer = MakeSerializer(makers, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(
                {"message": "Makers not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
