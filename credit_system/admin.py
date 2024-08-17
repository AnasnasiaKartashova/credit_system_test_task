from django.contrib import admin
from credit_system.models import (
    MakerModel,
    ProductModel,
    ContractModel,
    CreditApplicationModel,
)


admin.site.register(MakerModel)
admin.site.register(ProductModel)
admin.site.register(ContractModel)
admin.site.register(CreditApplicationModel)
