def get_formatted_city_country(name_city, name_country, population=''):
    """Genera un formato adeacuado para mostrar una ciudad de un pais."""
    if population:
        formatted_place = f"{name_city.title()}, {name_country.title()} - population {population}"
    else:
        formatted_place = f"{name_city}, {name_country}".title()
    return formatted_place