from services.models import ServicesRieltor, Valuation, Repair, Insurance, Cleaning, InstallationWater, UniversalService


def return_list_services():
        list_services = []
        if ServicesRieltor.get_solo().is_enable:
            list_services.append(ServicesRieltor.get_solo())
        if Valuation.get_solo().is_enable:
            list_services.append(Valuation.get_solo())
        if Repair.get_solo().is_enable:
            list_services.append(Repair.get_solo())
        if Insurance.get_solo().is_enable:
            list_services.append(Insurance.get_solo())
        if Cleaning.get_solo().is_enable:
            list_services.append(Cleaning.get_solo())
        if InstallationWater.get_solo().is_enable:
            list_services.append(InstallationWater.get_solo())
        if UniversalService.objects.all().exists():
            for universal in UniversalService.objects.all():
                if universal.is_enable:
                    list_services.append(universal)
        return list_services