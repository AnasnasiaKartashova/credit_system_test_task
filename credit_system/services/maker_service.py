from django.db.models import QuerySet
from credit_system.models import MakerModel


class MakerService:

    @staticmethod
    def get_list_maker_for_contract(contract_id: int) -> QuerySet[MakerModel]:
        """
        Returns a list of unique makers associated with
        the specified contract and credit application
        """
        makers = MakerModel.objects.filter(product__credit_application__contract=contract_id).distinct()
        return makers
