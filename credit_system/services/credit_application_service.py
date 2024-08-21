from django.db.models import QuerySet
from credit_system.models import CreditApplicationModel


class CreditApplicationsService:

    @staticmethod
    def get_list_maker_for_contract(
        contract_id: int,
    ) -> QuerySet[CreditApplicationModel]:
        """
        Returns a list of unique makers associated with
        the specified contract and credit application
        """
        makers = CreditApplicationModel.objects.get(contract_id=contract_id)
        return makers
